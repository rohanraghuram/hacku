import base64
import os
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from sendgrid import SendGridAPIClient

to_emails=[
    #('rohanraghuram37@gmail.com', 'Rohan Raghuram'),
    #('raghuramkanakatte@gmail.com', 'KG Raghuram'),
    ('vedant.bajaj14@gmail.com', 'Vedant Bajaj')
]


message = Mail(
    from_email=('rraghuram@umass.edu', 'company1'),
    to_emails= to_emails,
    subject='How was your recent order with us ?',
    html_content='<strong>Thank you for shopping with us and  we hope you enjoyed your purchase. Our ultimate goal is to provide our customers with the best serivce possible and that includes finding out areas we can improve.<br> We deeply appreciate your support and would value your input.<br></strong><em>Please reply to this email with your feedback<em>')
'''
file_path = 'unnamed.png'
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('application/png')
attachment.file_name = FileName('test_filename.png')
attachment.disposition = Disposition('attachment')
attachment.content_id = ContentId('Example Content ID') 
#message.attachment = attachment
'''
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
