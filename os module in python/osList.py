import os

folders  = os.listdir("data")

# print(folders)
# print("Current Directory: ", os.getcwd())
# os.chdir("/Users")
# print("Current Directory: ", os.getcwd())

# os.remove(f"data/Tutorial 10/tutorial.md")
os.rmdir(f"data/Tutorial 10")




# for i in folders:
    # print(i)
    # print(os.listdir(f"data/{i}"))