import os

pipType = "pip3"
libs = [f"{pipType} install beautifulsoup4"]

for i in libs:
    os.popen(i).read()
    pass


