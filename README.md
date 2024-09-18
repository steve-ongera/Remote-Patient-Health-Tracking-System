# <img height="24" src="https://raw.githubusercontent.com/yezyilomo/django-restql/master/docs/img/icon.svg" /> [  Django RESTQL](https://yezyilomo.github.io/django-restql)

![Build Status](https://github.com/yezyilomo/django-restql/actions/workflows/main.yml/badge.svg?branch=master)
[![Latest Version](https://img.shields.io/pypi/v/django-restql.svg)](https://pypi.org/project/django-restql/) 
[![Python Versions](https://img.shields.io/pypi/pyversions/django-restql.svg)](https://pypi.org/project/django-restql/) 
[![License](https://img.shields.io/pypi/l/django-restql.svg)](https://pypi.org/project/django-restql/)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
[![Downloads](https://pepy.tech/badge/django-restql)](https://pepy.tech/project/django-restql) 
[![Downloads](https://pepy.tech/badge/django-restql/month)](https://pepy.tech/project/django-restql) 
[![Downloads](https://pepy.tech/badge/django-restql/week)](https://pepy.tech/project/django-restql)


# Remote Patient Health Tracking System

## Overview

This project is a remote patient health tracking system built using Django and Django REST Framework. It allows healthcare providers to manage patient records and monitor health metrics such as weight, blood pressure, and heart rate.

## Features

- User registration and authentication
- Patient management (CRUD operations)
- Health metrics tracking (CRUD operations)
- RESTful API for easy data access and manipulation
- Admin interface for managing patients and health metrics

## Technologies Used

- Django
- Django REST Framework
- SQLite (or any other database of your choice)
- HTML/CSS for the frontend (if applicable)

## Installation

1. **Clone the repository:**
   1. Open your terminal.
   2. Run the following commands:
   ```bash
   git clone https://github.com/steve-ongera/remote-patient-health-tracking.git
   cd remote-patient-health-tracking

2. **Create a virtual environment (optional but recommended):**


python -m venv venv

3. **Activate the virtual environment:**

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. **Install the required packages:**

pip install -r requirements.txt

5. **Run migrations:**


python manage.py migrate
6. **Create a superuser (optional, for admin access):**


python manage.py createsuperuser
7. **Run the server:**


python manage.py runserver
Access the application: Open your browser and navigate to http://localhost:8000/admin for the admin interface or http://localhost:8000/api/ for the API.

## API Endpoints
**Patients:**

GET /api/patients/ - List all patients
POST /api/patients/ - Create a new patient
GET /api/patients/<id>/ - Retrieve a specific patient
PUT/PATCH /api/patients/<id>/ - Update a specific patient
DELETE /api/patients/<id>/ - Delete a specific patient

**Health Metrics:**

GET /api/health-metrics/ - List all health metrics
POST /api/health-metrics/ - Create a new health metric
GET /api/health-metrics/<id>/ - Retrieve a specific health metric
PUT/PATCH /api/health-metrics/<id>/ - Update a specific health metric
DELETE /api/health-metrics/<id>/ - Delete a specific health metric
Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries, please contact: 0112284093
gadafisteve001@gmail.com


### Instructions

1. Copy the above content.
2. Create a new file named `README.md` in your project directory.
3. Paste the content into the file and save it.

Feel free to replace any placeholders with your actual information! If you need further modifications, just let me know!


