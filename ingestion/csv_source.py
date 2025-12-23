import csv
from schemas.raw_schema import RawRecord

def fetch_csv_data():
    records = []
    with open("data/sample.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(RawRecord(
                name=row["name"],
                value=float(row["value"])
            ))
    return records
