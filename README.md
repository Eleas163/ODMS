# Diagnostic Lab Reporting System.
* Live: https://odl-v2.herokuapp.com/
* Developed By Django Web Framework (version: 2.2 Lts).
 
## Instructions (Windows 10x64):
* Some commands may differ depending on OS. Just google it.
* Install latest version of Python3 (64 bit).
* Clone the repository.
* Install and active virtual environment directory:
  1. :~$ cd Repository/venv/Scripts/
  2. :~$ activate
  3. (venv):~$ This '(venv)' sign will be shown up if virtual environment activated successfully.
  
* Install all the requirements using previously opened CMD where the virtual environment was activated:
  >> (venv):~$ pip install -r requirements.txt
  
* Run Local Server:
  >> (venv):~$ python manage.py runserver
  
* PATHs:
  1. System Admin Dashboard: http://127.0.0.1:8000/admin/ (default)
  2. Homepage: http://127.0.0.1:8000/
  3. Diagnostic Admin Login: http://127.0.0.1:8000/admin-login/ (Username = labaid_admin_1, Password = labad1-321)
  4. Diagnostic Staff Login: http://127.0.0.1:8000/staff-login/ (Username = labaid_staff_1, Password = labst1-321)


## Homepage
![Home](https://user-images.githubusercontent.com/23103980/64068231-35e60980-cc57-11e9-94c0-063a1752a4fa.png)

## Diagnostic Staff Dashboard
![Staff Dashboard](https://user-images.githubusercontent.com/23103980/64068244-5615c880-cc57-11e9-9f4e-c6fc9471d8f1.png)

## Diagnostic Admin Dashboard
![Completed Orders Admin](https://user-images.githubusercontent.com/23103980/64068249-6168f400-cc57-11e9-8741-ead7ef8153fd.png)

