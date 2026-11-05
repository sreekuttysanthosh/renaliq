# Downloads NHANES 2017-March 2020 pre-pandemic files into data/raw/
import urllib.request
from pathlib import Path

BASE = "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/"
FILES = ["P_DEMO", "P_DIQ", "P_GHB", "P_BIOPRO",
         "P_ALB_CR", "P_BMX", "P_BPXO", "P_SMQ"]

PROJECT_ROOT = Path(__file__).resolve().parent.parent
raw_dir = PROJECT_ROOT / "data" / "raw"
raw_dir.mkdir(parents=True, exist_ok=True)

for name in FILES:
    target = raw_dir / f"{name}.xpt"
    if target.exists():                      # skip files already downloaded
        print("Already have", name)
        continue
    url = f"{BASE}{name}.xpt"
    print("Downloading", url)
    urllib.request.urlretrieve(url, target)  # save the file to disk

print("Done.")