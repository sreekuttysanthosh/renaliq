from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer, MissingIndicator
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

NUMERIC = ["RIDAGEYR", "INDFMPIR", "LBXGH", "BMXBMI", "BPXOSY1", "BPXODI1"]
BINARY = ["female", "insulin"]
CATEGORICAL = ["smoking"]
TARGET = "kidney_marker"

def build_preprocessor(numeric=NUMERIC, binary=BINARY, categorical=CATEGORICAL, scale=True):
    # Numbers: fill missing with the median, then scale (if scale=True)
    steps = [("impute", SimpleImputer(strategy="median"))]
    if scale:
        steps.append(("scale", StandardScaler()))
    return ColumnTransformer([
        ("num", Pipeline(steps), numeric),
        # "Was missing" flags stay 0/1 and are never scaled
        ("miss", MissingIndicator(features="missing-only"), numeric),
        ("bin", "passthrough", binary),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical),
    ])