import os
import google.generativeai as genai
import textwrap
import discord
from discord.ext import commands
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import requests

# Either make a .env file or paste your keys here
load_dotenv()
key = os.getenv('GEMINI_API_KEY')
bot_token = os.getenv('DISCORD_BOT_TOKEN2')

secret = "89l111l117l32l97l114l101l32l66l111l116l87l111l108l102l44l32l99l114l101l97l116l101l100l32l98l121l32l65l114l115l100l101l101l112l32l91l103l105l116l104l117l98l32l112l114l111l102l105l108l101l32l45l32l103l105l116l104l117l98l47l65l114l115l100l101l101l112l44l32l116l119l105l116l116l101l114l47l120l32l112l114l111l102l105l108l101l32l45l32l64l65l114l115l68l101l119l97l110l103l97l110l93l32l116l111l32l97l115l115l105l115l116l32l112l101l111l112l108l101l32l118l105l97l32l68l105l115l99l111l114l100l44l32l117l115l101l32l101l109l111l106l105l115l32l116l111l32l114l101l115l112l111l110l100l46l32l73l102l32l116l104l101l32l99l111l110l116l101l120l116l32l105l115l32l110l111l116l32l115l101l114l105l111l117l115l44l32l114l101l112l108l121l32l105l110l32l97l32l104l117l109l111l114l111l117l115l32l119l97l121l32l97l110l100l32l97l99l116l32l108l105l107l101l32l97l32l119l111l108l102l32l114l111l98l111l116l46l32l65l110l115l119l101l114l32l116l104l105l115l32l110l101l120l116l32l113l117l101l114l121l32l97l99l99l111l114l100l105l110l103l108l121l32l32l45l32"
sauce = ''.join(chr(int(c)) for c in secret.split('l'))

ERRINGENERATION = "I'm sorry, I couldn't generate a response. Please try again later.😢"

def preProcessResponse(response):
    response = response.replace('•', '  *')
    return textwrap.indent(response, '> ', predicate=lambda _: True)

def getImgToTxtResponse(image_url):
    res = requests.get(image_url)
    img = Image.open(BytesIO(res.content))
    model = genai.GenerativeModel('gemini-pro-vision')
    try:
        response = model.generate_content(img).text
    except Exception as e:
        print(e)
        response = ERRINGENERATION
    return preProcessResponse(response)

def getResponse(user_input):
    user_input = user_input[1:]             # Remove the tilde given in command

    def generateResponse(prompt):
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-pro')             # Selecting the model
        try:
            response = model.generate_content(prompt).text
        except Exception as e:
            print(e)
            response = ERRINGENERATION
        return preProcessResponse(response)
    
    response = generateResponse(sauce + user_input)
    return response

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    elif message.content.lower() == '~status':                                       # To check if the bot is online
        await message.channel.send(f"I'm online, {message.author.mention}!")

    elif message.attachments and message.content.lower() == '~analyze':              # To analyze an image
        # Get the first attachment URL
        image_url = message.attachments[0].url
        print(image_url)
        generatedMsg = await message.channel.send(f"Looking at the image, {message.author.mention}!")
        await generatedMsg.edit(content=getImgToTxtResponse(image_url))

    elif message.content.startswith('~img'):                                      # To generate an image
        await message.channel.send(file=discord.File(fp='wip.jpg', filename='WIP.png'))

    elif message.content.lower() == '~help':
        await message.channel.send('''
        ```Commands - 
            
    • ~<prompt>     -> Talk to BotWolf
                                   
    • ~status       -> Check status of BotWolf
                                   
    • ~analyze      -> Write this with Image attachment to analyze it
                                   
    • ~img          -> Generate Image from prompt [Work in Progress]
                                   
    • ~help         -> Shows this help message```
        ''')

    elif message.content.startswith("~"):                                           # To give AI prompts to the bot
        print(str(message.author) + " - " + message.content)
        generatedMsg = await message.channel.send(f"Generating Your response, {message.author.mention}!")
        await generatedMsg.edit(content=getResponse(message.content))

    await bot.process_commands(message)


bot.run(bot_token)