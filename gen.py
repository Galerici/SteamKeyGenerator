import random
import colorama 
from colorama import Fore, Back, Style

simvols="ABCDEFGHIKLMNOPQRSTVXYZ1234567890"#символы
file=open("keys.txt","w")

colorama.init()
print(Fore.RED)

print( """

╔═╗╔╦╗╔═╗╔═╗╔╦╗  ╦╔═╔═╗╦ ╦  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
╚═╗ ║ ║╣ ╠═╣║║║  ╠╩╗║╣ ╚╦╝  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
╚═╝ ╩ ╚═╝╩ ╩╩ ╩  ╩ ╩╚═╝ ╩   ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═
Discord: discord.gg/HMMGKdC
Github: github.com/Galerici
                                                       
 """ + Fore.RESET)



while True:
	try:
		many=int(input("How many?: "))#кол-во ключей
		break
	except:
		print("You are input not number!")

while True:
	try:
		save_mode=int(input("How show keys?:\n1)in txt file(recommended)\n2)in console\n"))
		break
	except:
		print("Please, input number!")

for i in range(many):
	key=""
	for i1 in range(2):
		for i2 in range(5):
			key+=simvols[random.randint(1,len(simvols)-1)]
		key+="-"
	for i2 in range(5):
		key+=simvols[random.randint(1,len(simvols)-1)]
	
	if save_mode==1:
		file.write(key+"\n")
	elif save_mode==2:	
		print(key)

file.close()
print("\nKeys generating finished.You can close programm.")
while True:
	pass
