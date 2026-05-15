# =========================================
# MAX.HELPER FULL SLASH COMMAND BOT
# =========================================

import os
import random
import datetime
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("TOKEN")

# =========================================
# INTENTS
# =========================================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# =========================================
# BOT SETUP
# =========================================

bot = commands.Bot(
    command_prefix="/",
    intents=intents
)

# =========================================
# READY EVENT
# =========================================

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
        print(f"Synced {len(synced)} commands")

    except Exception as e:
        print(e)

# =========================================
# MEMBER JOIN EVENT
# =========================================

@bot.event
async def on_member_join(member):

    channel = member.guild.system_channel

    if channel:

        embed = discord.Embed(
            title="Welcome!",
            description=f"Welcome {member.mention} to **{member.guild.name}**",
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(url=member.display_avatar.url)

        await channel.send(embed=embed)

# =========================================
# PING
# =========================================

@bot.tree.command(name="ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):

    latency = round(bot.latency * 1000)

    await interaction.response.send_message(
        f"🏓 Pong! {latency}ms"
    )

# =========================================
# SERVER INFO
# =========================================

@bot.tree.command(name="server", description="Show server information")
async def server(interaction: discord.Interaction):

    guild = interaction.guild

    embed = discord.Embed(
        title="Server Information",
        color=discord.Color.green()
    )

    embed.add_field(
        name="Server Name",
        value=guild.name,
        inline=False
    )

    embed.add_field(
        name="Members",
        value=guild.member_count,
        inline=False
    )

    embed.add_field(
        name="Channels",
        value=len(guild.channels),
        inline=False
    )

    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)

    await interaction.response.send_message(embed=embed)

# =========================================
# USER INFO
# =========================================

@bot.tree.command(name="userinfo", description="Show user information")
async def userinfo(
    interaction: discord.Interaction,
    member: discord.Member = None
):

    member = member or interaction.user

    embed = discord.Embed(
        title="User Information",
        color=discord.Color.orange()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(
        name="Username",
        value=member.name,
        inline=False
    )

    embed.add_field(
        name="Joined Server",
        value=member.joined_at.strftime("%d/%m/%Y"),
        inline=False
    )

    embed.add_field(
        name="Account Created",
        value=member.created_at.strftime("%d/%m/%Y"),
        inline=False
    )

    await interaction.response.send_message(embed=embed)

# =========================================
# AVATAR
# =========================================

@bot.tree.command(name="avatar", description="Show user avatar")
async def avatar(
    interaction: discord.Interaction,
    member: discord.Member = None
):

    member = member or interaction.user

    embed = discord.Embed(
        title=f"{member.name}'s Avatar",
        color=discord.Color.blurple()
    )

    embed.set_image(url=member.display_avatar.url)

    await interaction.response.send_message(embed=embed)

# =========================================
# COMMUNITY ANALYSIS
# =========================================

@bot.tree.command(name="analyze", description="Analyze community")
async def analyze(interaction: discord.Interaction):

    guild = interaction.guild

    members = guild.member_count
    channels = len(guild.channels)

    if members < 20:
        mood = "🌱 Growing Community"

    elif members < 100:
        mood = "🔥 Active Community"

    else:
        mood = "🚀 Large Community"

    embed = discord.Embed(
        title="Community Analysis",
        description="AI community scan completed.",
        color=discord.Color.purple()
    )

    embed.add_field(
        name="Members",
        value=members
    )

    embed.add_field(
        name="Channels",
        value=channels
    )

    embed.add_field(
        name="Community Mood",
        value=mood,
        inline=False
    )

    await interaction.response.send_message(embed=embed)

# =========================================
# MOOD
# =========================================

@bot.tree.command(name="mood", description="Analyze server mood")
async def mood(interaction: discord.Interaction):

    moods = [
        "🔥 Highly Active",
        "😎 Chill Community",
        "🌙 Quiet Right Now",
        "🚀 Growing Fast",
        "🎉 Event Energy"
    ]

    embed = discord.Embed(
        title="Community Mood",
        description=random.choice(moods),
        color=discord.Color.gold()
    )

    await interaction.response.send_message(embed=embed)

# =========================================
# COINFLIP
# =========================================

@bot.tree.command(name="coinflip", description="Flip a coin")
async def coinflip(interaction: discord.Interaction):

    result = random.choice(["Heads", "Tails"])

    await interaction.response.send_message(
        f"🪙 {result}"
    )

# =========================================
# RATE
# =========================================

@bot.tree.command(name="rate", description="Rate something")
async def rate(
    interaction: discord.Interaction,
    thing: str
):

    number = random.randint(1, 100)

    await interaction.response.send_message(
        f"⭐ I rate **{thing}** {number}/100"
    )

# =========================================
# 8BALL
# =========================================

@bot.tree.command(name="8ball", description="Ask the magic 8ball")
async def eightball(
    interaction: discord.Interaction,
    question: str
):

    responses = [
        "Yes",
        "No",
        "Maybe",
        "Definitely",
        "Probably not",
        "Absolutely",
        "I don't think so"
    ]

    await interaction.response.send_message(
        f"🎱 Question: {question}\nAnswer: {random.choice(responses)}"
    )

# =========================================
# POLL
# =========================================

@bot.tree.command(name="poll", description="Create a poll")
async def poll(
    interaction: discord.Interaction,
    question: str
):

    embed = discord.Embed(
        title="📊 Poll",
        description=question,
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=embed)

    message = await interaction.original_response()

    await message.add_reaction("👍")
    await message.add_reaction("👎")

# =========================================
# SUGGESTION
# =========================================

@bot.tree.command(name="suggest", description="Send suggestion")
async def suggest(
    interaction: discord.Interaction,
    suggestion: str
):

    embed = discord.Embed(
        title="💡 New Suggestion",
        description=suggestion,
        color=discord.Color.green()
    )

    embed.set_footer(
        text=f"Suggested by {interaction.user}"
    )

    await interaction.response.send_message(embed=embed)

# =========================================
# REMINDER
# =========================================

@bot.tree.command(name="remind", description="Simple reminder")
async def remind(
    interaction: discord.Interaction,
    reminder: str
):

    await interaction.response.send_message(
        f"⏰ Reminder saved: {reminder}"
    )

# =========================================
# CLEAR
# =========================================

@bot.tree.command(name="clear", description="Delete messages")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(
    interaction: discord.Interaction,
    amount: int
):

    await interaction.channel.purge(limit=amount)

    await interaction.response.send_message(
        f"🧹 Cleared {amount} messages",
        ephemeral=True
    )

# =========================================
# KICK
# =========================================

@bot.tree.command(name="kick", description="Kick member")
@app_commands.checks.has_permissions(kick_members=True)
async def kick(
    interaction: discord.Interaction,
    member: discord.Member,
    reason: str = None
):

    await member.kick(reason=reason)

    await interaction.response.send_message(
        f"👢 Kicked {member}"
    )

# =========================================
# BAN
# =========================================

@bot.tree.command(name="ban", description="Ban member")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(
    interaction: discord.Interaction,
    member: discord.Member,
    reason: str = None
):

    await member.ban(reason=reason)

    await interaction.response.send_message(
        f"🔨 Banned {member}"
    )

# =========================================
# HELP
# =========================================

@bot.tree.command(name="helpme", description="Show all commands")
async def helpme(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Max.Helper Commands",
        description="AI Community Assistant",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="Utility",
        value="""
/ping
/server
/userinfo
/avatar
/analyze
/mood
/remind
""",
        inline=False
    )

    embed.add_field(
        name="Fun",
        value="""
/coinflip
/rate
/8ball
/poll
""",
        inline=False
    )

    embed.add_field(
        name="Moderation",
        value="""
/clear
/kick
/ban
""",
        inline=False
    )

    await interaction.response.send_message(embed=embed)

# =========================================
# ERROR HANDLING
# =========================================

@bot.event
async def on_command_error(ctx, error):

    print(error)

# =========================================
# START BOT
# =========================================

bot.run(TOKEN)
