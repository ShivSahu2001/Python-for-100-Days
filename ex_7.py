import os

files = os.listdir("ex_7/clutterFolder")
i = 1
for file in files:
    # print(file)
    if file.endswith(".png"):
        print(file)
        os.rename(f"ex_7/clutterFolder/{file}", f"ex_7/clutterFolder/{i}.png" )
        i = i + 1