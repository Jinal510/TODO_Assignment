
# TODO List Manager

A to-do list application enhances task management by facilitating efficient task writing, organization, and prioritization. It empowers users to manage, prioritize, and set deadlines for tasks, thereby boosting productivity. This repository encompasses all essential files for the todo_drf App, a Django Application incorporating APIs to enable CRUD operations, along with basic HTML/CSS for the client-side (frontend) user interface. Additionally, the application features a User-Authentication system to store user-specific tasks. Refer to the comprehensive README.md documentation for a clearer understanding of the operational architecture and additional features.


## Demo Link

Click here to watch the demo of the project.
https://www.kapwing.com/videos/65cffcf0a5fdac9cf55f0033

## Concepts

API Development

Django Development

CRUD Operations


## Tools & Technologies

Python 3

Django

Django REST Framework

HTML/CSS

Postgresql

GitHub

## Working

1. This is a To Do list application that allows user to manage his/her tasks more efficiently.

2. The App uses Django for back-end support and postgresql database to store the models data.

3. This To Do List application can store multiple users.

4. Its a complete application with an attractive user-interface which allows user to interact with the application in a better way.
## Features

1. User can perform basic CRUD operations , i.e Create | Update | Delete the ToDo list.

2. Users can add new tasks & also delete existing tasks from their respective list.

3. User can mark the task as DONE, once completed, just by selecting done button.
## Installation Guide


To install Python:

[Python website] https://www.python.org/downloads/.

To install django:

```bash
  pip install django
```
To install Django REST Framework:

```bash
  pip install djangorestframework
```

To create a migration file based on any changes detected in the models.

```bash
  python3 manage.py makemigrations
```

This command is used to apply the pending migrations to your database and synchronize the database schema with the changes in your models.

```bash
  python3 manage.py migrate
```

To run the application on local Port 8000:

```bash
  python3 manage.py runserver
```


