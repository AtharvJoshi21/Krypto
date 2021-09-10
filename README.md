Created three python files, one for API and two for email sender.
The Krypto.py file is for API in this file i have used canvas for creating the API.
Featched the data from the given link and stored in one variable.
Also stored the time at which the price of crypto we stored.
The buttons for Create and delete are also created for users.

In the mail.py file,I have used the panda,datetime,smtplib ,Email libraries. 
The EMAIL_USER and EMAIL_PASS are the password and email address of user and it was imported from another file name called keys for the privacy.
The user will set the target in TargetPrice variable and the current price is stored in currentClose variable.
When the currentClose will Hit the TargetPrice , it will send the email to the givan email address of the user with the given message.
The currentClose will be again do the same activity after every 1 minute.
