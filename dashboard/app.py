from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
import streamlit as st


st.set_page_config(page_title="Renal AI", page_icon="🩺")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "random_forest_pipeline.joblib"
THRESHOLD = 0.5  # The project metadata says this is the default, untuned threshold.


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_resource
def load_shap_explainer():
    model = load_model()
    return shap.TreeExplainer(model.named_steps["classifier"])


st.title("Renal AI")
st.write("A student project that explores kidney-related screening markers.")

if MODEL_PATH.exists():
    model = load_model()
else:
    model = None
    st.error(
        "The Random Forest pipeline was not found. Check that "
        "models/random_forest_pipeline.joblib exists in the project folder."
    )

st.header("Patient information")
st.write("Enter the nine features used by the project model.")

age = st.number_input("Age in years", min_value=20, max_value=80, value=45)
sex = st.selectbox("Sex", ["Female", "Male"])
income = st.number_input("Family income-to-poverty ratio", min_value=0.0, value=1.0)
hba1c = st.number_input("HbA1c", min_value=0.0, value=6.0)
bmi = st.number_input("BMI", min_value=0.0, value=25.0)
systolic = st.number_input("Systolic blood pressure", min_value=0, value=120)
diastolic = st.number_input("Diastolic blood pressure", min_value=0, value=80)
smoking = st.selectbox("Smoking status", ["never", "former", "current", "unknown"])
insulin_choice = st.selectbox("Insulin status", ["Yes", "No", "Unknown"])

if st.button("Predict", disabled=model is None):
    input_row = pd.DataFrame(
        [
            {
                "RIDAGEYR": age,
                "female": 1 if sex == "Female" else 0,
                "INDFMPIR": income,
                "LBXGH": hba1c,
                "BMXBMI": bmi,
                "BPXOSY1": systolic,
                "BPXODI1": diastolic,
                "smoking": smoking,
                "insulin": {"Yes": 1, "No": 0, "Unknown": np.nan}[insulin_choice],
            }
        ]
    )

    try:
        positive_class_index = list(model.classes_).index(1)
        positive_probability = float(
            model.predict_proba(input_row)[0, positive_class_index]
        )
        predicted_positive = positive_probability >= THRESHOLD

        st.subheader("Project model result")
        st.metric("Estimated probability for the study-defined kidney marker", f"{positive_probability:.1%}")
        st.write(
            "Model classification: **positive** for the study-defined kidney marker."
            if predicted_positive
            else "Model classification: **negative** for the study-defined kidney marker."
        )
        st.caption(f"Classification threshold: {THRESHOLD:.0%} (default; not separately tuned).")

        st.subheader("Why did the model make this estimate?")
        try:
            preprocessor = model.named_steps["preprocessor"]
            transformed_input = preprocessor.transform(input_row)
            if hasattr(transformed_input, "toarray"):
                transformed_input = transformed_input.toarray()

            shap_explanation = load_shap_explainer()(transformed_input)
            shap_values = shap_explanation.values
            base_values = np.asarray(shap_explanation.base_values)

            if shap_values.ndim == 3:
                local_values = shap_values[0, :, positive_class_index]
                local_base_value = base_values.reshape(-1, len(model.classes_))[
                    0, positive_class_index
                ]
            else:
                local_values = shap_values[0]
                local_base_value = base_values.reshape(-1)[0]

            waterfall = shap.Explanation(
                values=local_values,
                base_values=local_base_value,
                data=np.asarray(transformed_input)[0],
                feature_names=preprocessor.get_feature_names_out(),
            )
            shap.plots.waterfall(waterfall, max_display=10, show=False)
            st.pyplot(plt.gcf(), clear_figure=True)
            plt.close()
            st.caption(
                "Features pushing right increase the model output for the study-defined "
                "kidney marker; features pushing left decrease it. These are model "
                "contributions, not causes."
            )
        except Exception as error:
            st.warning(f"The prediction worked, but its SHAP explanation could not be created: {error}")

        with st.expander("See the model inputs"):
            st.dataframe(input_row, hide_index=True)
    except Exception as error:
        st.error(f"Prediction failed: {error}")

st.header("About")
st.write("This project uses NHANES data for academic analysis.")

st.header("Limitations")
st.warning(
    "This is an academic project, not a medical diagnostic tool. "
    "It does not replace laboratory tests or advice from healthcare professionals. "
    "The displayed probability is a model estimate for the study label, not a diagnosis."
)
