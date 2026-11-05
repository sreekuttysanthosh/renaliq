from pathlib import Path
import pandas as pd

FILES = ["P_DEMO", "P_DIQ", "P_GHB", "P_BIOPRO",
         "P_ALB_CR", "P_BMX", "P_BPXO", "P_SMQ"]

def fix_sas_zeros(df, tol=1e-70):
    # SAS files store some zeros as tiny numbers like 5e-79; turn them into real 0.0
    df = df.copy()
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].mask(df[col].abs() < tol, 0.0)
    return df

def load_raw_tables(raw_dir="data/raw"):
    tables = {}
    for name in FILES:
        df = pd.read_sas(Path(raw_dir) / f"{name}.xpt", format="xport")
        tables[name] = fix_sas_zeros(df)
    return tables