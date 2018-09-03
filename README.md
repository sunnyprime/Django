# Django
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.


# Virtual Environment create on django

1. Download and install [Anaconda](https://www.anaconda.com/download/) .

### 2. To create django environment 

```conda create --name DjangoTest```


### 2.	To check Environment:

```conda info --envs```

### 3.	To activate Environment:
```activate MyDjangoEnv```

### 4.	To deactivate Environment:
```deactivate MyDjangoEnv```

### 5.	To install the Django in conda env after activating the environment:
```conda install django```

### 6.	To create project [>django-admin: this command check weather it install or not]:

```django-admin startproject first_project```


### 7.	To run the server
```python manage.py runserver```

### 8.	To create a simple application:
```python manage.py startapp first_app```
