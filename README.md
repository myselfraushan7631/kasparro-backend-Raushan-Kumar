## Backend & ETL System

Run:
make up

API:
GET /data
GET /health
GET /stats

Includes:
- Incremental ETL
- API + CSV + Third source
- Dockerized
- Tests

# Backend Structure

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

