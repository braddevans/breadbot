# used for the help command
USAGE = "furry"
DESCRIPTION = "lol"

# the lol message
furry = "wof"
furryimg = "https://memestatic.fjcdn.com/large/pictures/90/40/90405c_6373348.jpg"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, furry)
    await client.send_message(message.channel, furryimg)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


