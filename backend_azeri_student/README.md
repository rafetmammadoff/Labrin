# Azeri Project #

## Local Setup ##

First you need to install backend_azeri_student module with bellow credentials
```

$ git clone https://bitbucket.org/labclients/backend_azeri_student.git
$ cd backend_azeri_student/
```sh

Create a virtual environment to install dependencies in and activate it:

$ virtualenv  .env
$ source .env/bin/activate

```
## requirements.txt ##

Then install the dependencies:
```
(env)$ pip install -r requirements.txt
```

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.



### --- Superuser ###

Create superusers using the createsuperuser command:
```
#!

$ python manage.py createsuperuser --username=joe --email=joe@example.com
```



### --- Migrate ###

By running **makemigrations**, you are telling Django that you have made some changes to your models (in this case, you have made new ones) and that you had like the changes to be stored as a *migration*.


```
#!

$ python manage.py makemigrations 
```

Now, run **migrate** again to create those model tables in your database:


```
#!

$ python manage.py migrate
```

Run project:
```
$ python manage.py runserver
```
And navigate to http://127.0.0.1:8000/.


### --- Running tests ###

In the terminal, we can run our test:
```
#!
$ python manage.py test <appname>
```



### --- Install dependencies ###

Installing required dependencies on virtual environment:
```
#!
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```
Note:If you run this project in local,you should:
  #### DEBUG=True ####

  in your settings.py(Django) file.

## Get involved! ##
We are happy to receive bug reports, fixes, documentation enhancements, and other improvements.

Please report bugs via the github issue tracker.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

### --- Credits & Helpers ###
1. Extend your RAM by adding a swap file - http://stackoverflow.com/a/18335151/968751
1. Make ffmpeg executable everywhere - http://askubuntu.com/a/613799
1. FFMpeg permission denied error - http://askubuntu.com/a/478019
1. One liner ffmpeg (or other) to get only resolution? - http://askubuntu.com/a/577431 / http://stackoverflow.com/a/29585066 (json)
1. Revert to a commit by a SHA hash in Git? - http://stackoverflow.com/a/1895095

----------------------------------------------------------------------------------------------------------------------------------------------------------------

