
import time, random, discord
from discord.ext import commands
from discord import app_commands
from palbot.pals import PALS
from palbot import storage

class Game(commands.Cog):
    def __init__(self,bot): self.bot=bot

    @app_commands.command(name="catch")
    async def catch(self,i:discord.Interaction):
        uid=i.user.id
        storage.ensure(uid)
        coins,last_catch,last_daily=storage.get_user(uid)
        now=int(time.time())
        if now-last_catch<30:
            await i.response.send_message("Cooldown active ⏳",ephemeral=True); return
        pal=random.choice(PALS)
        storage.add_pal(uid,pal)
        storage.update(uid,last_catch=now)
        await i.response.send_message(f"You caught **{pal}**!")

    @app_commands.command(name="inventory")
    async def inventory(self,i:discord.Interaction):
        uid=i.user.id
        storage.ensure(uid)
        pals=storage.get_pals(uid)
        if not pals: await i.response.send_message("No pals yet."); return
        await i.response.send_message(", ".join([p[0] for p in pals]))

    @app_commands.command(name="profile")
    async def profile(self,i:discord.Interaction):
        uid=i.user.id
        storage.ensure(uid)
        coins,_,_=storage.get_user(uid)
        pals=len(storage.get_pals(uid))
        await i.response.send_message(f"Coins: {coins} | Pals: {pals}")

    @app_commands.command(name="daily")
    async def daily(self,i:discord.Interaction):
        uid=i.user.id
        storage.ensure(uid)
        coins,lc,ld=storage.get_user(uid)
        now=int(time.time())
        if now-ld<86400:
            await i.response.send_message("Come back tomorrow ⏳",ephemeral=True); return
        coins+=100
        storage.update(uid,coins=coins,last_daily=now)
        await i.response.send_message("You claimed 100 coins!")
async def setup(bot): await bot.add_cog(Game(bot))
