import discord
from discord.ext import commands
import os

zuda = commands.Bot(command_prefix="~")
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

@zuda.event
async def on_ready() :
    await zuda.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to ~help"))
    print("I am online")

@zuda.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(zuda.latency, 2))}")

@zuda.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@zuda.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)


zuda.run(TOKEN)
