import numpy as np
import pandas as pd

def egfr_ckdepi_2021(scr, age, female):
    """Race-free 2021 CKD-EPI creatinine equation. scr in mg/dL."""
    kappa = np.where(female, 0.7, 0.9)
    alpha = np.where(female, -0.241, -0.302)
    ratio = scr / kappa
    egfr = (142
            * np.minimum(ratio, 1) ** alpha
            * np.maximum(ratio, 1) ** -1.200
            * 0.9938 ** age
            * np.where(female, 1.012, 1.0))
    return egfr

def label_outcome(df):
    """Adds egfr, uacr_ok flags and a label: 1, 0, or NaN (unlabelable)."""
    df = df.copy()
    female = df["RIAGENDR"] == 2
    df["egfr"] = egfr_ckdepi_2021(df["LBXSCR"], df["RIDAGEYR"], female)
    low_egfr = df["egfr"] < 60
    high_uacr = df["URDACT"] >= 30
    both_known = df["egfr"].notna() & df["URDACT"].notna()
    both_normal = both_known & ~low_egfr & ~high_uacr
    df["kidney_marker"] = np.where(low_egfr | high_uacr, 1,
                           np.where(both_normal, 0, np.nan))
    return df