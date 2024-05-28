import os
import google.generativeai as genai
import textwrap
import discord
from discord.ext import commands
from IPython.display import Markdown
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('GEMINI_API_KEY')
bot_token = os.getenv('DISCORD_BOT_TOKEN')

secret = "89-111-117-32-97-114-101-32-66-111-116-87-111-108-102-44-32-99-114-101-97-116-101-100-32-98-121-32-65-114-115-100-101-101-112-32-116-111-32-97-115-115-105-115-116-32-112-101-111-112-108-101-32-118-105-97-32-68-105-115-99-111-114-100-44-32-117-115-101-32-101-109-111-106-105-115-32-116-111-32-114-101-115-112-111-110-100-46-32-73-102-32-116-104-101-32-99-111-110-116-101-120-116-32-105-115-32-110-111-116-32-115-101-114-105-111-117-115-44-32-114-101-112-108-121-32-105-110-32-97-32-104-117-109-111-114-111-117-115-32-119-97-121-32-97-110-100-32-97-99-116-32-108-105-107-101-32-97-32-119-111-108-102-46-32-65-110-115-119-101-114-32-116-104-105-115-32-110-101-120-116-32-113-117-101-114-121-32-97-99-99-111-114-100-105-110-103-108-121-32-32-45-32"

sauce = ''.join(chr(int(c)) for c in secret.split('-'))

def getResponse(user_input):
    user_input = user_input[1:]
    print(user_input)

    def generateResponse(prompt):
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-1.0-pro')
        response = model.generate_content(prompt).text
        response = response.replace('•', '  *')
        return textwrap.indent(response, '> ', predicate=lambda _: True)
    
    
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
    
    elif message.content.lower() == '~status':
        await message.channel.send(f"I'm online, {message.author.mention}!")

    elif message.content.startswith("~"):
        await message.channel.send(f"Generating Your response, {message.author}!")
        await message.channel.send(getResponse(message.content))

    await bot.process_commands(message)


bot.run(bot_token)