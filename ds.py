from os import system
from pathlib import Path


# init switcher
switcher = Path("./SWITCH")

if switcher.exists() is False:
    switcher.touch()
    switcher.write_text("PC")

if switcher.read_text() == "PC":
    system("displayswitch.exe 4")
    switcher.write_text("TV")
else:
    system("displayswitch.exe 1")
    switcher.write_text("PC")
