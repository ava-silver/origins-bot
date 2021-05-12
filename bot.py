
import os

from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
from aternosapi import AternosAPI

LOGGING = True

def main():
    load_dotenv()
    discord_token = os.getenv('DISCORD_TOKEN')
    aternos_cookie = os.getenv('ATERNOS_COOKIE') 
    aternos_token = os.getenv('ATERNOS_TOKEN')
    aternos_user_agent = os.getenv('ATERNOS_USER_AGENT')

    STATUS = 'status'
    INFO = 'info'
    START = 'start'
    STOP = 'stop'

    if LOGGING:
        print(f'discord: {discord_token}\n aternos token: {aternos_token}\n user agent: {aternos_user_agent}\n') #aternos cookie: {aternos_cookie}\n\n')
    bot = commands.Bot(command_prefix='~')
    aternos_server = AternosAPI(aternos_cookie, aternos_token, aternos_user_agent)


    @bot.command(name=STATUS)
    async def status(server):
        await handle_command(server, aternos_server, STATUS)

    @bot.command(name=START)
    async def start(server):
        await handle_command(server, aternos_server, START)

    # @bot.command(name=STOP)
    # async def stop(server):
        # await handle_command(server, aternos_server, STOP)

    bot.run(discord_token)

async def handle_command(discord_server, aternos_server, name):

    switcher = {
        'status' : aternos_server.GetStatus,
        'info'   : aternos_server.GetServerInfo,
        'start'  : aternos_server.StartServer,
        'stop'   : aternos_server.StopServer
    }

    response = (switcher.get(name))()
    if name == 'status':
        response = f'Server Status: {response}'
    
    if LOGGING:
        print(f'{datetime.now()} -- {name.upper()} -> {response}')
    await discord_server.send(response)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass