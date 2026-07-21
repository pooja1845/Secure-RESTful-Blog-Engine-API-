# ✍️ Secure RESTful Blog Engine API

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" />
  <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens" alt="JWT" />
  <img src="https://img.shields.io/badge/-Swagger-%23C0E800?style=for-the-badge&logo=swagger&logoColor=black" alt="Swagger" />
</p>

A production-grade, secure blogging engine API built with the asynchronous power of **FastAPI**, backed by a relational **PostgreSQL** database and mapped with **SQLAlchemy ORM**. This API features secure user flows with **JWT token authentication** and cryptographic **bcrypt password hashing**.

---

## ⚡ Quick Showcase (Interactive Swagger UI Docs)

<img width="1118" height="802" alt="Screenshot 2026-07-21 220322" src="https://github.com/user-attachments/assets/8f881d76-2d26-4671-a515-a3eb4feab788" />


---

## 🎯 Core Features

* 🛡️ **Cryptographic Security**: Clear-text passwords are never stored. Passwords are securely encrypted using `bcrypt` via the `passlib` context before insertion.
* 🔑 **Stateless Auth (JWT)**: Secure user sign-up and authentication flows returning standards-compliant JSON Web Tokens (JWT) for subsequent authorized access.
* 🚧 **Route Guards**:
  * 🔓 **Public Access**: Anyone can fetch all posts (`GET /posts/`) or view a single post by ID (`GET /posts/{id}`).
  * 🔒 **Protected Access**: Creating a post (`POST /posts/`) and deleting a post (`DELETE /posts/{id}`) require a valid JWT token in the Authorization Header.
* 💾 **SQLAlchemy Database Engine**: Automatic connection pool management and transaction lifecycles wrapped in FastAPI yielding dependency injection.
* 📝 **Dynamic Validation**: Standardized data serialization and deserialization using Pydantic schemas to validate JSON payloads.

---

## 📂 Architecture Map

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
├── .gitignore               # Excludes virtual environments and build configurations
├── requirements.txt         # Package dependencies list
└── README.md                # Project documentation
```

---

## 🔧 Installation & Setup

### 1. Database Creation
Ensure a **PostgreSQL** database named `postgres` is running. Update your database connection string in `app/database.py`:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@localhost/<database_name>"
```

### 2. Project Boot-up
Execute the following commands in your workspace terminal:

```bash
# Clone the repository
git clone <your-repository-url>
cd <project-folder-name>

# Setup a clean virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate
# Activate environment (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload
```

---

## 🔗 API Endpoint Matrix

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| **POST** | `/login` | Authenticate user & retrieve JWT access token | ❌ No |
| **POST** | `/users/` | Create a new user profile | ❌ No |
| **GET** | `/users/` | Get a list of all registered users | ❌ No |
| **GET** | `/users/{id}` | Retrieve details of a specific user | ❌ No |
| **GET** | `/posts/` | Retrieve a list of all blog posts | ❌ No |
| **POST** | `/posts/` | Publish a new blog post | 🔒 **Yes** |
| **GET** | `/posts/{id}` | Fetch a single blog post details | ❌ No |
| **PUT** | `/posts/{id}` | Update post details | ❌ No |
| **DELETE** | `/posts/{id}` | Remove a post permanently | 🔒 **Yes** |
