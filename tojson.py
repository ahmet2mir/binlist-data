import csv
import json

# idea: add CSV to wildq :)

results = []
with open('binlist-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

    for row in reader:
        if len(row) != 12:
            raise Exception(f"Issue with row {row}, fix it first")

        results.append({
            "bin": row["bin"],
            "brand": row["brand"],
            "type": row["type"],
            "category": row["category"],
            "issuer": row["issuer"],
            "alpha_2": row["alpha_2"],
            "alpha_3": row["alpha_3"],
            "country": row["country"],
            "latitude": row["latitude"],
            "longitude": row["longitude"],
            "bank_phone": row["bank_phone"],
            "bank_url": row["bank_url"],
        })

with open("binlist-data.json", "w") as fd:
    fd.write(json.dumps(results, indent=2,))
