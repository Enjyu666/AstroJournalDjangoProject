# 🔭 AstroJournal

AstroJournal is a Django web application for keeping a personal astronomy journal.
Users can manage celestial objects, record observations, track the equipment used,
and browse their observation history.

## ✨ Features

- Create, view, edit, and delete celestial objects.
- Manage astronomy equipment.
- Record observations of celestial objects.
- Associate equipment with observations.
- Rate observations and add notes and images.
- Filter objects and equipment by type and observations by celestial object.
- Browse observation entries and images.

## 🚀 Technologies

- Python
- Django
- PostgreSQL
- HTML and CSS

## 🌌 Requirements

- Python
- PostgreSQL
- pip

## 💫 Installation and Setup

### 1. Clone the repository

Clone [this repository](https://github.com/Enjyu666/AstroJournalDjangoProject) from GitHub and open the project directory containing `manage.py`.

### 2. Create and activate a virtual environment

Create a virtual environment:

```bash
python -m venv .venv
```

On Windows, activate it with:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```


### 4. Configure PostgreSQL

Install PostgreSQL and ensure the PostgreSQL server is running.

Create a database and a PostgreSQL user with permission to access it.

By default, the project uses the following database settings:

- Database name: `astro_journal`
- Username: `postgres`
- Password: `postgres`
- Host: `127.0.0.1`
- Port: `5432`

If your PostgreSQL setup uses different values, configure the following environment variables before running the application:

- `DB_NAME` — database name
- `DB_USER` — PostgreSQL username
- `DB_PASSWORD` — PostgreSQL password
- `DB_HOST` — database host
- `DB_PORT` — database port

If an environment variable is not set, the project uses its corresponding default value.

The database and PostgreSQL user must already exist, and the user must have permission to access the database.


### 5. Apply database migrations

Run:

```bash
python manage.py migrate
```

This creates the database tables required by the application.

### 6. Start the development server

```bash
python manage.py runserver
```

Open the local development address shown in the terminal in your browser.

## 📜 Notes

- The PostgreSQL database must be created locally before running migrations.
- The project does not include pre-populated application data. Create celestial objects, equipment, and observations through the application's interface.
- Uploaded images are stored locally according to the Django media settings.
