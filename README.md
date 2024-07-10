# Project Planning Tool
This is tool for project plannig which consist of API's regarding it built in jango-rest-framework

## Installation
```
install VSCode
install extension: SQLite Viewer by Florian Klampfer
install requirements.txt in root folder ```pip install requirements.txt```
install Postman for testing api's

Before running the application, run following commands
going to the root folder
>>>python manage.py makemigrations
>>>python mangae.py migrate
>>>python manage.py runserver
```

## Description
This is a Django project 
``` projectmanagement ```.
It has 3 different apps in it which point to three different api's requirement i.e.,
``` User, Team, ProjectBoard ```

## API Reference

-- User's 
   - http://localhost:8000/users/             for get all
   - http://localhost:8000/users/<int:pk>/    for specified id results  

-- Team's 
   - http://localhost:8000/teams/
   - http://localhost:8000/teams/<int:pk>/    for specified id results  

-- Project Board's 
   - http://localhost:8000/project/
   - http://localhost:8000/project/<int:pk>/    for specified id results  
   
## some more Information

for get, post, put and patch request the views.py files are there which will tell you what is required in each kind of request
