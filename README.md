# 5g-hackathon


Project:
5G hackathon Registration Form

Website:

5G hackathon Registration Form

# Simple Registration/Login code in PYTHON

Read more:[PYTHON registration form](http://127.0.0.1:8000/5GHackathon/home/) 

#################################################

## IDE Requirments

1. Python 
	Go to Google ---->Download python latest Version ---->Download setup nd Install
2.Django

	Go to Command prompt --->  pip install Django
3.crispy-Forms 
	pip install django-crispy-forms
################################################

## Installation
1. First we need to install visual studio and python IDE

#################################################

## Process ( 5G hackathon Registration Form )


1. Select path where file is prasent    ---------------   (like:    C:\Users\SHAZY CHINNU\Desktop\Sample\My Project\INB )

2. python manage.py runserver      ----------------  (Now, we have to run the server---)

	Explanation of the above cmd:

python----> calling the python interpreter
python manage.py -----> calling the python interpreter to execute the code in manage.py file
python manage.py runserver -----> runserver is a command line argument
If the above cmd is executed,the control will switch to manage.py file 

manage.py
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

Explanation:

__name__ :
__name__ property will have the default name as __main__
so, 
__main__ == __main__  is true.

3.Now type http://127.0.0.1:8000/ in the web broswer and click on enter.
We can see a message as "Congragulations on your first Django-powered page"

If we want to run the server(start) the server again,type the below command-
python manage.py runserver 

Now again if we type http://127.0.0.1:8000/ it will run and shows the power page.

####################################################################

## Files
Personal----------------------------------->package
		migrations
			__init__.py
		__init__.py
		admin.py
		apps.py
		models.py
		tests.py
		views.py



================1)views===============================

View is simply called as a "function definiton" or reusable logic.

The output of this reusable code is shown to the user on the webpage.Thats why this reusable code is called as a view.

=============2)url=====================
Users can see the output of a view only by using (typing) a url in the address bar of the browser.

note :- 
In the url, r means read as it is.For example, if test/techno is there,then if we dont put r then it may be read like /t means like tab..So to avoid all those, we are putting r


Explanation:

request.user will check for the user name in auth_user table.
If the user is authenticated,it should show logout.If not,it should show Login and Register

When user enter details in register form the all details will stored in sqlite3 database in Django
The deatails will be stored in this format
('registration_time','registration_number','Name','email','gender','address','MobileNum','Password','city','profession')

And After submit the details acknowledgement will be displaed Register Number and Name .
