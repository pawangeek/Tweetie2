# Tweetie2

## *Introduction*

### Summary

> - Project
>   - Fetch you Home Timeline Tweets from Twitter Account
>   - Twitter Social Login
>   - Able to analyze the tweets having links in the text area and user who share maximum number of tweets having links
>  </br>
>
> - BACKEND
>   - Using Django for storing sessions and doing analysis part
>   - Authlib for Twitter oauth authorization
>  <br/>
>
> - FRONTEND
>   - Bootstrap, Jquery for some styling

### Requirements

> - BACKEND
>   - [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
>   - [Django 3.1](https://docs.djangoproject.com/en/3.1/releases/3.0/)
>   - [Authlib 0.14.3](https://authlib.org/)
>  <br/>
> - FRONTEND
>   - [JQuery](https://code.jquery.com/)
>   - [Bootstrap 4.5](https://getbootstrap.com/docs/4.5/getting-started/download/)
>  <br/>
> - Database
>   - [SQLite](https://www.sqlite.org/index.html)
> 	<br/>
> - Deploy
>  	- [Pythonanywhere](https://www.pythonanywhere.com/)
## Project Structure

```bash

.
├── README.txt
├── db.sqlite3
├── manage.py
├── requirements.txt
├── tweetie
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations *
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__*
│   ├── models.py
│   ├── static
│   │   └── imgs
│   │       ├── icon.ico
│   │       └── twitter.png
│   ├── templates
│   │   └── tweetie
│   │       ├── about.html
│   │       ├── analyze.html
│   │       ├── base.html
│   │       ├── home.html
│   │       └── tweet.html
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
└── vouch
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## How to Use


* **Step 1: Clone the Project**
```python3
git clone https://github.com/pawangeek/Tweetie2
cd Tweetie2
```

* **Step 2: Create a virtual environment**
```Python
# For mac and linux users
python3 -m venv env
source env/bin/activate

# For window users
py -m venv env
.\env\Scripts\activate
```

* **Step 3: Load all dependencies from requirements.txt**
```python
pip install -r requirement.txt
```

* **Step 4: Migrate Tables to Database**
```
python manage.py makemigrations
python manage.py migrate
```

* **Step 5: Go to [twitter developer](https://developer.twitter.com/en) console**
```python
Add callback url : http://127.0.0.1:8000/auth
```

* **Step 6: Get the twitter_client_id and twitter_client_secret from that twitter dev console**
```python
# Add them in setting.py in AUTHLIB_OAUTH_CLIENTS
client_id = ''
client_secret = ''
```

* **Step 7 Boom you will see you this app running on localhost.**
```python
python manage.py runserver
```
