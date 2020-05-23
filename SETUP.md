# How to set up this repository (Debug Mode)


* Clone this repository.

```bash
git clone https://github.com/MagnumDingusEdu/django-templating-boilerplate
```


* Set up your virtual environment

```bash
# Generate the neessary files
python -m venv env
OR
virtualenv env


# Activate the virtual environment
source env/bin/activate


# Install required packages
pip install --upgrade pip && pip install wheel
pip install -r src/requirements.txt
```

* Set up environment variables

```bash
# Copy the environment variable file
cp src/.env.debug src/.env


# Generate a secure secret key using the uuid module
sed "s/YOUR_SECRET_KEY/$( python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])')/" src/.env -i


# Set the environment variables in your terminal sesssion
while read line; do export $line; done < src/.env
```
* Set up your project

```bash

# Change to the ./src directory
cd ./src
```
* Generate and populate database

```bash
# To ensure changes in models.py are reflected
python manage.py makemigrations

# Populate the database tables
python manage.py migrate
```

* Run the debug server

```bash
python manage.py runserver
```

The django  development server will run at the default port 8000. Open http://localhost:8000 to view it in the browser.