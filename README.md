## Backend & ETL System
Backend ETL System – Crypto Data Ingestion
This project is a Dockerized backend ETL system that ingests cryptocurrency data from public APIs and exposes it via REST endpoints. It is built to demonstrate clean backend architecture, API integration, ETL pipelines, and containerized deployment.

🚀 Features
Fetches crypto market data from CoinGecko (free, no API key)
Optional support for CoinPaprika (free API key required)
ETL pipeline to ingest and store data in PostgreSQL
REST API built with FastAPI
Docker & Docker Compose for local setup
Automated tests using Pytest
🛠 Tech Stack
Python 3.11
FastAPI
PostgreSQL
SQLAlchemy
Docker & Docker Compose
Pytest

⚙️ Environment Variables
Create a .env file in the root directory:

DATABASE_URL=postgresql://etl:etl@db:5432/etl
COINPAPRIKA_API_KEY=your_free_api_key_here   # optional

Run the Project
docker compose up --build
API will be available at:
http://localhost:8000
API Endpoints

GET /health → Health check

GET /data → Crypto market data

Run:
docker compose up --build

🧪 Run Tests
docker compose exec api pytest -v

Backend Structure
backend-etl/
│
├── api/
│   ├── main.py
│   └── routes.py
│
├── ingestion/
│   ├── api_source.py
│   ├── csv_source.py
│   ├── third_source.py
│   └── orchestrator.py
│
├── services/
│   ├── etl_service.py
│   ├── checkpoint_service.py
│   └── stats_service.py
│
├── schemas/
│   ├── raw_schema.py
│   └── normalized_schema.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   └── models.py
│
├── tests/
│   ├── test_etl.py
│   ├── test_api.py
│   └── test_failure.py
│
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── requirements.txt
├── .env.example
└── README.md


