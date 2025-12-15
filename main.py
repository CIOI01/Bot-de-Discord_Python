#import necessary libraries
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#set up logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#create bot instance
bot= commands.Bot(command_prefix='!', intents=intents)

# Define a role for demonstration in Discord server
role = "new_role"

#log when bot is ready
@bot.event
async def on_ready():
    logging.info(f"We are ready to go in, {bot.user.name}")

# Welcome new members 
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}!")

# Respond to messages containing specific words    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "shit" in message.content.lower():
       await message.delete()
       await message.channel.send(f"{message.author.mention}, please watch your language!")
       
    await bot.process_commands(message)   

# Simple command to test bot responsiveness
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

# Command to assign a role to a user
@bot.command()
async def ping(ctx):
    role=discord.utils.get(ctx.guild.roles, name="new_role") 
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, you have been given the role: {role.name}") 
    else:
        await ctx.send(f"Role '{role.name}' not found.")  

# Command that requires a specific role to execute        
@bot.command()
@commands.has_role("new_role")
async def secret(ctx):
    await ctx.send(f"This is a secret command, {ctx.author.mention}!")

# Command to send a direct message to the user
@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"Private message: {msg}")

# Command to reply to a user's message    
@bot.command()
async def reply (ctx):
    await ctx.reply("This is a reply to your message!")   

bot.run(token, log_handler=handler, log_level=logging.DEBUG)   