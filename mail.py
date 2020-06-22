import smtplib
import ssl
import sys
import json

with open('emp_data.json', 'r') as f:
    employee = json.load(f)

print(employee['name'])

def MailApprove():

    # try:
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "eashanjindal99@gmail.com"
    receiver_email = "jindal.3@iitj.ac.in"
    password = "@Eashan2000"
    message = """\
    FROM: """+sender_email+"""
    TO: """+receiver_email+"""
    Subject: "Resignation Application approved\n
    Dear """+employee['name']+"\n"+"Your application for resignation has been approved by me and as been forwarded to concerned authorithies for furthers approvals."+"\n"+"\n"+"Regards"+"\n"+"Registar"+"\n"+"IIT Jodhpur"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email,receiver_email, message)