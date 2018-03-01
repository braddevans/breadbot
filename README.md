## Installation
1. modify config.ini to have your bot token, prefix, and your user id
2. `python3.5 bot.py`
3. success?

## Credits
1. Discord.PY -> The Discord API Wrapper Used :D

## Adding a command
1. make a new python file in commands with the name you want it to be triggered with
2. 
```
# used for the help command
USAGE = ""
DESCRIPTION = ""

# the main function that's ran when this script is called
async def run(message, client, args):
    None # code goes here

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION
```
3. restart the bot
