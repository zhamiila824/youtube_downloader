# youtube_downloader

# Installation and run
From you command line:
$ git clone https://github.com/jamilya824/youtube_downloader.git
$ virtualenv venv -p python3
$ source venv/bin/activate
$ cd youtube_downloader
$ pip install -r requirements.txt
$ python manage.py runserver

Before running serever:

1) create .env file with:

  SECRET_KEY='your-secret-key'

2) make migrations:
  
  $ python manage.py makemigrations
  
  $ python manage.py migrate
  
  $ python manage.py sqlmigrate downloader 0001

3) create superuser(to see admin page):
  
  $ python manage.py createsuperuser
