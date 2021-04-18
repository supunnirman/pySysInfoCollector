import platform
from datetime import datetime
import socket
import psutil
import inquirer
import time
import random


#BYTES CALCULATOR###############################
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
#################################################
questions1 = [
  inquirer.List('company',
                message="SELECT ASSET OWNED COMPANY = ",
                choices=['LANKA WALLTILES PLC', 'LANKA TILES PLC', 'SWISSTEK CEYLON PLC', 'TONER SUPPLIER', 'OTHER'],
            ),
]
answers1 = inquirer.prompt(questions1)

name = input("WHO IS THE USER ")
serial = input("SERIAL NUMBER ")
dept = input ("WHAT IS THE DEPARTMENT ")

questions2 = [
  inquirer.List('location',
                message="FOUND LOCATION = ",
                choices=['HEAD OFFICE', 'NARAHENPITA FACTORY OUTLET', 'JAWATTE', 'NAWALA FD UNIT', 'MEEPE','RANALA','ON FIELD'],
            ),
]
answers2 = inquirer.prompt(questions2)
#COLLECT INFORMATION
svmem = psutil.virtual_memory()
now = datetime.now()#VAR for DATETIME
randomNum = random.randint(0,40)
randomNumVar = str(randomNum)


companyName = (answers1["company"])
location = (answers2["location"])
deptName = (dept)
fullname = (name)                    #GET COMPUTER OWNER NAME
hostname = (socket.gethostname())    #GET COMPUTER HOSTNAME
uname = platform.uname()
release = (f"{uname.release}")
winver = (f"{uname.version}")
currDateTime = now.strftime("%m-%d-%Y %H:%M")


answer = (f"""==============================================================
SYSTEM INFORMATION COLLECTOR v1.0
DEVELOPED BY SUPUN NIRMAN KARUNARATHNE \n
REPORTED ON : {currDateTime}
========================BASIC INFO =================================\n
ASSIGNED TO             : {name.upper()}
CURRENT LOCATION        : {location.upper()}
COMPUTER OWNED BY       : {companyName}
DEPARTMENT              : {deptName.upper()}
HOSTNAME IS             : {hostname}
SERIAL NO               : {serial}
RELEASE                 : {release}
WINDOWS VERSION         : {winver} \n
======================== Memory Information ======================= \n
Total                   : {get_size(svmem.total)}
Available               : {get_size(svmem.available)}
Used                    : {get_size(svmem.used)}
Percentage              : {svmem.percent}% \n


""")



#GET DATE TO VARIABLE TO RENAME FILE

date_time = now.strftime("%m-%d-%Y-%H:%M")#GET CURR DATE TIME TO RENAME FILE

#WRITE INFORMATION
file = open(r"d:/Python/"+socket.gethostname()+" - "+randomNumVar+".txt", "w") #attribute "a" will continue data. and "w" will overwrite everything
file.write(answer)

print("ALL INFORMATION RECORDED ON SERVER FOLDER")
exit()

