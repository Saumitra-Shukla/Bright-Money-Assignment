## Make and enter a virtaul env  

```sh
$ virtualenv env
```
```sh
$ source env/bin/activate
```  

## Setup MySQl (You can use default SQLite but due to Async API calls the database may get locked.)
```sh
$ sudo apt install mysql-server
```
```sh
$ sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
```
```sh
$ pip3 install mysqlclient
```
```sh
$ sudo mysql -u root
```
```sh
mysql> CREATE DATABASE plaid_manager;
```
```sh
mysql> CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
```
```sh
mysql> GRANT ALL ON blog_data.* TO 'djangouser'@'%';
```
```sh
mysql> FLUSH PRIVILEGES;
```
  
## install RabbitMq (for Async Message Queue)

### Add a repository
```sh
$ - wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc |
     sudo apt-key add -
```
```sh
$ - wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
```
```sh
$ - sudo apt-get update
```

### install
```sh
$ sudo apt-get install rabbitmq-server
```


## install all dependencies
```sh
$ pip3 install -r requirements.txt 
```  
### Replace Sqlite DB or enter MySQL details in settings.py  
  
![](/api_photos/settings.png)

## **Replace your Plaid Client details in .env file in PlaidApp  
  
## Setup Models  

```sh
$ python3 manage.py makemigrations CustomUser,PlaidApp 
```
```sh
$ python3 manage.py migrate 
```
```sh
$ python3 manage.py runserver 'port' 
```

![](/api_photos/runserver.png)
  
## Start Celery worker  

```sh
$ celery -A plaid_manager worker -l info
```
![](/api_photos/rabbitmq.png)
  
## API END-PONTS  
  
@http://localhost:8080/  
  
### User API [ all POST req ]: (When hitting API with Postman make sure to include X-CSRFToken in Headers)  
  
-  api/signup/ -- User-Signup-API  
![](/api_photos/signup.png)
-  api/login/  -- User-Login-API  
![](/api_photos/login.png)
-  api/logout/  -- User-Logout-API  
![](/api_photos/logout.png)
  
### Plaid API  
  
[POST req]  
  
-  plaid/link_token/ ------- Get-Plaid-Link_Token 
![](/api_photos/link_token.png)  
-  plaid/get_access_token/ - Plaid-Link-Public_token (exchange public token with access_token)  
![](/api_photos/2.png)
![](/api_photos/3.png)
![](/api_photos/6.png)
  
[GET req]  
  
-  plaid/home/  ------------------ Get-Public_token 
![](/api_photos/1.png) 
-  plaid/get_items/	--------------  Get-All-Items  
![](/api_photos/items.png)
-  plaid/get_accounts/ ---------- Get-All-Accounts 
![](/api_photos/acc.png) 
-  plaid/get_transactions/ -------  Get-All-Transactions  
![](/api_photos/trans.png)
-  plaid/transaction_webhook/ - Transaction-Webhook  
![](/api_photos/webhook.png)



## Model Details:

### CustomUserModel
  
- email
- username
- date_joined
- last_login
- is_admin
- is_active
- is_staff
- is_superuser  
  
### BankItemModel
  
-	bank_item_id
-	access_token
-	request_id
-	user  
  
### AccountModel
  
-	account_id = models.CharField(max_length=100)
-	bank_item = models.ForeignKey(BankItemModel, on_delete=models.CASCADE)
-	balance_available = models.FloatField(default=None, null=True)
-	balance_current = models.FloatField()

### TransactionModel
  
-	transaction_id
-	account
-	amount
-	date
-	name
-	pending
  
### APILogModel

-	request_id
-	api_type
-	date_log




