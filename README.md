# 🦠 COVID-19 Data Pipeline – AWS + Python + Power BI

Dette prosjektet demonstrerer en full datapipeline for COVID-19-data: fra innhenting via API, til lagring i AWS, SQL-spørring med Athena, og visualisering i Power BI. Rapporten fokuserer på utviklingen i Norge og gir innsikt på nasjonalt og fylkesnivå.

---

## 📌 Formål

- Hente og prosessere daglige COVID-19-data
- Bygge en datalake-løsning med AWS S3 og Glue
- Koble til Athena for SQL-spørringer mot Parquet-data
- Visualisere utvikling og nøkkeltall med Power BI

---

## 🏗️ Arkitektur
- API → Python → Parquet → Amazon S3 → AWS Glue → Amazon Athena → Power BI

 
| Komponent     | Teknologi             | Funksjon |
|---------------|------------------------|----------|
| Datakilde     | [covid-api.com](https://covid-api.com) | Tilbyr rådata om smitte, dødsfall og friskmeldte |
| Databehandling| Python (`pandas`, `pyarrow`, `boto3`) | Henter, transformerer og lagrer som Parquet |
| Lagring       | Amazon S3             | Skylagring for strukturert data |
| Katalog       | AWS Glue              | Automatisk tabellopprettelse basert på S3-data |
| Analyse       | Amazon Athena         | SQL-basert spørring direkte på S3-data |
| Visualisering | Power BI              | Interaktive dashboards og filtrering |

---

## 💻 Teknologier brukt

- Python 3.10+
- pandas, requests, boto3, pyarrow
- AWS S3, Glue, Athena
- Power BI Desktop
- Amazon Athena ODBC-driver

---

## 📊 Power BI-rapport – Innhold

Rapporten er bygget opp som et 3-siders interaktivt dashboard:

| Side                 | Visualiseringer                              |
|----------------------|----------------------------------------------|
| `COVID-19 Oversikt`  | KPI-tall, smittetrend, dødsfall over tid     |
| `Fylkesvis Analyse`  | Kartvisning og søyler per fylke              |
| `Utvikling Over Tid` | Daglige endringer og tidsbaserte diagrammer  |

📍 **Filtrering med slicers**:
- Land (`country_region`)
- Fylke (`admin_region_1`)
- Dato (`updated`)

---

## 📁 Mappestruktur
COVID-19 Data Pipeline/
├── covid_to_s3.py # Python-script for ETL
├── visuals/
│ └── visuals.png # Skjermbilde av Power BI-rapport
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md


## 📤 Power BI-rapportfil

⚠️ `.pbix`-filen er **ikke inkludert i repoet** på grunn av GitHubs filstørrelsesgrense (130 MB > 100 MB).

📎 Du kan laste ned den fullstendige Power BI-rapporten her:

🔗 **[Last ned CovidDashboard.pbix fra Google Drive](https://drive.google.com/file/d/DEIN-FIL-ID/view?usp=sharing)**

📸 Forhåndsvisning er tilgjengelig i `visuals/dashboard_preview.png`.

---

## ▶️ Kom i gang

### 1. Klon repoet
```bash
git clone https://github.com/<ditt-brukernavn>/covid-data-lake.git
cd covid-data-lake
pip install -r requirements.txt
python scripts/covid_to_s3.py

