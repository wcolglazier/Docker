import sys

# Check the current Python version
version = sys.version_info
if version.major == 3 and version.minor == 7 and version.micro == 6:
    print("You are using Python 3.7.6")
else:
    print(f"You are using Python {version.major}.{version.minor}.{version.micro}")
