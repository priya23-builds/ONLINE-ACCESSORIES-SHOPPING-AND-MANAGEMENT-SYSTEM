# Online Accessories Shopping and Management System

A Flask + MySQL academic project for managing an online accessories shop. The project documentation describes an admin module and a user module, with product management, orders, registration/login, and profile-related pages.

## Stack

- Python
- Flask
- Flask-MySQLdb / MySQL
- HTML, CSS and Bootstrap (documented frontend stack)
- Jinja2 templates

## Current repository contents

This repository is intentionally structured from the material supplied for the project:

- `app.py` - cleaned and runnable Flask backend based on the supplied backend code.
- `database/schema.sql` - starter MySQL schema inferred from the backend and project documentation; review it against the student's original database before production use.
- `templates/` - minimal placeholder pages so the routes can render until the student's original HTML files are available.
- `static/` - folders reserved for the documented CSS, JavaScript and image assets.
- `docs/` - notes about what was available and what still needs to be supplied.

The submitted report describes pages for landing, login, registration, admin dashboard, add item, all orders, user dashboard, products, my orders, and my profile. It also states that the backend uses Flask and the data layer uses MySQL. See the project report for the detailed architecture and page descriptions.

## Setup

### 1. Create the database

Install MySQL and run:

```sql
SOURCE database/schema.sql;
```

### 2. Create and activate a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\\Scripts\\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> On some systems, `mysqlclient` requires native MySQL/MariaDB development libraries to be installed first.

### 4. Configure environment variables

Copy `.env.example` to `.env` and update the MySQL values. The application loads this file automatically. Do not commit `.env`.

### 5. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000/`.

## Demo admin credentials from the supplied backend

The source code contains an admin check for:

- Email: `admin@gmail.com`
- Password: `admin@123`
