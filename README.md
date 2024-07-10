# Project Planning Tool
This is a project planning tool featuring various APIs, developed using Django REST Framework.

## Installation
1. Install VSCode.
2. Add the SQLite Viewer extension by Florian Klampfer.
3. In the root folder, install the required dependencies with:
    ```
    pip install -r requirements.txt
    ```
4. Install Postman for API testing.

Before starting the application, execute the following commands in the root directory:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Description
This Django project, named `projectmanagement`, contains three different apps, each addressing a specific API requirement: `User`, `Team`, and `ProjectBoard`.

## API Reference

### User API
- Retrieve all users: `http://localhost:8000/users/`
- Retrieve user by ID: `http://localhost:8000/users/<int:pk>/`

### Team API
- Retrieve all teams: `http://localhost:8000/teams/`
- Retrieve team by ID: `http://localhost:8000/teams/<int:pk>/`

### Project Board API
- Retrieve all projects: `http://localhost:8000/project/`
- Retrieve project by ID: `http://localhost:8000/project/<int:pk>/`

## Additional Information
To handle GET, POST, PUT, and PATCH requests, refer to the `views.py` files in each app directory. These files provide the necessary details for each type of request.