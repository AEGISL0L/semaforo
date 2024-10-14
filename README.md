# Traffic Light Management System

## Project Overview

This project is a web-based application for managing traffic lights using the Flask framework. The application allows users to view and update the states of multiple traffic lights. Each traffic light can be in one of three states: red, yellow, or green. The application uses SQLite as the database to store the traffic light data and Bootstrap for the frontend styling.

## Project Structure

The project is organized into the following main components:

- **app.py**: The main application file that sets up the Flask app, configures the database, and defines the routes for viewing and updating traffic lights.
- **models.py**: Contains the data model for the traffic lights, defining the `Semaforo` class with fields for `id`, `nombre`, and `estado`.
- **templates/**: Contains HTML templates for rendering the web pages. Includes `base.html` for the base layout, `index.html` for displaying the list of traffic lights, and `update.html` for updating a traffic light's state.
- **static/css/**: Contains custom CSS styles for the application.
- **traffic_lights.db**: The SQLite database file that stores the traffic light data.

## Application Logic

1. **Data Model**: The `Semaforo` class in `models.py` defines the structure of the traffic light data, with fields for `id`, `nombre`, and `estado`.

2. **Database Initialization**: The database is initialized using SQLAlchemy, and initial data is added through a Python interactive session.

3. **Routes and Views**:
   - The main route `'/'` displays a list of all traffic lights and their current states.
   - The route `'/semaforo/<int:id>'` displays the details of a specific traffic light.
   - The route `'/update/<int:id>'` allows users to update the state of a specific traffic light.

4. **Frontend**: The application uses Bootstrap for styling. The `index.html` template displays the list of traffic lights in a table, and the `update.html` template provides a form for updating a traffic light's state.

## Running the Application

To run the application, execute the following command in the terminal:

