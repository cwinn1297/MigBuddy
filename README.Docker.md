# Docker Setup for MigBuddy

This project is containerized using Docker and Docker Compose with PostgreSQL as the database. **PostgreSQL is required for both development and production - SQLite is not supported.**

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. **Build and start the containers:**
   ```bash
   docker-compose up --build
   ```

2. **Create a superuser (in a new terminal):**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

3. **Access the application:**
   - Web application: http://localhost:8000
   - Admin panel: http://localhost:8000/admin
   - PostgreSQL: localhost:5432

## Environment Variables

The application uses the following environment variables (set in `docker-compose.yml`):

- `DB_HOST`: PostgreSQL host (default: `db`)
- `DB_NAME`: Database name (default: `migbuddy`)
- `DB_USER`: Database user (default: `migbuddy`)
- `DB_PASSWORD`: Database password (default: `migbuddy`)
- `DB_PORT`: Database port (default: `5432`)
- `DEBUG`: Debug mode (default: `True`)
- `SECRET_KEY`: Django secret key (optional, has default)

## Database

The PostgreSQL database is automatically created when the containers start. Data is persisted in a Docker volume named `postgres_data`.

## Running Migrations

Migrations run automatically when the container starts. To run manually:

```bash
docker-compose exec web python manage.py migrate
```

## Collecting Static Files

Static files are collected during the Docker build. To collect manually:

```bash
docker-compose exec web python manage.py collectstatic
```

## Stopping the Containers

```bash
docker-compose down
```

To also remove the database volume:

```bash
docker-compose down -v
```

## Development

For development with hot-reload, the code is mounted as a volume, so changes to Python files will be reflected immediately (you may need to restart the container for some changes).

## Production Considerations

For production deployment, you should:

1. Set `DEBUG=False`
2. Set a strong `SECRET_KEY`
3. Configure proper `ALLOWED_HOSTS`
4. Use a production WSGI server (e.g., Gunicorn) instead of `runserver`
5. Set up proper reverse proxy (e.g., Nginx)
6. Use environment variables or secrets management for sensitive data

