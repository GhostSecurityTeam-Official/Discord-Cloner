from os import system
import psutil
from pypresence import Presence
import time
import sys
start_time=time.time()
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}


   _____ _               _      _____                      _ _           _______                   
  / ____| |             | |    / ____|                    (_| |         |__   __|                  
 | |  __| |__   ___  ___| |_  | (___   ___  ___ _   _ _ __ _| |_ _   _     | | ___  __ _ _ __ ___  
 | | |_ | '_ \ / _ \/ __| __|  \___ \ / _ \/ __| | | | '__| | __| | | |    | |/ _ \/ _` | '_ ` _ \ 
 | |__| | | | | (_) \__ | |_   ____) |  __| (__| |_| | |  | | |_| |_| |    | |  __| (_| | | | | | |
  \_____|_| |_|\___/|___/\__| |_____/ \___|\___|\__,_|_|  |_|\__|\__, |    |_|\___|\__,_|_| |_| |_|
                                                                  __/ |                            
                                                                 |___/                                                                                      
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}Developed by: Ghost Security Team.{Style.RESET_ALL}
        """)
token = input(f'Please enter your token:\n >')
guild_s = input('Please enter guild id you want to copy:\n >')
guild = input('Please enter guild id where you want to copy:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


  ______ _       _     _              _ 
 |  ____(_)     (_)   | |            | |
 | |__   _ _ __  _ ___| |__   ___  __| |
 |  __| | | '_ \| / __| '_ \ / _ \/ _` |
 | |    | | | | | \__ | | | |  __| (_| |
 |_|    |_|_| |_|_|___|_| |_|\___|\__,_|
                                        

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)
