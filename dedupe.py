import os
import glob

dirname = r"E:\Snapchat"

files = glob.glob(os.path.join(dirname, "*.mp4")) + glob.glob(os.path.join(dirname, "*.jpg"))

for f in files:
    if f[-5] == ")" and f[-7] == "(":
        os.remove(f)