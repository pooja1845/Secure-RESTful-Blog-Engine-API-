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

1. **User Authentication**: Secure user registration and login endpoints. Password hashing using `bcrypt` and session management via JWT tokens.
2. **Post CRUD Operations**: Create, read, update, and delete endpoints for blog posts.
3. **Protected Routes**: Middleware dependencies ensure that only logged-in users can create or delete posts.
4. **Automatic API Docs**: Interactive documentation generated automatically via Swagger UI and ReDoc.
5. **Database Session Management**: Dependable yield-based session connection lifecycle to prevent connection leaks.

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
