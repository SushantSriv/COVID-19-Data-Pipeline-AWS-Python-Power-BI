import pandas as pd
import requests
import datetime
import os
import boto3
import pyarrow as pa
import pyarrow.parquet as pq

# 📁 Lag mappe
os.makedirs("data", exist_ok=True)

# 📅 Datoer fra 2021-01-01 til 2022-01-01
start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2022, 1, 1)
date_list = [start_date + datetime.timedelta(days=i) for i in range((end_date - start_date).days)]

records = []

for date in date_list:
    formatted_date = date.isoformat()
    url = "https://covid-api.com/api/reports/total?date=" + formatted_date + "&iso=NOR"
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        if json_data.get("data") and json_data["data"].get("confirmed") is not None:
            data = json_data["data"]
            data["date"] = formatted_date
            records.append(data)

# ✅ Lag DataFrame
df = pd.DataFrame(records)

if df.empty:
    print("❌ Ingen data funnet.")
else:
    print("✅ Antall rader: {}".format(len(df)))

    # Rydd opp kolonner (valgfritt)
    df = df[["date", "confirmed", "deaths", "recovered", "active", "fatality_rate"]]
    df["date"] = pd.to_datetime(df["date"])

    # 💾 Lag Parquet
    table = pa.Table.from_pandas(df)
    pq.write_table(table, "data/covid_norway_history.parquet")

    # ⬆️ Last opp til S3
    s3 = boto3.client("s3")
    bucket_name = "covid-datalake-sushant"
    s3.upload_file("data/covid_norway_history.parquet", bucket_name, "covid-data/covid_norway_history.parquet")

    print("✅ Historiske data lastet opp til S3!")
