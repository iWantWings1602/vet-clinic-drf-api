# Vet Clinic DRF API

A clean RESTful API for managing veterinary clinic operations, built using Django REST Framework.

## How to run locally
1. Clone the repository and navigate into it.
2. Create and activate a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file based on `.env.example`.
5. Run migrations: `python manage.py migrate`
6. Seed the database with sample data: `python manage.py seed`
7. Start the server: `python manage.py runserver`

## API Endpoints Table

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | `/api/owners/` | List all owners | Anyone (Read-only) |
| GET | `/api/owners/<id>/` | Detailed owner info | Anyone (Read-only) |
| GET | `/api/pets/` | List all pets (with filters/search) | Anyone (Read-only) |
| POST | `/api/pets/` | Create a new pet entry | Authenticated users |
| PATCH | `/api/pets/<id>/` | Partially update pet data | Object owner only |
| DELETE| `/api/pets/<id>/` | Delete pet record | Object owner only |
| GET | `/api/records/` | List all medical records | Anyone (Read-only) |
| GET | `/api/records/expensive/` | Get records with cost > 3000 UAH | Anyone (Read-only) |
