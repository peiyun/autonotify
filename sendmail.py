#!/usr/bin/python

import smtplib
import sys

subject = sys.argv[1]
content = sys.argv[2]

sender = 'from@domain.com'
receiver = 'to@domain.com'

message = """From: sender <%s>
To: receiver <%s>
Subject: <%s>

%s
"""%(sender, receiver, subject, content)
print message

try:
	session = smtplib.SMTP('smtp.domain.com',587)
	session.ehlo()
	session.starttls()
	session.ehlo()
	session.login(sender,'password')
	session.sendmail(sender,receiver,message)
	session.quit()
	# smtpObj = smtplib.SMTP('localhost')
	# smtpObj.sendmail(sender, receiver, message)         
	print "Successfully sent email"
except smtplib.SMTPException:
	print "Error: unable to send email"