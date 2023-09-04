import os
import discord
import toml

bot = discord.Bot()

# Config template
config = {
    'Config': {
        'VERSION': '3'
    },
    'Discord': {
        'TOKEN': ''
    },
    'Minecraft': {
        'authtype': 'ftp'
    },
    'FTP': {
        'host': '',
        'user': '',
        'pass': ''
    }
}
if not os.path.isfile('config.toml'):
    with open('config.toml', 'w') as f:
        toml.dump(config, f)
    print('Config file created, add discord bot token and start the bot.')
    exit()
elif os.path.isfile('config.toml'):
    with open('config.toml', 'r') as f:
        data = toml.load(f)
    version = data['Config']['VERSION']
    if version != '3':
        print(
            'Error: Config version is outdated, rename your `config.toml` file or move to another folder and resart the bot')
        exit()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


cogs_list = [
    'download',
    'link',
    'info'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')


with open("config.toml", "r") as f:
    data = toml.load(f)
TOKEN = data['Discord']['TOKEN']
try:
    bot.run(TOKEN)
except:
    print('Error: Invalid or no Discord token, check `config.toml`')
    exit()
