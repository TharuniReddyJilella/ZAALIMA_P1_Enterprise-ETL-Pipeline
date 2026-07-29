# Enterprise ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that collects data from external REST APIs, processes it into a consistent format, and prepares it for loading into a database.

This project is being developed to learn production-level Python programming, API integration, data transformation, and ETL architecture.

---

## Project Goal

Many companies use different services such as Stripe, Salesforce, or Zendesk. Since each service provides data in different formats, it becomes difficult to analyze everything together.

The goal of this project is to build a modular ETL pipeline that:

- Extracts data from REST APIs
- Cleans and validates the data
- Transforms different API responses into a common format
- Loads processed data into a database
- Maintains logs for debugging and monitoring

---

## Features

- Modular project architecture
- REST API integration
- Retry mechanism for failed API requests
- Data validation using Pydantic
- Data transformation using Pandas/Polars
- Centralized logging
- Environment variable management
- Database-ready architecture
- Unit testing support

---

## Project Structure

```
app/
│
├── api/
├── config/
├── database/
├── extract/
├── load/
├── logger/
├── models/
├── transform/
└── utils/

data/
logs/
tests/

main.py
requirements.txt
```

---

## Technologies Used

- Python 3.11+
- Requests
- Tenacity
- Pydantic
- Pandas
- Polars
- SQLAlchemy
- PostgreSQL
- Pytest
- Git & GitHub

---

## Current Progress

- ✅ Project structure created
- ✅ Configuration module
- ✅ API client
- ✅ Logging module
- ✅ Data extraction module
- ✅ Database module
- ✅ Utility functions
- ✅ Test folder

The remaining ETL pipeline will be developed step by step.

---

## Learning Objectives

This project is helping me learn:

- Production-level Python programming
- API integration
- ETL pipeline development
- Data validation
- Data transformation
- Database interaction
- Clean project architecture
- Git workflow

---

## Future Enhancements

- PostgreSQL data loading
- Incremental data synchronization
- Apache Airflow scheduling
- Docker containerization
- AWS S3 storage
- Monitoring and alerting

---

## Author

Tharuni

Learning Python Backend Development and Data Engineering.