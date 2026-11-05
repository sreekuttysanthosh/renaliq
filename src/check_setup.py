
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import scipy
import sklearn

# Find the root project folder
project_root = Path(__file__).resolve().parent.parent

print("=" * 50)
print("KIDNEY DISEASE ANALYTICS — SETUP CHECK")
print("=" * 50)

print(f"Python version: {sys.version.split()[0]}")
print(f"Python executable: {sys.executable}")
print(f"Project root: {project_root}")

print("\nPackage versions:")
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"Seaborn: {sns.__version__}")
print(f"SciPy: {scipy.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")

print("\nFolder checks:")
for folder in ["data/raw", "data/interim", "data/processed",
               "notebooks", "src", "reports", "docs", "tests"]:
    path = project_root / folder
    print(f"{'OK' if path.is_dir() else 'MISSING'}: {folder}")

print("\nSETUP CHECK COMPLETED")
