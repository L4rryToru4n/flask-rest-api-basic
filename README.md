# Basic Flask REST API


A production-ready REST API built with Python, Flask, Docker, and PostgreSQL—featuring secure authentication, modular design, and containerized deployment.

### Tech Stack
- Python 3.x
- Flask + Flask-Smorest
- Flask-JWT-Extended
- Flask-SQLAlchemy
- PostgreSQL
- Alembic (DB migrations)
- Docker + Docker Compose

### Features
- RESTful API architecture
- Secure user authentication (JWT, refresh tokens, blacklisting)
- Role-based access control (RBAC-ready structure)
- Modular blueprints and input validation
- PostgreSQL with SQLAlchemy ORM
- Alembic-managed database migrations
- Dockerized development & deployment
- Clean error handling and response formatting

### Project Structure
```
/app  
├── resources/           # API route handlers  
├── schemas/             # Marshmallow validation schemas  
├── models/              # SQLAlchemy models  
├── extensions/          # JWT, DB, Marshmallow init  
├── migrations/          # Alembic migrations  
├── config.py            # Environment config  
└── main.py              # Entry point  
```
## Getting Started

## Clone the repository
```
git clone https://github.com/L4rryToru4n/flask-rest-api-basic.git
cd flask-rest-api-basic
```
## Start the app (Docker required)
```
docker-compose up --build
```
API will be available at http://localhost:5000

## Authentication
`/register` - Register new user

`/login` - Obtain access and refresh tokens

`/refresh` - Get new access token

`/logout` - Blacklist refresh token
