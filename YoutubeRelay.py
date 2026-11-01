# This file will initialize the Pytchat library, look for messages starting with the prefix, and call VMController with the command they sent.

import shlex
from Config import YouTubeLiveChatID, CommandPrefixA, CommandPrefixB
import subprocess

if YouTubeLiveChatID is None:
    print("YouTubeLiveChatID is not set. Please set it in Config.py.")
    exit(1)

if CommandPrefixA is None:
    print("CommandPrefixA is not set. Please set it in Config.py")
    exit(1)

if CommandPrefixB is None:
    print("CommandPrefixB is not set. Please set it in Config.py")
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

try:
    import pytchat
except:
    print("Pytchat is not installed. Please install it with pip and try again.")
    exit(1)

try:
    print(f"Connecting to YouTube live chat with ID: {YouTubeLiveChatID}")
    Chat = pytchat.create(video_id=YouTubeLiveChatID)
    print("Connected to YouTube live chat.")
except Exception as e:
    print(f"Failed to connect to YouTube live chat, perhaps you forgot to set the YouTubeLiveChatID variable in Config.py? Error: {e}")
    exit(1)


while Chat.is_alive():
    for Message in Chat.get().sync_items():
        if Message.message.startswith(CommandPrefixA):
            with open("CommandHistory.txt", "a") as f:
                f.write(f" [ YOUTUBE ] {Message.datetime} [{Message.author.name}]- {Message.message}")

            Commands = ParseCommands(Message.message)
            
            for Command, Argument in Commands:
                try:
                    Argument = Argument.replace(r"\\quote", '"') if Argument else None
                    Result = subprocess.run(["python", "VMController.py", Command, Argument] if Argument else ["python", "VMController.py", Command], capture_output=True, text=True)
                    if Result.stderr.strip() != "":
                        print(f"An error appears to have occured: {Result.stderr.strip()}")
                    print(Result.stdout.strip()) if Result.stdout.strip() else print("No Output.")
                except Exception as e:
                    print(f"Error occurred while running command: {Command} | Argument: {Argument}")
                    print(f"Error: {e}")
