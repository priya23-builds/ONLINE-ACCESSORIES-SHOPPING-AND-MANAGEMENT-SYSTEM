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

These are preserved only as a reference to the supplied academic code. Change them before any real deployment.

## Important notes before GitHub publication

1. The original source contains hard-coded database credentials and a Flask secret key. This repository moves configuration to environment variables and ignores `.env`.
2. The original login SQL contained a malformed condition. This repository uses `WHERE email = %s` so the route is syntactically correct.
3. The original code referenced `userdashboard` but did not define that route. This repository adds the missing route and template placeholder.
4. The original code returned strings such as `"my_orders.html"`; this repository renders the matching templates.
5. Passwords are still stored as plain text because that is what the supplied student code does. Hash passwords before any real-world deployment.
6. The supplied project report describes a broader e-commerce scope than the backend code currently implements. The repository therefore does not claim that payment, wishlist, recommendations, delivery integration, or full CRUD are implemented here.

## What to add when available

Replace the placeholder templates and empty static folders with the student's actual HTML/CSS/images. Also replace the starter schema with the exact database export if the student has one.
