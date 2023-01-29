#|/usr/bin/env python3
import subprocess
import platform

LINUX_PREMAKE = "tools/lpremake5"
MAC_PREMAKE = "premake/premake5"
WIN_PREMAKE = "premake/premake5.exe"
SLN = "vs2022"
print("this is the gensln command!")
if platform.system() == "Linux":
    PREMAKE = LINUX_PREMAKE
elif platform.system() == "Darwin":
    PREMAKE = MAC_PREMAKE
elif platform.system() == "Windows":
    PREMAKE = WIN_PREMAKE
subprocess.call([PREMAKE, SLN])