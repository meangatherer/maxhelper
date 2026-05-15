# Max.Helper — Full Discord Bot Starter (Python)

## Folder Structure

```text
MaxHelper/
│
├── main.py
├── requirements.txt
└── Procfile
```

---

# requirements.txt

```text
discord.py
```

---

# Procfile

```text
worker: python main.py
```

---

# main.py

```python
import os
import random
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# -----------------------------
# BOT READY EVENT
# -----------------------------

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="community activity..."
        )
    )

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands")
    except Exception as e:
        print(e)

# -----------------------------
# MEMBER JOIN EVENT
# -----------------------------

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel

    if channel:
        embed = discord.Embed(
            title="Welcome!",
            description=f"Welcome to **{member.guild.name}**, {member.mention}!",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(url=member.display_avatar.url)

        await channel.send(embed=embed)

# -----------------------------
# BASIC PREFIX COMMANDS
# -----------------------------

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! {latency}ms")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention} 👋")

@bot.command()
async def server(ctx):
    guild = ctx.guild

    embed = discord.Embed(
        title="Server Information",
        color=discord.Color.purple()
    )

    embed.add_field(name="Server Name", value=guild.name, inline=False)
    embed.add_field(name="Members", value=guild.member_count, inline=False)
    embed.add_field(name="Channels", value=len(guild.channels), inline=False)

    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)

    await ctx.send(embed=embed)

@bot.command()
async def analyze(ctx):

    members = ctx.guild.member_count
    channels = len(ctx.guild.channels)

    embed = discord.Embed(
        title="Max.Helper Analysis",
        description="Community scan complete.",
        color=discord.Color.green()
    )

    embed.add_field(name="Members", value=str(members), inline=True)
    embed.add_field(name="Channels", value=str(channels), inline=True)

    if members < 20:
        mood = "Small Growing Community"
    elif members < 100:
        mood = "Active Community"
    else:
        mood = "Large Community"

    embed.add_field(name="Community Mood", value=mood, inline=False)

    await ctx.send(embed=embed)

# -----------------------------
# FUN COMMANDS
# -----------------------------

@bot.command()
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.send(f"🪙 {result}")

@bot.command()
async def rate(ctx, *, thing):
    number = random.randint(1, 100)
    await ctx.send(f"⭐ I rate **{thing}** {number}/100")

# -----------------------------
# MODERATION COMMANDS
# -----------------------------

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)

    msg = await ctx.send(f"🧹 Cleared {amount} messages")
    await msg.delete(delay=3)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"👢 Kicked {member}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 Banned {member}")

# -----------------------------
# SLASH COMMANDS
# -----------------------------

@bot.tree.command(name="ping", description="Check bot latency")
async def slash_ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)

    await interaction.response.send_message(
        f"🏓 Pong! {latency}ms"
    )

@bot.tree.command(name="mood", description="Analyze server mood")
async def mood(interaction: discord.Interaction):

    guild = interaction.guild
    members = guild.member_count

    if members < 20:
        mood_text = "🌱 Small but growing community"
    elif members < 100:
        mood_text = "🔥 Active community"
    else:
        mood_text = "🚀 Large active community"

    embed = discord.Embed(
        title="Community Mood",
        description=mood_text,
        color=discord.Color.orange()
    )

    embed.add_field(name="Members", value=str(members))

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="helpme", description="Show bot commands")
async def helpme(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Max.Helper Commands",
        description="Smart Discord Assistant",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="Utility",
        value="!ping\n!server\n!analyze",
        inline=False
    )

    embed.add_field(
        name="Fun",
        value="!coinflip\n!rate",
        inline=False
    )

    embed.add_field(
        name="Moderation",
        value="!clear\n!kick\n!ban",
        inline=False
    )

    await interaction.response.send_message(embed=embed)

# -----------------------------
# ERROR HANDLING
# -----------------------------

@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission.")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠️ Missing command arguments.")

    else:
        print(error)

# -----------------------------
# START BOT
# -----------------------------

bot.run(TOKEN)
```

---

# Railway Variable

In Railway Variables:

| Name  | Value                  |
| ----- | ---------------------- |
| TOKEN | Your Discord Bot Token |

---

# Important Discord Developer Portal Settings

Enable:

* Message Content Intent
* Server Members Intent

Inside:

Discord Developer Portal → Bot

---

# Run Locally

```bash
python main.py
```

---

# Bot Features Included

✅ Prefix commands
✅ Slash commands
✅ Welcome system
✅ Moderation
✅ Server analysis
✅ Embeds
✅ Community mood system
✅ Error handling
✅ Railway hosting support
✅ Custom status

---

# Future Upgrade Ideas

* AI chatbot
* Dashboard website
* Leveling system
* Reputation system
* Logging system
* Database
* Music system
* Auto moderation
* Analytics panel
* Community heatmap
* AI summaries
