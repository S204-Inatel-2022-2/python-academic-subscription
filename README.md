# Academic Subscription API with Django Rest Framework
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 
- Django
- Django REST Framework

## Installation
It uses [poetry](https://python-poetry.org/) to manage the project. So first make sure that is
installed. Then clone the repo and run:

```bash
$ poetry install
```
This will create a virtualenv and install both project and dev dependencies in it. See the [poetry
documentation](https://python-poetry.org/docs/) to learn how to work within the project.

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application 
using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized 
around _collections_ and _elements_, both of which are resources.


## Use
First, we have to start up Django's development server.
```
python manage.py runserver
```
After that, we can access and interact with the API endpoints.
The API base url is http://127.0.0.1:8000/api/v1/.