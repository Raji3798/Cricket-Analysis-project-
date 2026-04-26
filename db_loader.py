from sqlalchemy import create_engine
import pandas as pd
import os
import sqlite3

BASE_DIR = "C:/Users/DS/Documents/cricketsheet/data/processed"

# Create SQLite DB
engine = create_engine("sqlite:///cricket.db")

formats = ["odi", "t20", "test", "ipl"]

for fmt in formats:
    file_path = os.path.join(BASE_DIR, f"{fmt}.csv")

    print(f"\n📥 Loading {fmt.upper()} data...")

    df = pd.read_csv(file_path)

    # Table name
    table_name = f"{fmt}_matches"

    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"✅ Loaded into table: {table_name}")
    print(f"Rows: {len(df)}")

print("\n🎉 All tables created successfully!")

conn = sqlite3.connect("cricket.db")

query = "SELECT name FROM sqlite_master WHERE type='table';"
print(pd.read_sql(query, conn))