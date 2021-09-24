from PIL import Image
import os
import email
import os
import smtplib
from email.mime.multipart  import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from email.mime.base import MIMEBase
from email import encoders

hashtags = open('C:/Users/ccraig/Desktop/hashtags.txt','r').read()
listing_info = 'Zillow Listing'
directory = 'C:/Users/ccraig/Desktop/Listing_Photo/'
i = 0
#im = Image.open('C:/Users/ccraig/Desktop/test1.jpg')

for item in os.listdir(directory):
    im = Image.open('C:/Users/ccraig/Desktop/Listing_Photo/'+item).convert('RGB')
    image = im
    os.remove('C:/Users/ccraig/Desktop/Listing_Photo/'+item)
    i = str(i)
    image.save('C:/Users/ccraig/Desktop/Listing_Photo/conv'+i+'.jpg')
    i = int(i)
    i+=1
 
#Set up crap for the attachments
files = directory
filenames = [os.path.join(files, f) for f in os.listdir(files)]

#Set up users for email
gmail_user = "chadcraigfjm@gmail.com"
gmail_pwd = "BabyAria94-"
recipients = ['chadcraigfjm@gmail.com']

#Create Module
def mail(to, subject, text, attach):
   msg = MIMEMultipart()
   msg['From'] = gmail_user
   msg['To'] = ", ".join(recipients)
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   #get all the attachments
   for file in filenames:
      part = MIMEBase('application', 'octet-stream')
      part.set_payload(open(file, 'rb').read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
      msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   mailServer.close()

#send it
mail(recipients,
   listing_info,
   hashtags,
   filenames)


for item in os.listdir(directory):
    os.remove(directory+item)









