import os
import json
import pandas as pd
from tqdm import tqdm

BASE_DIR = "C:/Users/DS/Documents/cricketsheet/data/raw_json"
OUTPUT_DIR = "C:/Users/DS/Documents/cricketsheet/data/processed"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_match(file_path, match_type):
    records = []

    with open(file_path, "r") as f:
        data = json.load(f)

    match_id = os.path.basename(file_path).replace(".json", "")

    innings = data.get("innings", [])

    for inning in innings:
        team = inning.get("team")   # ✅ FIXED
        overs = inning.get("overs", [])

        for over_data in overs:
            over_num = over_data.get("over")

            deliveries = over_data.get("deliveries", [])

            for ball_index, delivery in enumerate(deliveries):

                batter = delivery.get("batter")
                bowler = delivery.get("bowler")

                runs = delivery.get("runs", {})
                batter_runs = runs.get("batter", 0)
                extras = runs.get("extras", 0)
                total_runs = runs.get("total", 0)

                wicket = 1 if "wickets" in delivery else 0

                records.append({
                    "match_id": match_id,
                    "match_type": match_type,
                    "team": team,
                    "batsman": batter,
                    "bowler": bowler,
                    "runs": batter_runs,
                    "extras": extras,
                    "total_runs": total_runs,
                    "over": over_num,
                    "ball": ball_index + 1,
                    "is_wicket": wicket
                })

    return records

def process_format(format_name):
    print(f"\n🚀 Processing {format_name.upper()} matches...")

    folder = os.path.join(BASE_DIR, format_name)
    all_records = []

    files = [f for f in os.listdir(folder) if f.endswith(".json")]

    for file in tqdm(files[:500]):  # LIMIT initially
        file_path = os.path.join(folder, file)

        try:
            records = process_match(file_path, format_name)
            all_records.extend(records)
        except Exception as e:
            print(f"⚠️ Error in {file}: {e}")

    df = pd.DataFrame(all_records)

    output_path = os.path.join(OUTPUT_DIR, f"{format_name}.csv")
    df.to_csv(output_path, index=False)

    print(f"✅ Saved: {output_path}")
    print(df.head())


# Run for all formats
for fmt in ["odi", "t20", "test", "ipl"]:
    process_format(fmt)