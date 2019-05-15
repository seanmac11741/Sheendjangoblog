https://www.youtube.com/watch?v=UmljXZIypDc
following this tutorial to create a django website
mkvirtual env djangotutorialenv
pip install django
django-admin
django-admin startproject django_project
http://localhost:8000/ is the same as the thing in cmd window
http://localhost:8000/admin/login/?next=/admin/ is the admin site, by default


part2 https://www.youtube.com/watch?v=a48xeeo5Vnk create an app
can have multiple apps in a website, blog app, api app

manage.py startapp blog            
that creates a blog app
Everything goes to the main urls.py first, then we can send it around based on the url

part3 https://www.youtube.com/watch?v=qDwdMDQ8oX4 making templates
within blog directory, create templates directory and in there make another blog directory
omg type in "html" then hit tab and it fills it in for you.... super nice
add the base.html and then inherit from it for home and about.html
{% code goes here %}
{{ dict.var goes here }}

part4 with full playlist https://www.youtube.com/watch?v=1PkNiYlkkjo&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=4
to create new user: manage.py createsuperuser ERROR, no such table
manage.py makemigrations
manage.py migrate
manage.py createsuperuser  pw = testing321
http://localhost:8000/admin/ default admin site

part5 databases https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=5
ORM- object relational mapper, can use different databases without changing code... wow that is nice
sqllite for dev, postgress for production
manage.py makemigrations   #this will make db migrations
to find actual sql code that will be run, goto django_project/blog/migrations/0001_initial.py
manage.py sqlmigrate blog 0001  #that will print the sql code that is run

manage.py migrate  #this will apply all migrations to the data and generate sql to fix the db
manage.py shell    #this will run the shell to query the db directly

>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()          #this is a query line
<QuerySet [<User: smcconn3>, <User: TestUser>]>

to get out of the shell prompt, enter this: exit()
man this is cool.... need to do this daily if possible

Part6 user registration https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6
create a new app for the user registration stuff
manage.py startapp users  #makes a new users apps
remember, new apps go to project settings.py
all the class tags in the html are inherited from the base.html which uses the bootstrap css files
crispy forms works with Django nicely
pip install django-crispy-forms
crispyforms just makes all of the forms look alot nicer... love that there are easy automated ways to do CSS

Part7 https://www.youtube.com/watch?v=3aVqWaLjqS4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=7
create authentication system for users to login and log out. as well as need auth to get to certain pages
added some stuff to the base.html as well to dynamically change based on if you are logged in or not

Part8 https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8
create user picture and stuffs
remember whenever you are changing the models.py files, that means you are doing db changes, so you need to register those
changes, using these commands. also need to register in the admin.py file(s) one for each app :
manage.py makemigrations
manage.py migrate
says you need pillows
pip install pillow
pictures, cool, signals didn't make a ton of sense to me... they kind of seem like a listener

Part9 https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9
Update user Profiles, resize images. Broke registration for whatever reason, so I had to add a few
  arguements to the users/models.py file from https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert/52351829

Part10 CRUD operations on Posts https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=10
class-based views, make one to view the details of a post
now make a view to create a post
now require login to change posts


Part11 https://www.youtube.com/watch?v=acOktTcTVEQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=11
pagination

Par12 https://www.youtube.com/watch?v=-tyBEsHSv7w&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=12
email and password reset
setting environ vars in windows https://www.youtube.com/watch?v=IolxqkL7cD8
for whatever reason, the environ vars aren't working.... sad day... hardcoded for now, but def dont commit that!

Part16 to store files and photos on AWS webbuckets. Can't do that on Heroku, they delete it

Part17 Deploy to Heroku! https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17
gitignore from here https://github.com/github/gitignore/blob/master/Python.gitignore
heroku create sheendjangoblog   #to make the app
create procfile web: gunicorn django_project.wsgi. This just tells heroku to use gunicorn
good god i really messed up file structure when I started... should be fixed now
to set Heroku env variables!!!!
heroku config:set DEBUG_VALUE="True"
dont forget to do that for aws stuff when you get there
setup postgress on windows https://devcenter.heroku.com/articles/heroku-postgresql#set-up-postgres-on-windows


follow-up stuff
bootstrap, does css and html for you, so nice... https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template
