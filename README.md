# Twitter Clone (Django)

A modern, dark-mode Twitter clone built with Django and Bootstrap 5. Users can register, log in, create tweets (with image uploads), edit, and delete their own tweets. The UI is fully responsive and aesthetic, using Bootstrap for a seamless experience.

## Features

- User registration and authentication (open to all)
- Create, edit, and delete tweets
- Upload images with tweets
- Responsive, modern dark mode UI (Bootstrap 5)
- Secure user access (only owners can edit/delete their tweets)

## Local Setup

### Prerequisites

- Python 3.8+
- pip
- (Recommended) Virtual environment tool: `venv` or `virtualenv`

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd "Twitter Clone"
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   cd chaihq
   python manage.py migrate
   ```
5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Visit the app:**
   Open [http://127.0.0.1:8000/tweet/](http://127.0.0.1:8000/tweet/) in your browser.


## Project Structure

- `chaihq/` - Django project root
- `tweet/` - Main app (models, views, forms, templates)
- `templates/` - Shared and registration templates
- `static/` - Static assets

## Author

Vidita Singh

---

Feel free to contribute or raise issues!
