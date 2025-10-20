# Import AAC CSV into MongoDB, idempotent on animal_id
import pandas as pd
from crud import AnimalShelter

CSV_PATH = "aac_shelter_outcomes.csv"

def main():
    db = AnimalShelter()
    df = pd.read_csv(CSV_PATH)
    df = df.where(pd.notnull(df), None)  # NaNs -> None

    n_insert = 0
    for rec in df.to_dict(orient="records"):
        aid = rec.get("animal_id")
        if not aid:
            continue
        res = db.collection.update_one(
            {"animal_id": aid},
            {"$setOnInsert": rec},
            upsert=True
        )
        if res.upserted_id:
            n_insert += 1
    print(f"Upsert complete. Inserted new: {n_insert}, total now: {db.count()}")

if __name__ == "__main__":
    main()
