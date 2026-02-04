
import discord
from discord.ext import commands
from palbot.config import TOKEN
from palbot.storage import init_db

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync()

@bot.event
async def setup_hook():
    init_db()
    await bot.load_extension("palbot.cogs.game")

bot.run(TOKEN)
