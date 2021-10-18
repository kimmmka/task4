## Courses
A simple API for users to view and create various courses

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites
This is a project written using Python, Django and Django Rest Framework

**1.** Clone the repository
https://github.com/kimmmka/task4.git

**2.** Create the virtual enviroment
```sh
 *python3 -m venv venv*

 *source myvenv/bin/activate*
```

**3.** Install the requirements

```sh
*pip install -r requirements.txt* 
```

**4.** Make migrations
```sh
 *python manage.py makemigrations*

 *python manage.py migrate*
```

**5.** Create a new superuser

##### *python manage.py createsuperuser*

**6.** Run the server

```sh 
*python manage.py runserver*
``` 

Run the server and go to: [site](http://127.0.0.1:8000/admin/course)

## Built With

Django - The framework used, Django Rest Framework - The toolkit used to build API, Swagger UI - for API documentation.

## Documentation
[Apiry](https://app.apiary.io/courses28/editor#/)

