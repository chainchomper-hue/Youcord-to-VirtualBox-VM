# This file will contain all the variables that are used in the other files. This is to make it easier to change them in one place instead of having to change them in multiple files and also mitigate secrets like the bot token accidentally being left in and pushed to GitHub.

# - Discord Bot Variables
DiscordBotToken = None  # Replace with your Discord bot token - Getting the bot token is a process that will take too long to explain here, you can however google "how to create a discord bot" and follow those instructions.
ChannelID = None  # Replace with your Discord channel ID that the bot will recieve commands from. Leave as None to accept commands from all channels. To get your channel ID, you will need to enable developer mode in Discord. Once you have done that, you can right click on the channel and click "Copy ID". This will copy the channel ID to your clipboard.

# - YouTube Live Chat Variables
YouTubeLiveChatID = None  # Replace with your YouTube live stream ID or URL, it is the video identifier found in the URL. For example, if your live stream URL is https://www.youtube.com/watch?v=abc123, you would replace None with "abc123" or the full URL. If you are not using the YouTube relay, you can leave this as None.

# - VirtualBox Variables - Required for both relays.
VirtualBoxVMName = None  # Replace with your VirtualBox VM name
VBoxManagePath = None  # Replace with the path to VBoxManage on your system, this is usually the same place virtualbox is installed. For example, on Windows, it is usually "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", and on Linux, it is usually "/usr/bin/VBoxManage". It is VERY important that this is set correctly, as the program will not work if it isn't.

# - General Variables

CommandPrefixA = "!vm" # The prefix that the relays will look for at the start of a message to determine if it should be treated as a command. Messages that do not start with this prefix will be ignored.
CommandPrefixB = "!" # The prefix that the relays will look for to determine if the following word is a command. For example, if you set this to "!", then the command "!start" would be treated as a command, but "start" would not. This is only required due to the program needing a way to differentiate between a command and an argument.

# Replace None with the value you want to use with "" around it. For example, if your Discord bot token is "abc123", you would change the line to: 

# DiscordBotToken = "abc123"

# Each variable has is followed by a comment explaining what it is and how to find it. Please read the comments carefully before editing the variables.

# DiscordBotToken + ChannelID and YouTubeLiveChatID are only required for their respective relay files. If you are not using one of the relays, you can leave the variable as None. For example, if you are only using the Discord relay, you can leave YouTubeLiveChatID as None and Vice versa.

if __name__ == "__main__":
    print("This file is not meant to be run directly. Please run the relay files instead.")
    exit(1)