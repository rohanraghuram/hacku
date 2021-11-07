import base64
import os
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from sendgrid import SendGridAPIClient

to_emails=[
    ('customer@example1.com', 'customer1'),     #customer email IDs and names must be inserted here
    ('customer@example2.com', 'customer2'),
    ('customer@example3.com', 'customer3')
]


message = Mail(
    from_email=('company1@example.com', 'company1'),   #user email ID must be inserted here
    to_emails= to_emails,
    subject='How was your recent order with us ?',     
    html_content='<strong>Thank you for shopping with us and  we hope you enjoyed your purchase. Our ultimate goal is to provide our customers with the best serivce possible and that includes finding out areas we can improve.<br> We deeply appreciate your support and would value your input.<br></strong><em>Please reply to this email with your feedback<em>')

try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
