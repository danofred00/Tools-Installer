#coding:utf-8
# https://t.me/fredshackerchannel
# https://newfredtech.blogspot.com
    
import os


os.system("clear")
print("\nPatienter Lors de l'installation des packages ...")
def install():
    os.system("pkg install zip unzip figlet toilet php -y")
    os.system("clear")
    os.system("sleep 2")
    os.system('figlet Danofred')
    print("\n")
    print("\n")
    os.system("unzip -r -f module.zip && rm -f module.zip")
    print("\n\n")
    dcs = str(input("Voulez-vous lancer le programme ? (y/n)"))
    if (dcs in 'yY'):
        os.system("./Tools")
    else :
        exit()
        
install()
