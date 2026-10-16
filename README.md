# Vet Clinic DRF API

A professional RESTful API for managing veterinary clinic operations, built using Django REST Framework, JWT authentication, and PostgreSQL 17 inside Docker Compose.

## How to run with Docker (Recommended)
1. Clone the repository and navigate into it.
2. Make sure **Docker Desktop** is running on your machine.
3. Start the multi-container production environment (Django with Gunicorn + PostgreSQL 17):
   ```bash
   docker compose up --build
   ```
4. In a new terminal tab, seed the database with sample clinic data and create a superuser:
   ```bash
   docker compose exec web python manage.py migrate
   ```
   *(Migrations run automatically on startup, but you can trigger them manually if needed)*.
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```
   ```bash
   docker compose exec web python manage.py seed
   ```
5. Open your browser and navigate to the API root: `http://127.0.0`

## How to check Database via psql
To connect to the live PostgreSQL container and verify tables, run:
```bash
docker compose exec db psql -U app_user -d app_db
```
Inside the `psql` console, you can use:
* `\dt` — List all database tables.
* `SELECT * FROM clinic_pet;` — View all pet records.
* `\q` — Exit the console.

## How to run tests
To run automatic permission and validation tests inside the container, use:
```bash
docker compose exec web python manage.py test clinic
```

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

## Postman & HTTP Testing
* The ready-to-import Postman test collection is located in the `/postman` directory.
* For IDE-native testing, you can use the `test_db.http` file inside PyCharm.

