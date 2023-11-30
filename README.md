# Newspaper Agency #

 System dedicated to tracking redactors assigned to each newspaper. This system aims
 to provide a comprehensive record of the publishers associated with each newspaper, ensuring seamless monitoring and
 management. 

# Check it out!

https://newspaper-agency-ktto.onrender.com

For login, please, enter this:
```
Username: admin
Password: gRZ8B6qsZezBEiD
```

## How to install

Python 3 must be installed

```
git clone https://github.com/Oxbay/Develop-Newspaper-Agency.git
```

If you don't have **pip** installed  [install it here](https://pip.pypa.io/en/stable/installation/#).

Also, you need make some changes in settings.py

DATABASES must look like this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': dj_database_url.config(
#         default='postgres://twzmhsog:KmAUoAxvsVcSdFuiS6nfA8yoOr1uMS4O@cornelius.db.elephantsql.com/twzmhsog',
#         conn_max_age=600,
#         conn_health_checks=True,
#     )
# }
```
Now you must do all of this commands:

   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py runserver
   ```

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Features

* Authentication functionality for Redactors
* Managing newspapers and topics directly from website interface
* Powerful admin panel for advancing managing

## Demo
![Website interface](demo.png)