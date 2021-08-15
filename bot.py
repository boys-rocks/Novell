import discord
from discord.ext import commands
import os
import ast

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", None)
print(DISCORD_TOKEN)
bot = commands.Bot(command_prefix=",", help_command=None)


@bot.event
async def on_ready():
    print("Ready..")
    print("Logged in as: ", bot.user)
    print("Prefix: ", bot.command_prefix)
    print("Latency: ", round(bot.latency * 1000), "ms")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
        else:
            print(f"Unable to load {filename}")


@bot.command()
async def ping(ctx):
    em = discord.Embed(title="Pong!", description=f"{round(bot.latency * 1000)} ms")
    await ctx.send(embed=em)


@bot.command()
async def help(ctx):
    docstring_values = await __parse_docstrings()
    caller_message = ctx.message.content
    if len(caller_message.split()) == 1:
        # The message which called the help command has no params
        message_text = "Available Commands:\n```\n"
        for cog in docstring_values.keys():
            message_text += f"* {cog}"
        message_text += "\n```"
        await ctx.send(message_text)
    else:
        # The command has parameters, search for cog with required name
        cog = caller_message.split()[1]
        try:
            em = discord.Embed()
            em.add_field(name="name", value=cog, inline=False)
            for key, value in docstring_values[cog].items():
                em.add_field(name=key, value=value, inline=False)
            await ctx.send(embed=em)
        except:
            em = discord.Embed(
                title="Error", description=f"Could not find command {cog}"
            )
            await ctx.send(embed=em)


async def __parse_docstring(filename):
    with open(filename, "r") as f:
        contents = f.read()
    module = ast.parse(contents)
    docstring = ast.get_docstring(module)
    if not docstring:
        docstring = "description: <Unknown>\n" + "syntax: <Unknown>"
    return {
        line.split(": ")[0]: "".join(line.split(": ")[1:])
        for line in docstring.split("\n")
        if line.strip()
    }


async def __parse_docstrings():
    values = {}
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            values[filename.strip(".py")] = await __parse_docstring(
                os.path.join("cogs", filename)
            )
    return values


bot.run(DISCORD_TOKEN)
