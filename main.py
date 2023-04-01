from __init__ import * # Initializer script that imports modules and defined OS-specific custom functions

# Function that does the regex matching to determine password strength
def check_strength(i: str):
  # Patterns to detect lowercase and uppercase alphabets, numbers, special characters as well as if the string is longer than 8 characters
  patterns = ["([a-z])", "([A-Z])","([0-9])",r'''([!\@#\$%\^&\*\(\)~`\-\_=\+\[\{\]\}\|;:'",>/\?])''', "(.{8,})"]
  matches = [] # Initialize list that shows matches
  
  for p in patterns: # Loop over strength determination criteria patterns
    group = re.findall(p, i) # Find all instances of pattern(match does not work reliably, i tried)
    if(group and group != ""): matches.append("✔️"); continue # If the patterns matches anwhere, append a tick mark emoji to matches and continue so that the x emoji dosnt get appended
    matches.append("❌") # If pattern not matched(and thus this line not skipped), append a cross-emoji to mathces

  if(__name__ != "__main__"): return [1 if m == "✔️" else 0 for m in matches] # Return a list of zeros and ones instead of emojis if file is being used as a module
  clear_screen() # Clear previous print of password report
  # Print password report with titles and respective emojis
  print(f'''Lowercase Letters: {matches[0]}
Uppercase Letters: {matches[1]}
Numbers: {matches[2]}
Special characters: {matches[3]}
More than 8 characters: {matches[4]}
{i}
{i[-1]}''', flush=True)

if (__name__ == "__main__"): # Only display user interface if file is not being used as a module
  liveStr = "" # Initialize input string
  while True: # Endless Loop
      char = getch() # Wait for and get character from terminal
      if(to_byteStr(char) == enter_code): break # if user presses enter key, exit
      if(to_byteStr(char) == backspace_code): # if user presses backspace
          liveStr = liveStr[:-1] # Remove last character of string(currently buggy)

      liveStr += decode(char) # Append latest character to input string
      check_strength(liveStr) # Generate and show password strength report
