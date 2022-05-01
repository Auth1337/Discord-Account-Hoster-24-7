'''
- KaramveerPlayZ#1337
- Account Hoster Open Source Emoji Supported 
- Name Of Status Isn't Supported By Discord
- /indiaop
'''
import discord
import discord.ext.commands
import json
import os, sys
from discord.gateway import DiscordWebSocket
os.system("pip install discord.py==1.7.3")
os.system("clear")
os.system("title Discord Acount Hoster Loading Config - KaramveerPlayZ#1337")
token = input(f"KaramveerPlayZ#1337 | Enter Discord Account Token: ")
os.system("clear")
with open('settings.json') as f:
  settings = json.load(f)

emoji = settings.get('Emoji')
status = settings.get('Type')
lowertext = status.lower()

async def identify(self):
    payload = {
        'op': self.IDENTIFY,
        'd': {
            'token': self.token,
            'properties': {
                '$os': sys.platform,
                '$browser': 'Discord Android',
                '$device': 'Discord Android',
                '$referrer': '',
                '$referring_domain': ''
            },
            'compress': True,
            'large_threshold': 250,
            'v': 3
        }
    }

    if self.shard_id is not None and self.shard_count is not None:
        payload['d']['shard'] = [self.shard_id, self.shard_count]

    state = self._connection
    if state._activity is not None or state._status is not None:
        payload['d']['presence'] = {
            'status': state._status,
            'game': state._activity,
            'since': 0,
            'afk': False
        }

    if state._intents is not None:
        payload['d']['intents'] = state._intents.value

    await self.call_hooks('before_identify', self.shard_id, initial=self._initial_identify)
    await self.send_as_json(payload)

if lowertext == "mobile":
  DiscordWebSocket.identify = identify

client = discord.ext.commands.Bot(command_prefix=">", intents=discord.Intents.all(), help_command=None, case_insensitive=False)

@client.event
async def on_ready():
  os.system("title Discord Account Hoster Account Hosted Successfully - [KaramveerPlayZ#1337]")
  if lowertext == "idle":
    await client.change_presence(activity=discord.CustomActivity(name=None, emoji=emoji), status=discord.Status.idle)
  elif lowertext == "dnd":
    await client.change_presence(activity=discord.CustomActivity(name=None, emoji=emoji), status=discord.Status.dnd)
  elif lowertext == "online":
    await client.change_presence(activity=discord.CustomActivity(name=None, emoji=emoji), status=discord.Status.online)
  elif lowertext == "mobile":
    await client.change_presence(activity=discord.CustomActivity(name=None, emoji=emoji))

@client.event
async def on_connect():
  print(f"Discord Account Successfully Hosted\nUsername: {client.user}\nID: {client.user.id}")

client.run(token, bot=False)
