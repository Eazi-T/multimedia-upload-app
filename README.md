# Django Multimedia Upload Site

This project is a simple Django-based web application that allows users to upload media files (e.g. images) and stores the file information in a PostgreSQL database.

---

## 📁 Project Structure

- `myproject/`
  - `myapp/`  
    - `migrations/`
    - `models.py`
    - `views.py`
    - `urls.py`
    - `forms.py`
  - `manage.py`
  - `settings.py`
  - `urls.py`
  - `templates/`
    - `upload.html`
  - `media/` (directory to store uploaded media)

---


---

## 🚀 How to Run the Project

1. Unzip the project folder into your desired working directory.

2. Open a terminal or command prompt and navigate to the project folder:
   ```bash
   cd multimedia_project
   
3. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   
4. Create a PostgreSQL database named multimedia_db. 

5. Open multimedia/settings.py and configure the database settings

6. Run database migrations:
   ```bash
    python manage.py makemigrations
    python manage.py migrate

7. Start the development server:
   ```bash
   python manage.py runserver


8. Open your browser and go to http://127.0.0.1:8000/ to use the app.