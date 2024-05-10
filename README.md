# Meta Back-end Capstone Project
This is the capstone project for the Meta Back-End Development Certificate

# Commands

``` bash
python3 -m venv littlelemon
source littlelemon\bin\activate
pip3 install django
# create a django project
django-admin startproject littlelemon
# run development server
cd littlelemon
python manage.py runserver
# create a django app 
python manage.py startapp restaurant
# install client
pip3 install mysqlclient
```

```sql
create database littlelemon;
use littlelemon;
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'admindjango'@'localhost';
```

```bash
python3 manage.py migrate 
python3 manage.py makemigrations
python3 manage.py createsuperuser
#user:admin
#email: admin@littlelemon.com
#password: admin@123
pip3 install djangorestframework
```

GET in 
http://localhost:8000/api/menu/1

```json
 {
    "id": 1,
    "title": "Chicken Rice",
    "price": "11.00",
    "inventory": 50
}
```
GET in 
http://localhost:8000/api/menu

- Get all menus items

POST http://localhost:8000/api/menu/

BODY
```json
{
    "title": "Menu Item",
    "price": "100.00",
    "inventory": 3
}
```
RESULT
```json
{
    "id": 2,
    "title": "Menu 2",
    "price": "100.00",
    "inventory": 3
}
```


GET in 
http://localhost:8000/api/booking/tables

```json
[
    {
         "id": 1,
         "name": "Jakub",
         "number_of_guests": 4,
         "booking_date": "2024-05-10T18:10:00Z"
    }
]
```

```bash
pip3 install djoser
```

navigate to http://127.0.0.1:8000/auth/token/login/ to get the token  
```
user: "super  
password: "123"
```

use http://127.0.0.1:8000/auth/token/logout/ to logout with the token in the header

## Testing
```bash
python3 manage.py test
```

```sql
GRANT ALL PRIVILEGES ON `test_littlelemon`.* TO 'admindjango'@'localhost';
FLUSH PRIVILEGES;
```
To execute the UnitTestCases, open VSC terminal and enter this :
```bash
 python3 manage.py test
```
Please make sure you have activated the virtual environment and navigated into the 'littlelemon' directory before running the unit-test command.

For testing, you can make use of the following API endpoints with Insomnia or Postman clients based on your choice.

DJOSER endpoint, for example, to perform a POST request and register a new user.
```
/auth/users/
```

To log in and obtain an authentication token.
```
/api-token-auth/
```

To log-in using DJOSER endpoint.
```
token/login
```

Menu items endpoints are as follows:
```
/api/menu/
/api/menu/{menuItemId}
```

Table reservations endpoints are as follows: 
```
/api/booking/tables/
/api/booking/tables/{bookingId}
```