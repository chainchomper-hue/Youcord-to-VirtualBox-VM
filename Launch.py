# This file will be run with either --discord, --youtube, --history, --all or multiple as arguments. It will then start the appropriate relay(s) based on the arguments provided.

import platform
import sys
import subprocess

Terminal = None

Arguments = sys.argv[1:]


for arg in Arguments:
    if arg not in ["--discord", "-d", "--youtube", "-y", "--history", "-h", "--help", "-?" "--all", "-a"]:
        print(f"Invalid argument: {arg}. Please check the usage information with -? or --help.")
        exit(1)

for arg in Arguments:
    if arg == "--help" or arg == "-?":
        print("""
Usage:

-? / --help: Show this help message.
-d / --discord: Start the Discord relay.
-y / --youtube: Start the YouTube relay.
-h / --history: Start the command history display.
-a / --all: Start everything. (Discord, YouTube, and command history display)
""")
        exit(0)


if platform.system() == "Windows":
    Terminal = "cmd.exe"
elif platform.system() == "Linux":
    pass
elif platform.system() == "Darwin":
    Terminal = "open"
else:
    print("Unsupported operating system. Please use Windows, Linux, or macOS.")
    sys.exit(1)

if len(sys.argv) < 2:
    print("No arguments provided. Please check usage information with --help, or -?")
    sys.exit(1)

if Terminal == None:
    PotentialTerminals = ["gnome-terminal", "konsole", "xfce4-terminal", "lxterminal", "xterm"]
    for term in PotentialTerminals:
        try:
            subprocess.run(["which", term], check=True)
            Terminal = term
            print(f"Detected terminal: {Terminal}")
        except:
            print(f"{term} not found. Trying next terminal...")

if not Terminal:
    print("No supported terminal found. Please install one of the following terminals: gnome-terminal, konsole, xfce4-terminal, lxterminal, xterm. OR manually open the relays in a terminal of your choice.")
    exit(1)

if Terminal == "cmd.exe":
    if "--all" in Arguments or "-a" in Arguments:
        subprocess.Popen(["start", "cmd", "/k", "python", "DiscordRelay.py"], shell=True)
        subprocess.Popen(["start", "cmd", "/k", "python", "YoutubeRelay.py"], shell=True)
        subprocess.Popen(["start", "cmd", "/k", "python", "CommandHistoryDisplay.py"], shell=True)
        exit(0)
    
    if "--discord" in Arguments or "-d" in Arguments:
        subprocess.Popen(["start", "cmd", "/k", "python", "DiscordRelay.py"], shell=True)
    if "--youtube" in Arguments or "-y" in Arguments:
        subprocess.Popen(["start", "cmd", "/k", "python", "YoutubeRelay.py"], shell=True)
    if "--history" in Arguments or "-h" in Arguments:
        subprocess.Popen(["start", "cmd", "/k", "python", "CommandHistoryDisplay.py"], shell=True)
elif Terminal == "open":
    if "--all" in Arguments or "-a" in Arguments:
        subprocess.Popen(["open", "-a", "Terminal", "DiscordRelay.py"])
        subprocess.Popen(["open", "-a", "Terminal", "YoutubeRelay.py"])
        subprocess.Popen(["open", "-a", "Terminal", "CommandHistoryDisplay.py"])
        exit(0)
    if "--discord" in Arguments or "-d" in Arguments:
        subprocess.Popen(["open", "-a", "Terminal", "DiscordRelay.py"])
    if "--youtube" in Arguments or "-y" in Arguments:
        subprocess.Popen(["open", "-a", "Terminal", "YoutubeRelay.py"])
    if "--history" in Arguments or "-h" in Arguments:
        subprocess.Popen(["open", "-a", "Terminal", "CommandHistoryDisplay.py"])
else:
    if "--all" in Arguments or "-a" in Arguments:
        subprocess.Popen([Terminal, "-e", "python3 DiscordRelay.py"])
        subprocess.Popen([Terminal, "-e", "python3 YoutubeRelay.py"])
        subprocess.Popen([Terminal, "-e", "python3 CommandHistoryDisplay.py"])
        exit(0)
    if "--discord" in Arguments or "-d" in Arguments:
        subprocess.Popen([Terminal, "-e", "python3 DiscordRelay.py"])
    if "--youtube" in Arguments or "-y" in Arguments:
        subprocess.Popen([Terminal, "-e", "python3 YoutubeRelay.py"])
    if "--history" in Arguments or "-h" in Arguments:
        subprocess.Popen([Terminal, "-e", "python3 CommandHistoryDisplay.py"])

if not ("--discord" in Arguments or "--youtube" in Arguments or "--history" in Arguments or "--all" in Arguments):
    print("No valid arguments provided. Please check usage information with -? or --help.")
    exit(1)

    
