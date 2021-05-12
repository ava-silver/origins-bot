from aternosapi import AternosAPI
import os
from dotenv import load_dotenv

load_dotenv()
headers_cookie = os.getenv('ATERNOS_COOKIE') 
TOKEN = os.getenv('ATERNOS_TOKEN')
user_agent = os.getenv('ATERNOS_USER_AGENT')
server = AternosAPI(headers_cookie, TOKEN, user_agent)

def cmd(cmd):
	if cmd == "start":
		print(server.StartServer())
	if cmd == "stop":
		print(server.StopServer())
	if cmd == "status":
		print(server.GetStatus())
	if cmd == "info":
		print(server.GetServerInfo())

while True:
	icmd = input("[*] > ")
	cmd(icmd)
