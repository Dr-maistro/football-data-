
import requests
from pathlib import Path

BASE_URL = "https://raw.githubusercontent.com/jfjelstul/worldcup/master/data-csv"
TABLES = ["matches", "goals", "players", "teams"]

def main():
    out_dir = Path("datasets/worldcup")
    out_dir.mkdir(parents=True, exist_ok=True)
    for table in TABLES:
        response = requests.get(f"{BASE_URL}/{table}.csv")
        with open(out_dir / f"{table}.csv", "wb") as f:
            f.write(response.content)
    print("تم تحديث بيانات كأس العالم.")

if __name__ == "__main__": main()
