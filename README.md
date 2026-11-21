# Youcord to VirtualBox VM

This is a program that allows your discord server members or YouTube live stream viewers to control a VirtualBox VM by sending commands through the chat.

## Setup

- Make sure you have Python 3.10 or higher installed on your system.
- Make sure you have VirtualBox installed on your system and that you have a VM set up that you want to control.
- Make sure you have a Discord Bot and/or YouTube Account with the ability to go live depending on which relays you want to use.
- Use pip to install the required dependencies using the following command:
```
"Way to run pip on your system" install -r requirements.txt
```

## VirtualBox Setup

- Make sure you have VirtualBox installed on your system, and that you have a VM set up that you want to control.
- Inside the Config.py file, set the VirtualBoxVMName variable to the name of your VM.
- Inside the Config.py file, set the VBoxManagePath variable to the path of your VBoxManage executable. This is usually located in the VirtualBox installation directory.
- Make sure your VM is set to the US keyboard layout, as VBoxManage maps its keyboardputstring command to the US keyboard layout. If your VM is set to a different keyboard layout, the keys may not be mapped correctly.

## Discord Bot Setup

- Create a Discord Bot
  - If you don't know how to, you can follow this guide: https://discordpy.readthedocs.io/en/stable/discord.html
- Make sure to enable the "Message Content Intent" in the bot settings.
- invite it to your server with the appropriate permissions.
  - Read Messages/View Channels
  - Send Messages
  - Read Message History
- Paste the bot token into the config.json file. - Make sure to not accidentally leak your bot token or the completed config.json file, as it can be used to take control of your bot and destroy your server if it has administrator privileges.
- Optionally you can set a channel ID in the config.json file to restrict the bot to only listen to commands from that channel. Otherwise the bot will listen to commands from all channels.
- To find the Channel ID, go to the developer tab in your Discord settings, enable developer mode, and right click the channel you want to use and select "Copy ID".

## YouTube Live Stream Setup

- Make sure you have a YouTube account that is eligible to go live.
- Go to the Go Live section of your YouTube Studio and create a new live stream.
- Before you start streaming through your preferred software, take the video ID in the URL and paste it into the config.json file.
- While setting up the live stream or testing the relay, make sure the stream is set to "Unlisted" as if the stream is private, the relay will be unable to connect to the chat.

## Usage

- Run Launch.py with the appropriate arguments to start the relays and/or the command history display. Use -? or --help for usage information.
- You can also run the files directly.

## AI Disclaimer

- Only inline suggestions ( VSCode Feature powered by GitHub Copilot ) were used to help write code for this project.
- The way inline suggestions works is just a fancy autocomplete, and most of the suggestions were what I would have written myself.
- Other AI tools were only used to check for bugs and help with figuring out how to implement difficult logic.
- I understand that you may have a much lower bar for what you might consider "Vibe Coded AI Slop" but personally I don't think so.