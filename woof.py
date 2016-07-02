#JF - to pass image
# unix.stackexchange.com/questions/problems-running-python-script-from--motion
#search motion event run python script

#Verizon <phone_number>@vtext.com

def woof():
  import smtplib
  import os
  fromaddr = 'sourceemail@gmail.com'
  toaddrs = 'phonenumber@vtext.com,targetemail@gmail.com'
  msg = 'Configurable message'
  username = 'piwoof@gmail.com'
  password = ''
  homedir=os.path.expanduser('~')
  with open(os.path.abspath(homedir+'/.credentials/woof.txt')) as myfile:
    password=myfile.read().rstrip()
  server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
  server.login(username,password)
  server.sendmail(fromaddr,toaddrs,msg)
  server.quit()
  print 'Email sent to ',toaddrs

if __name__=="__main__":
  import sys
  woof()
