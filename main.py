from __init__ import *

def check_strength(i: str):
  patternTitles = ["Lowercase Letters: ", "Uppercase Letters: ","Numbers: ","Special characters: ","More than 8 characters: "]
  patterns = ["([a-z]*)", "([A-Z])","([0-9]*)",r'''([!\@#\$%\^&\*\(\)~`\-\_=\+\[\{\]\}\|;:'",>/\?])''', "(.{8,})"]
  matches = []
  
  for p in patterns:
    group = re.findall(p, i)
    if(group and group != ""): matches.append("✔️"); continue
    matches.append("❌")

  os.system("cls")
  print(f'''Lowercase Letters: {matches[0]}
Uppercase Letters: {matches[1]}
Numbers: {matches[2]}
Special characters: {matches[3]}
More than 8 characters: {matches[4]}
{i}''', flush=True)

liveStr = ""
while True: 
    char = getch()
    if(char == b"\r"): break
    if(char == b"\x08"): liveStr = liveStr[:-1]

    liveStr += char.decode("utf-8")
    check_strength(liveStr)