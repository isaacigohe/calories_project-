# Calorie Counter Web Application

A simple and efficient web application built with Django to track daily calorie consumption.

## Features
- **Add Food Items**: Easily add food names and their calorie counts.
- **View Log**: See a list of all food items consumed during the day.
- **Total Calories**: Automatically calculates and displays the total calories for the day.
- **Remove Items**: Delete individual food items from your log.
- **Reset Day**: Clear the entire log to start fresh for a new day.
- **Responsive Design**: Styled with Tailwind CSS for a modern look on all devices.

## Technical Stack
- **Backend**: Python 3.x, Django 3.2
- **Database**: PostgreSQL
- **Frontend**: HTML5, Tailwind CSS (via CDN)
- **Deployment**: Ready for platforms like Render or Heroku.

## Setup Instructions

### Prerequisites
- Python 3.x
- PostgreSQL installed and running

### Installation
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd calorie_counter_project
   ```

2. **Install dependencies**:
   ```bash
   pip install django==3.2.25 psycopg2-binary
   ```

3. **Database Configuration**:
   - Create a PostgreSQL database named `calorie_db`.
   - Update `calorie_project/settings.py` with your database credentials.

4. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000/`.

## Deployment (e.g., on Render)
1. Connect your GitHub repository to Render.
2. Select "Web Service".
3. Use the following build command:
   ```bash
   pip install -r requirements.txt && python manage.py migrate
   ```
4. Use the following start command:
   ```bash
   gunicorn calorie_project.wsgi
   ```
5. Add environment variables for `DATABASE_URL` and `SECRET_KEY`.

## Project Structure
- `calorie_project/`: Main project configuration.
- `calorie_tracker/`: App containing logic for calorie tracking.
  - `models.py`: Defines the `Food` model.
  - `views.py`: Handles CRUD operations and calorie calculations.
  - `templates/`: HTML templates with Tailwind CSS.

## License
MIT License
