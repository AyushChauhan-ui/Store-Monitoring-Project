# Store-Monitoring-Project

This is a Django-based backend API project for monitoring the online status of restaurants and generating reports about their uptime and downtime.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Data Ingestion](#data-ingestion)
- [Report Generation](#report-generation)
- [Contributing](#contributing)
- [License](#license)

## Description

The Store Monitoring project provides a set of backend APIs to monitor the online status of restaurants during their business hours. It ingests data from CSV files containing store status, business hours, and timezones. The system generates reports about uptime and downtime for a specified time period, providing valuable insights for restaurant owners.

## Features

- Data ingestion from CSV files.
- Calculation of store uptime and downtime based on business hours.
- Asynchronous report generation.
- API endpoints for triggering report generation and retrieving report status.

## Requirements

- Python 3.x
- Django 4.x
- MySQL (or any other supported database)
- Additional Python packages (install using `pip install -r requirements.txt`)

## Installation

1. Clone this repository to your local machine.
2. You can also create your own project using commands
  django-admin startproject store_monitoring_project
  cd store_monitoring_project
  python manage.py startapp store_monitoring_app
4. Create and activate a virtual environment (optional but recommended).
5. Install the required Python packages using `pip install -r requirements.txt`.
6. Configure the database settings in `store_monitoring_project/settings.py`.

## Usage

1. Run database migrations using `python manage.py migrate`.
2. Ingest data from CSV files using `python manage.py ingest_data` (custom command for data ingestion).
3. Start the development server using `python manage.py runserver`.

## API Endpoints

- `/api/trigger_report`: Triggers the generation of a report. Returns a report ID.
- `/api/get_report`: Retrieves the status of a generated report or the complete report data.

## Data Ingestion

The data ingestion process reads CSV files containing store status, business hours, and timezones. The data is populated into the database tables `StoreStatus`, `BusinessHours`, and `StoreTimezone`.

## Report Generation

Reports are generated based on real-time data from the database. The system calculates store uptime and downtime within specified time intervals, considering business hours and timezones.
