# Vet Clinic DRF API

A clean RESTful API for managing veterinary clinic operations, built using Django REST Framework, JWT authentication, and Docker.

## How to run with Docker (Recommended)
1. Clone the repository and navigate into it.
2. Make sure **Docker Desktop** is running on your machine.
3. Start the multi-container environment (Django + PostgreSQL):
   ```bash
   docker compose up --build
   ```
4. In a new terminal tab, seed the database with sample clinic data:
   ```bash
   docker compose exec web python manage.py seed
   ```
5. Open your browser and navigate to: `http://127.0.0`

## How to run locally (Without Docker)
1. Create and activate a virtual environment: `python -m venv venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file based on `.env.example`.
4. Run migrations: `python manage.py migrate`
5. Seed the database with sample data: `python manage.py seed`
6. Start the development server: `python manage.py runserver`

## How to run tests
To run automatic permission and validation tests, use the following command:
* **Locally:** `python manage.py test clinic`
* **In Docker:** `docker compose exec web python manage.py test clinic`

## API Endpoints Table

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| POST | `/api/token/` | Obtain JWT Access and Refresh tokens (Login) | Anyone |
| POST | `/api/token/refresh/` | Refresh expired Access token | Anyone |
| POST | `/api/token/verify/` | Verify token validity | Anyone |
| GET | `/api/owners/` | List all owners (search available) | Anyone (Read-only) |
| GET | `/api/owners/<id>/` | Detailed owner info | Anyone (Read-only) |
| GET | `/api/pets/` | List all pets (with filters/search/pagination) | Anyone (Read-only) |
| POST | `/api/pets/` | Create a new pet entry | Authenticated users (JWT Bearer) |
| PATCH | `/api/pets/<id>/` | Partially update pet data | Object owner only |
| DELETE| `/api/pets/<id>/` | Delete pet record | Object owner only |
| GET | `/api/records/` | List all medical records | Anyone (Read-only) |
| GET | `/api/records/expensive/` | Get records with cost > 3000 UAH | Anyone (Read-only) |

## Postman Collection
You can find the ready-to-import Postman test collection in the `/postman` directory of this repository.
