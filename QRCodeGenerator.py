import pyqrcode
s= "Hey ladies and gentleman \nMyself Ketki Dandgavale \n I am a Computer Science student\tI am currently studying in " \
   "Bharti Vidyapeeth College in pune\n My native is nashik "
url=pyqrcode.create(s)
url.svg("MyQRCode.svg",scale=8)
# Output will be saved in MyQRCode.svg file
