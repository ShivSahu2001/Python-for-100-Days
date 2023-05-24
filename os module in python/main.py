import os

if(not os.path.exists("data")):
    os.mkdir("dataPython")

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")