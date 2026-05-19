from pathlib import Path
from json import loads

SETTINGS_FILE = Path(__file__).parent.absolute() / "settings.json"

print(SETTINGS_FILE)

with open(SETTINGS_FILE,"r") as file:

    data = file.read()
    
    settings = loads(data)

