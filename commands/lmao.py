# used for the help command
USAGE = "lmao"
DESCRIPTION = "lol"

# the lol message
LOL = "Nani the fuck did you just fucking hanashimasu about watashi," \
      " anata little konoyarro? watashi will have anata know watashi " \
      "graduated ichiban of my gakkou in the Navy Seals, and watashi" \
      " has been involved in numerous secret raids on Al-Quaeda, and " \
      "watashi have over san hyaku confirmed shinimasu. watashi am benkyou" \
      " in gorilla warfare and I’m the ichiban  sniper in the entire US armed " \
      "forces. Anata are nothing to watashi but just another target. Watashi will " \
      "wipe anata the fuck out with precision the likes of which has zenzen been " \
      "mimasu before on this sekai, mark watashi no fucking words. anata think " \
      "anata can get away with hanashimasu that shit to watashi over the Internet?" \
      " Think again, fucker. As oretachi hanashimasu watashi am contacting my secret " \
      "network of spies across the USA and your IP is being traced right now so anata" \
      " better prepare for the storm, mushi. The storm that wipes out the warui chiisai" \
      " mono anata call your life. You’re fucking shinimasu, kodomono. Watashi" \
      " can be anywhere, anytime, and I can korosu anata in over shichi hyaku ways," \
      " and that’s just with my bare te. Not only am watashi sugoi trained in unarmed " \
      "combat, but watashi have access to the entire arsenal of the United States Marine" \
      " Corps and watashi will shimasu kore to its full extent to wipe your miserable " \
      "oshiri off the kao of the continent, you chiisai shit. If only anata could have " \
      "shiteiru what unholy retribution your chiisai “clever” comment was about to bring" \
      " down upon anata, maybe anata would have held your fucking shita. But anata muri" \
      " desu, anata didn’t, and now you’re paying the price, anata goddamn baka. watashi " \
      "will shit fury all over anata and anata will drown in it. anata wa fucking shinimasu, kodomono"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, LOL)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION
