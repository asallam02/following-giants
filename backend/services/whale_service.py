import csv
from pathlib import Path

filename = "obis_seamap_dataset_1755_points.csv"
DATA_FILE = Path(__file__).parent.parent / "data" / "whales" / filename

def load_blue_whale_data(limit: int = 100):
    """Load manually downloaded CSV data for mapping"""
    records = []
    with open(DATA_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if i >= limit:
                break
            records.append({
                "id": row.get("occurrence_id"),
                "scientificName": row.get("scientific_name"),
                "commonName": row.get("common_name"),
                "latitude": float(row.get("decimal_latitude", 0)),
                "longitude": float(row.get("decimal_longitude", 0)),
                "eventDate": row.get("event_date"),
                "individualCount": row.get("individual_count"),
                "platform": row.get("platform"),
                "provider": row.get("provider"),
                "notes": row.get("notes"),
            })

    return records
