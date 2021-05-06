# SUPER SHOP MANAGEMENT

## Setup
At first clone the repository
```
 git clone https://github.com/tashfiq12/supershopmanagement.git
 cd supershopmanagement
```
At first install pip,check pip version, then  install dependencies
```
 pip install -r requirements.txt
```
Then migrate the tables and database, I used mysql db in my project .
```
 python manage.py migrate
```
Then run the project
```
 cd supershopmanagement
 python manage.py runserver
```
## Project overview
This is mainly a supershop receipt generation app.After running the project we will see there is a product table. We can add new products by clicking on the Create new product 
button.All the basic crud functionalities of the products table can also be performed. Then in this there page is a button for creating order. By clicking this button we 
will go to order page. From this page if we select product items from the table by checking checkboxes ,input quantity and other essential details then we will go to the receipt
page.If we click on the print button then it will either print or save as pdf. Customer info is stored as a QRCODE.

## Technology used
* Python 3
* Django
* Bootstrap
* JAVASCRIPT
* MYSQL DATABASE
