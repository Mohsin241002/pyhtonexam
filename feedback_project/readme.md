# Django Feedback Application

This is a simple Django web application that allows users to submit feedback along with their credentials through a form. The application includes basic validation and displays a thank you message upon successful submission.

## Features

- User-friendly feedback form
- Fields for user name, email, password, confirm password, phone number, and feedback message
- Validation checks for matching passwords and valid phone numbers
- Thank you message displayed after form submission
- No database storage required for feedback

## Prerequisites

- Python 3.x
- Django 3.x or higher

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd django-feedback-app

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


pip install django

django-admin startproject feedback_project
cd feedback_project
django-admin startapp feedback

Set up the application:

Add the feedback app to the INSTALLED_APPS list in settings.py:

INSTALLED_APPS = [
    ...
    'feedback',
]

Create the templates folder:

Inside the feedback app directory, create the following structure:
feedback/
    ├── templates/
    │   └── feedback/
    │       └── feedback_form.html

Create the form:

In forms.py, define the feedback form:
Set up URLs:

In urls.py of the feedback app, define the URL

python manage.py runserver