# This file will initialize the Discord Bot, look for messages starting with the prefix, and call VMController with the command they sent.

import shlex
import subprocess

from Config import ChannelID, CommandPrefixA, CommandPrefixB, DiscordBotToken

if CommandPrefixA is None:
    print("CommandPrefixA is not set. Please set it in Config.py.")
    exit(1)

if CommandPrefixB is None:
    print("CommandPrefixB is not set. Please set it in Config.py.")
    exit(1)

if DiscordBotToken is None:
    print("DiscordBotToken is not set. Please set it in Config.py.")
    exit(1)

def ParseCommands(Command):

    try:
        # Splits the command into tokens while keeping quotes together.
        Tokens = shlex.split(Command)
    except ValueError as e:
        print(f"Parsing error: {e}")
        return []

    Tokens.remove(CommandPrefixA)

    Commands = []
    i = 0
    while i < len(Tokens):
        token = Tokens[i]
        
        if token.startswith(CommandPrefixB):
            Cmd = token[1:]
            Arg = None
            
            if i + 1 < len(Tokens) and not Tokens[i + 1].startswith(CommandPrefixB):
                Arg = Tokens[i + 1]
                i += 2  # Skip both command and its argument
            else:
                i += 1  # Skip just the command (no argument provided)
                
            Commands.append((Cmd, Arg))
        else:
            # Skip any stray tokens that aren't preceded by CommandPrefixB
            i += 1
            
    return Commands

Help = f"""

Management Commands:

{CommandPrefixA} {CommandPrefixB}start - Starts the VirtualBox VM.
{CommandPrefixA} {CommandPrefixB}stop - Stops the VirtualBox VM.
{CommandPrefixA} {CommandPrefixB}pause - Pauses the VirtualBox VM.
{CommandPrefixA} {CommandPrefixB}resume - Resumes the VirtualBox VM.
{CommandPrefixA} {CommandPrefixB}reset - Resets the VirtualBox VM.
{CommandPrefixA} {CommandPrefixB}snapshot \"name\" - Takes a snapshot of the VirtualBox VM with the given name.
{CommandPrefixA} {CommandPrefixB}list snapshots - Lists all snapshots of the VirtualBox VM.
{CommandPrefixA} {CommandPrefixB}restore \"name\" - Restores the VirtualBox VM to the snapshot with the given name.

Input Commands:

{CommandPrefixA} {CommandPrefixB}type \"text\" - Types the given text into the VirtualBox VM.
{CommandPrefixA} {CommandPrefixB}key \"key\" - Presses the given key in the VirtualBox VM.
{CommandPrefixA} {CommandPrefixB}send \"text\" - Types the given text into the VirtualBox VM and presses enter.
{CommandPrefixA} {CommandPrefixB}hold \"key, time\" - Holds the given key in the VirtualBox VM for time seconds.

Notes:

You can use !s normally inside arguments for commands, however to use \"s you have to use \\quote.
Arguments have to be enclosed in quotes with all of them together in the same quotes if they have multiple words. Otherwise only the first word will be used.
- Example: {CommandPrefixA} {CommandPrefixB}type \"Hello World\" will type \"Hello World\" into the VM, but {CommandPrefixA} {CommandPrefixB}type Hello World will only type \"Hello\" with \"World\" being ignored.

"""

try:
    import discord
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
except:
    print("Required Package: discord.py not installed. Please install it using pip or verify your python interpreter.")

@client.event
async def on_ready():
    channel = client.get_channel(ChannelID)
    await channel.send('Relay Ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    Time = str(message.created_at).split(".")[0]
    content = message.content.strip()

    if not content.startswith(CommandPrefixA):
        return

    if not message.channel.id == ChannelID and ChannelID is not None:
        return

    with open("CommandHistory.txt", "a") as f:
        f.write(f" [ DISCORD ] {Time} [{message.author.name}]- {message.content}")

    if content.startswith(f"{CommandPrefixA} !help"):
        await message.channel.send(Help)
        return

    if len(content.split(" ")) < 2:
        await message.channel.send(f"No command provided. Please use {CommandPrefixA} {CommandPrefixB}help for a list of commands.")
        return
    
    Commands = ParseCommands(content)

    for Command, Argument in Commands:
        try:
            Argument = Argument.replace(r"\\quote", '"') if Argument else None
            Result = subprocess.run(["python", "VMController.py", Command, Argument] if Argument else ["python", "VMController.py", Command], capture_output=True, text=True)
            if Result.stderr.strip() != "":
                await message.channel.send(f"An error appears to have occured: {Result.stderr.strip()}")
            await message.channel.send(Result.stdout.strip()) if Result.stdout.strip() else await message.channel.send("No Output.")
        except Exception as e:
            await message.channel.send(f"Error occurred while running command: {Command} | Argument: {Argument}")
            await message.channel.send(f"Error: {e}")

client.run(DiscordBotToken)
    