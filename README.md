# Regex Password Strength Tester

## Usage
__This can be used as a script or a module.__

### Usage as Script
Simply run `__*python main.py*__` and the script will install all dependencies and run

### Usage as module
Put the `\__init.py__` file and `main.py` file in your project put this line in your imports:

*`from main import check_strength`*

Now you can pass your password into that function and something like [1,0,0,0,0] will be returned.
Each number in this list represents a test:
* Index 0 - Password has lowercase letters
* Index 1 - Password has uppercase letters
* Index 2 - Password has numbers
* Index 3 - Password has special characters
* Index 4 - Password has 8 or more characters