
import os

from discord.ext import commands
from dotenv import load_dotenv

from aternosapi import AternosAPI

def main():
    load_dotenv()
    discord_token = os.getenv('DISCORD_TOKEN')
    aternos_cookie = os.getenv('ATERNOS_COOKIE') 
    aternos_token = os.getenv('ATERNOS_TOKEN')
    aternos_user_agent = os.getenv('ATERNOS_USER_AGENT')

    print(f'discord: {discord_token}\n aternos token: {aternos_token}\n user agent: {aternos_user_agent} \naternos cookie: {aternos_cookie}')
    bot = commands.Bot(command_prefix='~')
    aternos_server = AternosAPI(aternos_cookie, aternos_token, aternos_user_agent)

    @bot.command(name='status')
    async def status(server):
        await server.send(f'Server Status: {aternos_server.GetStatus()}')

    @bot.command(name='start')
    async def start(server):
        await server.send(aternos_server.StartServer())

    @bot.command(name='stop')
    async def stop(server):
        await server.send(aternos_server.StopServer())

    bot.run(discord_token)


if __name__ == '__main__':
    main()