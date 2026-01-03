import discord
from discord.ext import commands

from palbot.config import TOKEN
from palbot.storage import init_db

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} slash commands")
    except Exception as e:
        print("Slash sync error:", e)

@bot.event
async def setup_hook():
    init_db()
    await bot.load_extension("palbot.cogs.core")
    await bot.load_extension("palbot.cogs.pals_cog")

bot.run(TOKEN)
