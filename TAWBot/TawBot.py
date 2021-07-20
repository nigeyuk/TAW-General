import discord
import random
import os
from itertools import cycle
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix = '!', help_command=None)

statuses = cycle(['Destiny 2', 'TranceAirWaves.FM', 'With Himself', 'PUBG', 'VSCODE', 'Sheep Simulator', 'Minecraft'])

@bot.event
async def on_ready():
    change_status.start()
    print('I Am Ready Nigel..........')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

@tasks.loop(seconds=300)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(statuses)))

@bot.event
async def on_member_join(member):
    print (f'{member} has joined the server.')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Awesome Listener')
    await bot.add_roles(member, role)

## Linux Server status command
@bot.command()
async def status(ctx):
    file = open(r"serverStatus.txt", "rt")
    content = file.read()
    file.close
    await ctx.message.channel.send(content)

## !ping Command ##
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

## !!8ball command & Answer array ##
@bot.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 '2 million years of evolution and this is the smartest question you ask me?.',
                 'Most Likely, or I could be yanking your chain.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again after I finish my coffee.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cant tell you now, boning your mom.',
                 'Cannot predict now, taking a shit.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook sucks.',
                 'Very doubtful.',
                 "Don't swipe right, it's your cousin.",
                 'Yes, but do it drunk as fuck.',
                 'My sources said no, but they also said Hilary would win.',
                 'Do what Jesus would do, die at the age of 33.',
                 'Who gives a fuck about Szechuan Sauce?!',
                 "Do swipe right, its your HOT cousin.",
                 'Is your mom free tonight?']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

## !clear command - purges the channel of xx messages, Admin role only ##
@bot.command()
@commands.has_role('Admins')
async def clear(ctx, amount : int):
    if amount > 10 :

        await ctx.send('Value must be less than 10')
    
    else : await ctx.channel.purge(limit=amount)

## Error handling for !clear
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete')

## !hello Command TODO change to onjoin greeting ##
@bot.command()
async def hello(ctx):
    msg = f'HI **{ctx.author.mention}** **Welcome To TranceAirWaves.FM** Enjoy your stay, Do you Like Sheep?'
    await ctx.send(msg)

@bot.command()
async def penis(ctx):
    msg = f"Please don't use that command {ctx.author.mention} you may be hurt!"
    await ctx.send(msg)

## !love command ##
@bot.command()
async def love(ctx):
    msg = f'I LOVE **{ctx.author.mention}**, He is **awesome!**'
    await ctx.send(msg)

## !version command, displays an Embed with version info ##
@bot.command(name='version')
async def version(ctx):

    VersionEmbed = discord.Embed(title="Current Version", description="TAWBotty Version 1.0", color=0x00ff00)
    VersionEmbed.add_field(name="Code Version:", value="1.0.3", inline=False)
    VersionEmbed.add_field(name="Date Released", value="July 2021", inline=False)
    VersionEmbed.set_footer(text="TranceAirWaves.FM")
    VersionEmbed.set_author(name="Author: Nigel Smart")

    await ctx.message.channel.send(embed=VersionEmbed)

## Our custom !help command ##
@bot.command()
async def help(ctx):
    msg = f'Hey **{ctx.author.mention}**\n **Here are my available commands**\n **!status** - Displays the current playing track / mix title & links to tune in.\n **!love** - Spread some love :)\n **!hello** - Get a nice warm hello from me.\n **!version** - Shows my code info.\n **!help** - Displays this help message.'
    await ctx.send(msg)

## Kick / Ban ##
@bot.command()
@commands.has_role('Admins')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command()
@commands.has_role('Admins')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

## Unban ##
@bot.command()
@commands.has_role('Admins')
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


## !status command, pulls in the status.txt and sends it to the channel ##
@bot.command(name='tune')
async def tune(ctx):
    file = open(r"status.txt", "rt")
    content = file.read()
    file.close
    msg = f'To Tune In & More information visit **http://www.tranceairwaves.fm**'
    await ctx.message.channel.send(content)
    await ctx.send(msg)

## Run ##
bot.run(TOKEN)
