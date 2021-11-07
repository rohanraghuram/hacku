## Responsum
At the heart of every succesful business is customer engagement and is especially important if you are running a small business which you are looking to scale. Most small businesses
either have little to no online presence or choose to use social media applications to market their products and often carry out transactions through the same sites. 
This is completely understandable as building a webiste might seem like a tedious task and consulting web development services may seem too execcessive for your business.

Fortunately, Responsum solves this problem by giving you the ability to automate conversations with customers and storing their responses in a database which can be analysed in the future to help your business take those small steps in the right direction.

## How it was built 
Twilio SendGrid Email API - The Twilio SendGrid Mail Send API and python were used to implement the automation of the mail sends to the customer mail IDs.

Zapier - Access to Zapier's email parser in order to parse through email replies and store this information in a database.

## Code files 
emtester.py - This is the python script that needs to be run in order to send emails to customer IDs. Requires the sendgrid package as well as the sendgrid API key to authenticate its use.
