# Secure RESTful Blog Engine API

A high-performance backend REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. This project features user account management, secure JWT-based authentication, and a complete CRUD system for publishing and managing blog posts.

---

## 📸 Swagger UI Documentation

Once the server is running, visit the interactive documentation at `http://localhost:8000/docs`.

<!-- Place your Swagger UI screenshot at assets/swagger_ui.png to show it on GitHub -->
![Swagger UI API Documentation](assets/swagger_ui.png)

---

## 🛠️ Tech Stack

- **Framework**: FastAPI (Asynchronous Python Web Framework)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Security**: OAuth2 with JWT (JSON Web Tokens), Bcrypt Password Hashing (`passlib`)
- **Validation**: Pydantic v2
- **Server**: Uvicorn

---

## 🚀 Key Features

1. **User Registration & Hashed Passwords**: Secure user registration utilizing the `bcrypt` hashing algorithm to encrypt clear-text passwords before storing them in the database.
2. **JWT Authentication & Session Management**: Issues secure JSON Web Tokens (JWT) upon successful credentials validation, enabling stateless, token-based authorization.
3. **Authentication-Guarded Routes**: Specific API endpoints require user authentication:
   - **Protected Endpoints**: Creating a post (`POST /posts/`) and deleting a post (`DELETE /posts/{id}`) require a valid JWT Bearer token.
   - **Public Endpoints**: Anyone can list posts (`GET /posts/`) or view a specific post (`GET /posts/{id}`).
4. **Post CRUD Operations**: Supports complete creation, reading, updating, and deletion operations for user posts.
5. **Interactive Swagger UI**: Automatic, interactive documentation for testing endpoints.
6. **Database Session Lifecycle Management**: Implements yielding dependencies (`get_db`) to automatically handle opening and closing database connections cleanly.

---

## 📂 Project Structure

```text
├── app/
│   ├── routers/
│   │   ├── auth.py          # User authentication endpoints (/login)
│   │   ├── post.py          # CRUD endpoints for posts (/posts)
│   │   └── user.py          # User registration & profile endpoints (/users)
│   ├── database.py          # PostgreSQL engine and session config
│   ├── main.py              # Application entrypoint and router registration
│   ├── models.py            # SQLAlchemy database models (User, Post)
│   ├── oauth2.py            # JWT creation, decoding, and route guards
│   ├── schemas.py           # Pydantic schemas for data validation
│   └── utils.py             # Password hashing utility functions
├── .gitignore               # Configured to exclude virtualenvs and build files
├── requirements.txt         # Project dependencies list
└── README.md                # Project documentation
```

---

## 💻 Local Setup & Installation

### Prerequisite: Database Setup
Make sure you have a **PostgreSQL** server running locally and create a database named `postgres`. 
Modify the database URL inside `app/database.py` with your credentials:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@localhost/<database_name>"
```

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd <project-folder-name>
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the local development server**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API & Interactive Docs**:
   - Welcome Endpoint: `http://127.0.0.1:8000/`
   - **Swagger UI Interactive Docs**: `http://127.0.0.1:8000/docs`
   - ReDoc Alternative Docs: `http://127.0.0.1:8000/redoc`
