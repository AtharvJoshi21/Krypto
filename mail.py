#for sending the automated mails
import os
import smtplib
import imghdr
from email.message import EmailMessage

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import time

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()

yf.pdr_override() # <== that's all it takes :-)
start =dt.datetime(2020,12,1)
now = dt.datetime.now()

stock="QQQ"
# Your target price
TargetPrice=180

msg['Subject'] = 'Alert on '+ stock+'!'
msg['From'] = EMAIL_ADDRESS
# Enter the email address your mail address for the messages
msg['To'] = 'xyz@gmail.com'

alerted=False

while 1:

	df = pdr.get_data_yahoo(stock, start, now)
	currentClose=df["Adj Close"][-1]

	condition=currentClose>TargetPrice

	if(condition and alerted==False):

		alerted=True

		message=stock +" Has activated the alert price of "+ str(TargetPrice) +\
		 "\nCurrent Price: "+ str(currentClose)

		print(message)
		msg.set_content(message)

		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		    smtp.send_message(msg)

		    print("completed")
	else:
		print("No new alerts")
	time.sleep(60)