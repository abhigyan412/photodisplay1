# Django Image Upload and Reel Display

## Overview

This Django project allows users to upload images and view them as a reel-style slideshow on a webpage. It demonstrates Django’s model-view-template structure and basic file handling.

## Features

- Upload images through a form.
- Display uploaded images in a carousel or reel format.



## Technologies Used
- Python 3.7+
- Django 4.0+
- Pillow (for image handling


## Installation

1. **Clone the repository:**

   ```bash
 git clone <repository-url>
 cd django-image-reel

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
3. **Install required packages:**

   ```bash
   pip install -r requirements.txt
4. **Apply migrations:**

   ```bash
   python manage.py migrate
 5. **Create Superuser (Optional):**
     ```bash
   python manage.py createsuperuser
 6. **Run the Server:** 
     ```bash
   python manage.py runserver
## Usage
- Navigate to http://127.0.0.1:8000/upload/ to upload an image.
- Go to http://127.0.0.1:8000/view/ to see the reel of uploaded images.



    
   
