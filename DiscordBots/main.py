import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
import pyjokes
import praw
from discord.ext import commands


# client = discord.Client()


reddit = praw.Reddit(
    client_id="**censcored (^-^)", client_secret="**censcored (^-^)", username="**censcored (^-^)", password="**censcored (^-^)", user_agent="**censcored (^-^)")

client = commands.Bot(command_prefix="$")

sad_words = ["bsdk", "laude", "gandu", "mkl", "bkl", "bhosdk", "chutiye", "chutiya", "lund", "lode", "fuck", "fuck off", "fuck me", "shit", "bitch", "asshole",  "ma ki chut", "randi", "chut", "lawde",
             "harami", "madarchod", "behenchod", "madharjhat", "betichod", "teri maa ki chut", "bhosdike", "bakchodi", "bish", "backchodi", "jhattu", "lawde", "motherfucker", "Gaand ", "saale", "behen", "chodke", "vivek"]

yashraj_words = ["yashraj", "Yashraj", "whynesspower", "yashu", "Shukla"]

starter_encouragements = [
    "Oye! Gali nahi dene ka, respect women",
    "TU TU TU Gali dega? TU? ",
    "How dare you use a curse word? very bad", "Gali? Tumhare jaise logo ki vajah say he bharat pichay reh gaya", "India was once a godlen sparrow, it was only due to people like you it lost its place, nevermind don't curse from next time", "Don't curse respect women", "theek hai yaar gali bhi chalti hai kabhi kabhaar", "Gali deke honey singh nahi bann jaoge tum log"
]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.top(Limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=" $help"))

    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('$joke'):
        joke = pyjokes.get_joke()
        await message.channel.send(joke)
    if msg.startswith("$bzk"):
        # joke= pyjokes.get_joke()
        await message.channel.send("ZINDABAD!")

    if msg.startswith('$jec'):
        # joke= pyjokes.get_joke()
        await message.channel.send("ZINDABAD!")

    # if msg.startswith('$'):
    #   # joke= pyjokes.get_joke()
    #   await message.channel.send("ZINDABAD!")

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]
        if msg.startswith('$help'):
            # joke= pyjokes.get_joke()
            await message.channel.send("$inspire - motivational quote \n $joke - gives a not so funny joke \n $bzk - cheer up! \n $responding false - disables working of the bot\n $responding true - turns working of the bot back on \n beside these features this bot also detect curse words and suggest you not to use them anymore XD  ")

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

        if any(word in msg for word in yashraj_words):
            await message.channel.send("Hello there! I don\'t think Yashraj is available right now, reach out to this cell phone or instagram handle, Thank you,  and \t PS: You are really important to him I noticed that thing for sure! keep spreading love see you! ")

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")

keep_alive()
client.run(os.environ['**censcored (^-^)'])
