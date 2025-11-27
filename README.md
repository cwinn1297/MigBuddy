# MigBuddy

**Immigration Made Simple** – A Django web application designed to help users manage their immigration applications and forms.

## 🚀 Features

- **User Authentication & Registration**: Secure user accounts with custom user model
- **Dashboard**: Personalized dashboard to track immigration applications
- **PDF Form Management**: View and analyze USCIS PDF forms (e.g., I-129F)
- **Form Field Extraction**: Automatically extract fillable fields from PDF forms using PyPDF2
- **PostgreSQL Database**: Robust database backend for production use
- **Docker Support**: Easy deployment with Docker and Docker Compose
- **Responsive UI**: Modern, Bootstrap-based interface

## 🛠️ Tech Stack

- **Backend**: Django 5.2.8
- **Database**: PostgreSQL 15
- **PDF Processing**: pypdf
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Containerization**: Docker, Docker Compose
- **Python**: 3.10+

## 📋 Prerequisites

- Python 3.10 or higher
- PostgreSQL (for local development) OR Docker & Docker Compose
- pip (Python package manager)

## 🚀 Quick Start with Docker (Recommended)

The easiest way to get started is using Docker:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd MigBuddy
   ```

2. **Build and start the containers:**
   ```bash
   docker-compose up --build
   ```

3. **Create a superuser:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. **Access the application:**
   - Web application: http://localhost:8000
   - Admin panel: http://localhost:8000/admin
   - PostgreSQL: localhost:5432

For more Docker details, see [README.Docker.md](README.Docker.md)

## 💻 Local Development Setup

If you prefer to run locally without Docker:

1. **Install PostgreSQL:**
   - Install PostgreSQL 15+ on your system
   - Create a database named `migbuddy`

2. **Clone and navigate to the project:**
   ```bash
   git clone <repository-url>
   cd MigBuddy
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables:**
   Set the following environment variables or update `settings.py`:
   ```bash
   export DB_HOST=localhost
   export DB_NAME=migbuddy
   export DB_USER=your_postgres_user
   export DB_PASSWORD=your_postgres_password
   export DB_PORT=5432
   export SECRET_KEY=your-secret-key-here
   export DEBUG=True
   ```

6. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

9. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

10. **Access the application:**
    - Web application: http://localhost:8000
    - Admin panel: http://localhost:8000/admin

## 📁 Project Structure

```
MigBuddy/
├── accounts/          # User authentication and registration
│   ├── models.py      # Custom User model
│   ├── views.py       # Registration and account views
│   ├── forms.py       # User registration form
│   └── templates/     # Account templates
├── applications/      # Immigration form management
│   ├── views.py       # PDF form processing views
│   ├── static/forms/  # PDF form files
│   └── templates/     # Form templates
├── core/              # Core application functionality
│   ├── views.py       # Landing, login, home views
│   └── templates/     # Base templates
├── MigBuddy/          # Django project settings
│   ├── settings.py    # Application settings
│   ├── urls.py        # Main URL configuration
│   └── wsgi.py        # WSGI configuration
├── docker-compose.yml # Docker Compose configuration
├── Dockerfile         # Docker image configuration
├── requirements.txt   # Python dependencies
└── manage.py          # Django management script
```

## 🔧 Configuration

### Environment Variables

The application uses the following environment variables:

- `DB_HOST`: PostgreSQL host (default: `localhost` or `db` in Docker)
- `DB_NAME`: Database name (default: `migbuddy`)
- `DB_USER`: Database user (default: `migbuddy`)
- `DB_PASSWORD`: Database password (default: `migbuddy`)
- `DB_PORT`: Database port (default: `5432`)
- `DEBUG`: Debug mode (default: `True`)
- `SECRET_KEY`: Django secret key (required for production)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

### Database

**Important**: This application uses PostgreSQL exclusively. SQLite is not supported.

The database configuration is in `MigBuddy/settings.py` and automatically uses PostgreSQL when environment variables are set.

## 📖 Usage

### User Registration

1. Navigate to http://localhost:8000/accounts/register/
2. Fill in the registration form
3. You'll be automatically logged in after registration

### Viewing Forms

1. Navigate to http://localhost:8000/applications/
2. Browse available PDF forms
3. Click "Open Form" to view form fields extracted from PDFs

### Dashboard

1. After logging in, access your dashboard at http://localhost:8000/home/
2. View your application statistics
3. Start new applications from the dashboard

## 🧪 Running Tests

```bash
python manage.py test
```

Or with Docker:

```bash
docker-compose exec web python manage.py test
```

## 🐳 Docker Commands

```bash
# Start containers
docker-compose up

# Start in background
docker-compose up -d

# Stop containers
docker-compose down

# Stop and remove volumes
docker-compose down -v

# View logs
docker-compose logs -f web

# Run management commands
docker-compose exec web python manage.py <command>

# Access Django shell
docker-compose exec web python manage.py shell
```

## 🚀 Production Deployment

For production deployment:

1. Set `DEBUG=False` in environment variables
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS` with your domain
4. Use a production WSGI server (e.g., Gunicorn)
5. Set up a reverse proxy (e.g., Nginx)
6. Use environment variables or secrets management for sensitive data
7. Enable HTTPS/SSL
8. Set up proper database backups

Example with Gunicorn:

```bash
pip install gunicorn
gunicorn MigBuddy.wsgi:application --bind 0.0.0.0:8000
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Django community
- USCIS for providing immigration forms
- Bootstrap for the UI framework

## 📞 Support

For support, please open an issue in the GitHub repository.

---

**Note**: This application is for educational and assistance purposes. Always verify information with official immigration authorities.

