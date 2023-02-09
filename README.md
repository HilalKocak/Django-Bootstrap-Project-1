# This project is corporate website with Django

## Static Corporate Website Project with FAKE_DB
 - The goal of the project is to develop a Django project with more than one module (App).
 - Understanding Django Template Language(DTL)
 - Working with static files
 - Using the feature with DTL extends
 - Creating modular HTML structure with DTL include
 - Creating Our Own Context Processor and Sending Data to Project
 - Understanding URL structure
 - Working with SLUG
 - Creating multiple detail pages and product pages with Fake Data without using DB infrastructure

### Project Structure
```
.
├── README.md
├── db.sqlite3
├── proje1
│   ├── __init__.py
│   ├── asgi.py
│   ├── project_context_processors.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── page
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── fake_db
│   │   └── pages.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── page
│   │       ├── components
│   │       │   ├── hero_component.html
│   │       │   └── carousel.html
│   │       ├── deleted
│   │       │   ├── about_us.html
│   │       │   ├── contact_us.html
│   │       │   └── vision.html
│   │       ├── home_page.html
│   │       └── page_detail.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── product
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── fake_db
│   │   └── products.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── product
│   │       ├── components
│   │       │   └── card.html
│   │       ├── product_detail.html
│   │       └── products.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── static_files
│   ├── css
│   │   └── bootstrap.min.css
│   └── js
│       └── bootstrap.bundle.min.js
├── templates
│   └── core
│       ├── base.html
│       ├── footer.html
│       ├── navbar.html
│       └── projects.html
```
## Requirements
Python 3.11.0 

## You can install packages with
pip install -r requirements.txt

## Creating superuser
python manage.py createsuperuser

NOTE: The password does not appear on the screen while being entered. Please ensure that you enter your password correctly.

## You can run the project with
python manage.py runserver

