# Notes App (Django)

A very simple, clean Notes app with full CRUD functionality (create, view, edit, delete).

## Features
- Create, view, edit, and delete notes
- Clean Bootstrap UI
- SQLite database by default

## Project Structure
- `manage.py` — Django management script
- `notes/` — Application with model, forms, views, urls
- `notes_project/` — Django project settings and urls
- `templates/` — HTML templates (base + pages for notes)

## Requirements
- Python 3.9+
- pip

Install project dependencies:

```powershell
pip install -r requirements.txt
```

## Run Locally (Windows PowerShell)
From the project root folder `C:\Users\nitin\CascadeProjects\project1`:

```powershell
# Optional but recommended: create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Make initial migrations and migrate
python manage.py makemigrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

## Usage
- Home page lists all notes
- Click "New Note" to create
- Click a note to view details
- Use Edit/Delete buttons on detail or list items

## Admin (optional)
If you want to use the Django admin:
```powershell
python manage.py createsuperuser
```
Then visit http://127.0.0.1:8000/admin/

## Notes
- This app uses Bootstrap via CDN for styling.
- Default database is SQLite located at `db.sqlite3` in the project root.
