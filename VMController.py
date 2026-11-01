# This file will be run with it's arguments being the commands and arguments that the relays send to it. It will then execute the commands and return the output to the relay that sent it.

from Config import VBoxManagePath, VirtualBoxVMName
import subprocess
import time

if VBoxManagePath is None:
    print("VBoxManagePath is not set. Please set it in Config.py.")
    exit(1)

if VirtualBoxVMName is None:
    print("VirtualBoxVMName is not set. Please set it in Config.py.")
    exit(1)

KeyMap = {
    "a": ("1e", "9e"),                  # A
    "b": ("30", "b0"),                  # B
    "c": ("2e", "ae"),                  # C
    "d": ("20", "a0"),                  # D
    "e": ("12", "92"),                  # E
    "f": ("21", "a1"),                  # F
    "g": ("22", "a2"),                  # G
    "h": ("23", "a3"),                  # H
    "i": ("17", "97"),                  # I
    "j": ("24", "a4"),                  # J
    "k": ("25", "a5"),                  # K
    "l": ("26", "a6"),                  # L
    "m": ("32", "b2"),                  # M
    "n": ("31", "b1"),                  # N
    "o": ("18", "98"),                  # O
    "p": ("19", "99"),                  # P
    "q": ("10", "90"),                  # Q
    "r": ("13", "93"),                  # R
    "s": ("1f", "9f"),                  # S
    "t": ("14", "94"),                  # T
    "u": ("16", "96"),                  # U
    "v": ("2f", "af"),                  # V
    "w": ("11", "91"),                  # W
    "x": ("2d", "ad"),                  # X
    "y": ("15", "95"),                  # Y
    "z": ("2c", "ac"),                  # Z
    "1": ("02", "82"),                  # 1
    "2": ("03", "83"),                  # 2
    "3": ("04", "84"),                  # 3
    "4": ("05", "85"),                  # 4
    "5": ("06", "86"),                  # 5
    "6": ("07", "87"),                  # 6
    "7": ("08", "88"),                  # 7
    "8": ("09", "89"),                  # 8
    "9": ("0a", "8a"),                  # 9
    "0": ("0b", "8b"),                  # 0
    ",": ("33", "b3"),                  # Comma
    ".": ("34", "b4"),                  # Period
    "/": ("35", "b5"),                  # Forward Slash
    ";": ("27", "a7"),                  # Semicolon
    "'": ("28", "a8"),                  # Apostrophe
    "[": ("1a", "9a"),                  # Left Bracket
    "]": ("1b", "9b"),                  # Right Bracket
    "\\": ("2b", "ab"),                  # Backslash
    "-": ("0c", "8c"),                  # Minus
    "=": ("0d", "8d"),                  # Equals
    "`": ("29", "a9"),                  # Backtick
    "!": ("2a", "02", "82", "aa"),      # Exclamation Mark
    "@": ("2a", "03", "83", "aa"),      # At Sign
    "#": ("2a", "04", "84", "aa"),      # Hash
    "$": ("2a", "05", "85", "aa"),      # Dollar Sign
    "%": ("2a", "06", "86", "aa"),      # Percent Sign
    "^": ("2a", "07", "87", "aa"),      # Caret
    "&": ("2a", "08", "88", "aa"),      # Ampersand
    "*": ("2a", "09", "89", "aa"),      # Asterisk
    "(": ("2a", "0a", "8a", "aa"),      # Left Parenthesis
    ")": ("2a", "0b", "8b", "aa"),      # Right Parenthesis
    "_": ("2a", "0c", "8c", "aa"),      # Underscore
    "+": ("2a", "0d", "8d", "aa"),      # Plus
    "{": ("2a", "1a", "9a", "aa"),      # Left Brace
    "}": ("2a", "1b", "9b", "aa"),      # Right Brace
    "|": ("2a", "2b", "ab", "aa"),      # Vertical Bar
    ":": ("2a", "27", "a7", "aa"),      # Colon
    '"': ("2a", "28", "a8", "aa"),      # Quotation Mark
    "~": ("2a", "29", "a9", "aa"),      # Tilde
    "<": ("2a", "33", "b3", "aa"),      # Less Than
    ">": ("2a", "34", "b4", "aa"),      # Greater Than
    "?": ("2a", "35", "b5", "aa"),      # Question Mark
    "escape": ("01", "81"),
    "delete": ("e0", "53", "e0", "d3"),
    "insert": ("e0", "52", "e0", "d2"),
    "home": ("e0", "47", "e0", "c7"),
    "end": ("e0", "4f", "e0", "cf"),
    "tab": ("0f", "8f"),
    "caps lock": ("3a", "ba"),
    "shift": ("2a", "aa"),
    "control": ("1d", "9d"),
    "super/windows": ("e0", "5b", "e0", "db"),
    "alt": ("38", "b8"),
    "enter": ("1c", "9c"),
    "backspace": ("0e", "8e"),
    "space": ("39", "b9"),
    "up": ("e0", "48", "e0", "c8"),
    "down": ("e0", "50", "e0", "d0"),
    "left": ("e0", "4b", "e0", "cb"),
    "right": ("e0", "4d", "e0", "cd"),

    # Aliases

    "esc": ("01", "81"),
    "del": ("e0", "53", "e0", "d3"),
    "ins": ("e0", "52", "e0", "d2"),
    "ctrl": ("1d", "9d"),
    "win": ("e0", "5b", "e0", "db"),
    "windows": ("e0", "5b", "e0", "db"),
    "super": ("e0", "5b", "e0", "db"),
    "meta": ("e0", "5b", "e0", "db"),
}

def GetStatus():
    Lines = VBoxManage(["showvminfo", VirtualBoxVMName]).splitlines()
    for Line in Lines:
        if "State:" in Line:
            return Line.split("State:")[1].strip().split("(")[0].strip()
        
def VBoxManage(Commands):
    Result = subprocess.run([VBoxManagePath] + Commands, capture_output=True, text=True)
    return Result.stdout.strip() if Result.stdout.strip() else Result.stderr.strip() if Result.stderr.strip() else "No output."

def StartVM():
    if GetStatus() == "running" or GetStatus() == "paused":
        return f"{VirtualBoxVMName} is already running."
    return VBoxManage(["startvm", VirtualBoxVMName])

def StopVM():
    if GetStatus() != "running" and GetStatus() != "paused":
        return f"{VirtualBoxVMName} is not running."
    return VBoxManage(["controlvm", VirtualBoxVMName, "shutdown"])

def PauseVM():
    if GetStatus() != "running":
        return f"{VirtualBoxVMName} is not running."
    return VBoxManage(["controlvm", VirtualBoxVMName, "pause"])

def ResumeVM():
    if GetStatus() != "paused":
        return f"{VirtualBoxVMName} is not paused."
    return VBoxManage(["controlvm", VirtualBoxVMName, "resume"])

def ResetVM():
    if GetStatus() != "running" and GetStatus() != "paused":
        return f"{VirtualBoxVMName} is not running."
    return VBoxManage(["controlvm", VirtualBoxVMName, "reset"])

def SnapshotVM(Argument):
    if Argument is None:
        return "No snapshot name provided. Please provide a snapshot name after the command."
    return VBoxManage(["snapshot", VirtualBoxVMName, "take", Argument])

def RestoreVM(Argument):
    if Argument is None:
        return "No snapshot name provided. Please provide a snapshot name after the command."
    if GetStatus() == "running" or GetStatus() == "paused":
        Output = VBoxManage(["controlvm", VirtualBoxVMName, "poweroff"])
        Output += VBoxManage(["snapshot", VirtualBoxVMName, "restore", Argument])
        Output += VBoxManage(["startvm", VirtualBoxVMName])
    else:
        Output = VBoxManage(["snapshot", VirtualBoxVMName, "restore", Argument])
    return Output

def ListInfo(Argument):
    if Argument is None:
        return "No list provided."
    match Argument:
        case "snapshots":
            return VBoxManage(["snapshot", VirtualBoxVMName, "list"])
        case _:
            return "Invalid list."

def TypeInVM(Argument):
    if GetStatus() != "running":
        return f"{VirtualBoxVMName} is not running."
    if Argument is None:
        return "No text provided. Please provide text after the command."
    return VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputstring", Argument])

def PressKeyInVM(Argument):
    if GetStatus() != "running":
        return f"{VirtualBoxVMName} is not running."
    if Argument is None:
        return "No key provided. Please provide a key after the command."
    if Argument.lower() not in KeyMap:
        return f"Unknown key: {Argument}. Please provide a valid key."
    Scancodes = KeyMap[Argument.lower()]
    return VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputscancode"] + list(Scancodes))

def SendTextToVM(Argument):
    if GetStatus() != "running":
        return f"{VirtualBoxVMName} is not running."
    if Argument is None:
        return "No text provided. Please provide text after the command."
    Output = "1. " + VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputstring", Argument])
    Output += "\n2. " + VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputscancode", "1c", "9c"])
    return Output

def SendComboToVM(Argument):
    if Argument is None:
        return "No combo provided."
    PressScancodes = []
    ReleaseScancodes = []
    CombinedScancodes = []
    Keys = Argument.split("+")
    for Key in Keys:
        if Key in KeyMap:
            Scancodes = KeyMap[Key]
            if len(Scancodes) == 2:
                PressScancodes.append(Scancodes[0])
                ReleaseScancodes.append(Scancodes[1])
            else:
                PressScancodes.append(Scancodes[0])
                PressScancodes.append(Scancodes[1])
                ReleaseScancodes.append(Scancodes[2])
                ReleaseScancodes.append(Scancodes[3])
        else:
            print(f"Key not found, {Key}")
    CombinedScancodes = PressScancodes + ReleaseScancodes
    Command = ["controlvm", VirtualBoxVMName, "keyboardputscancode"] + CombinedScancodes
    return VBoxManage(Command)

def HoldKeyInVM(Argument):
    if GetStatus() != "running":
        return "VM is not running."
    if not Argument:
        return "No key and time provided."
    try:
        Key = Argument.split(", ")[0]
        Time = Argument.split(", ")[1]
    except:
        return("Key or time missing or arguments were provided with incorrect syntax. It should be \"Key, Time\"")
    if not Key or not Time:
        return "Please provide a key to press or time to press it for."
    Key = Key.lower()
    try:
        Time = int(Time)
    except:
        return "Invalid Time."
    if Time > 30:
        return "Please provide a time shorter than 30 seconds."
    if not Key in KeyMap:
        return "Invalid Key."
    Scancodes = KeyMap[Key]
    if len(Scancodes) == 2:
        VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputscancode", Scancodes[0]])
        time.sleep(Time)
        VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputscancode", Scancodes[1]])
    if len(Scancodes) == 4:
        VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputscancode", Scancodes[0]])
        VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputscancode", Scancodes[1]])
        time.sleep(Time)
        VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputscancode", Scancodes[2]])
        VBoxManage(["controlvm", VirtualBoxVMName, "keyboardputscancode", Scancodes[3]])
    return f"Successfully held key \"{Key}\" for {Time} seconds."

    


def RunCommand(Command, Argument=None):
    match Command:
        case "list":
            return ListInfo(Argument)
        case "start":
            return StartVM()
        case "stop":
            return StopVM()
        case "pause":
            return PauseVM()
        case "resume":
            return ResumeVM()
        case "reset":
            return ResetVM()
        case "snapshot":
            return SnapshotVM(Argument)
        case "restore":
            return RestoreVM(Argument)
        case "type":
            return TypeInVM(Argument)
        case "key":
            return PressKeyInVM(Argument)
        case "send":
            return SendTextToVM(Argument)
        case "combo":
            return SendComboToVM(Argument)
        case "hold":
            return HoldKeyInVM(Argument)
        case _:
            return f"Unknown command: {Command}"

if __name__ == "__main__":
    import sys
    command = sys.argv[1] if len(sys.argv) > 1 else None
    argument = sys.argv[2] if len(sys.argv) > 2 else None
    if not command:
        print("No command provided. Did you accidentally run this without going through a relay?")
        sys.exit(1)
    output = RunCommand(command, argument)
    if output == None:
        print("No output.")
    else:
        print(output)
