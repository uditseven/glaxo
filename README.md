# glaxo
A medicine inventory management system.


## Setup
- Activate Virtual Environment
```
foo@bar:~$ source ./venv/bin/activate
```


## Install

- Install requirements by typing this:
```
foo@bar:~$ pip install -r requirements.txt
```
- Migrate Database by typing this:
```
foo@bar:~$ python manage.py migrate
```
- Create new user by typing this:
```
foo@bar:~$ python manage.py createsuperuser
```
- Run server by typing this:
```
foo@bar:~$ python manage.py runserver
```
- Reset port by typing (If required):
```
foo@bar:~$ sudo fuser -k 8000/tcp
```
#
**Creators:**
Shubham Anand &
Udit Pandey

