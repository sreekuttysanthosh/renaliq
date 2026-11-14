# Explainable Machine Learning for Screening Kidney Disease Markers Among Adults with Diabetes Using NHANES Clinical Data

## Project Overview

This project develops an explainable machine learning framework to identify kidney abnormality markers among adults with diabetes using publicly available data from the National Health and Nutrition Examination Survey (NHANES), 2017–March 2020 pre-pandemic cycle.

The project integrates demographic, examination, laboratory, and questionnaire data to identify participants with kidney abnormality markers using estimated glomerular filtration rate (eGFR) and urine albumin-to-creatinine ratio (UACR).

Three machine learning algorithms are developed and compared:

- Logistic Regression
- Random Forest
- XGBoost

SHAP (SHapley Additive exPlanations) is used to interpret model predictions. A Streamlit dashboard is being developed to demonstrate model predictions and interpretability.

**This project is intended for research and educational purposes. It is not a clinical diagnostic tool.**

## Objectives

- Integrate and preprocess relevant NHANES datasets.
- Identify adults with diabetes using documented cohort criteria.
- Define kidney abnormality using eGFR and UACR thresholds.
- Perform exploratory data analysis and data-quality assessment.
- Prevent target leakage during feature selection and model development.
- Develop and compare three machine learning classification models.
- Interpret model predictions using SHAP.
- Develop a Streamlit-based research prototype.
- Examine model limitations, fairness, and generalizability.

## Dataset

**Source:** National Health and Nutrition Examination Survey (NHANES), CDC.

**Study cycle:** 2017–March 2020 pre-pandemic cycle.

Relevant datasets include:

- Demographic data
- Diabetes questionnaire
- Examination and body measurement data
- Blood pressure measurements
- Laboratory measurements
- Smoking questionnaire
- Urine albumin and creatinine measurements

Datasets are merged using the NHANES participant identifier, `SEQN`.

Participant identifiers are used for data integration and are excluded from model predictors.

## Cohort Definition

Adults aged 20 years or older with diabetes are identified using one or more of the following criteria:

- Self-reported diabetes diagnosis
- Use of diabetes medication
- HbA1c ≥ 6.5%

## Kidney Abnormality Definition

Kidney abnormality is defined as either:

- eGFR < 60 mL/min/1.73 m²
- UACR ≥ 30 mg/g

eGFR is calculated using the race-free CKD-EPI 2021 equation.

The NHANES-provided UACR value is used and checked against its underlying urine measurements.

## Methodology

The project follows these stages:

1. NHANES data collection and integration.
2. Data cleaning and quality assessment.
3. Diabetes cohort identification.
4. Kidney abnormality outcome construction.
5. Exploratory data analysis.
6. Feature selection and leakage audit.
7. Missing-value handling and preprocessing.
8. Stratified train-test splitting.
9. Model training and cross-validation.
10. Model evaluation and comparison.
11. SHAP-based explainability.
12. Streamlit dashboard development.

All preprocessing transformations are fitted using training data to avoid information leakage.

## Machine Learning Models

The following classification models are implemented:

| Model | Description |
|---|---|
| Logistic Regression | Baseline linear classification model |
| Random Forest | Ensemble of decision trees |
| XGBoost | Gradient-boosted tree model |

### Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrices

Special attention is given to the trade-off between missed kidney abnormality cases and false-positive predictions.

## Explainable AI

SHAP is used to understand model behaviour through:

- Global feature importance
- SHAP summary plots
- Individual prediction explanations

These explanations describe how model features contribute to predictions. They do not establish causation.

## Streamlit Dashboard

The planned dashboard will provide:

- Selection between Logistic Regression, Random Forest, and XGBoost.
- Participant feature inputs.
- Predicted kidney abnormality marker status.
- Estimated model probability.
- Model explanations, where supported.
- Research-use disclaimer and limitations.

## Technology Stack

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- XGBoost
- SHAP
- Joblib
- Streamlit
- Jupyter Notebook / Google Colab
- Git and GitHub

## Repository Structure

```text
renaliq-main/
│
├── data/
│   └── README.md
│
├── models/
│   ├── all_models.joblib
│   └── model_metadata.json
│
├── notebooks/
│   ├── data_preparation.ipynb
│   ├── exploratory_data_analysis.ipynb
│   └── modeling.ipynb
│
├── src/
│   └── ...
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
└── README.md
```

*The structure above is the intended organization; notebook and source filenames should be adjusted to match the actual repository.*

## Installation and Usage

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd renaliq-main
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit dashboard

```bash
python -m streamlit run dashboard/app.py
```

The dashboard will open in your browser.

## Privacy and Data Handling

NHANES is a publicly available research dataset. However, participant-level health information should be handled responsibly.

- Raw and participant-level datasets should not be committed to a public repository.
- Participant identifiers must not be used as model predictors.
- Only appropriate code and safe aggregate outputs should be shared publicly.
- Data handling should follow applicable ethical and privacy principles.

## Limitations

- NHANES is cross-sectional; the project identifies existing kidney abnormality markers rather than predicting future disease.
- A single abnormal eGFR or UACR measurement does not establish chronic kidney disease.
- Model performance may be affected by missing data, sample size, and class imbalance.
- Findings may not generalize to other populations.
- Model explanations indicate associations within the model, not causal relationships.
- The prototype has not been clinically validated.

## Disclaimer

This project is developed exclusively for academic, research, and educational purposes. Predictions indicate model-estimated kidney abnormality marker status and must not be interpreted as a diagnosis of chronic kidney disease or used as a substitute for professional medical assessment.

## Acknowledgements

Data used in this project are obtained from the National Health and Nutrition Examination Survey (NHANES), conducted by the U.S. Centers for Disease Control and Prevention (CDC).

## Project Status

Research and development in progress. Model development and pipeline verification have been completed for three candidate classifiers. Streamlit integration, dashboard testing, and final documentation are ongoing.
