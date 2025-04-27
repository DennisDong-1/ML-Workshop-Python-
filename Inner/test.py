import os
# import pandas as pd

# print(os.listdir("data/processed"))
# print(os.getcwd())

# BASE_DIR = r"data\raw"
# files = os.listdir(BASE_DIR)
# print(files)

# FILE_DIR = os.path.join(BASE_DIR, files[0])
# print(FILE_DIR)

# f = open(FILE_DIR, "r")
# print(f)

BASE_DIR2 = r"data\processed"
files = os.listdir(BASE_DIR2)

FILE_DIR2 = os.path.join(BASE_DIR2, files[1])

x = open(FILE_DIR2, "r")

var = x.readlines()

print(var)
# print(x.read())
# x.close()

y = open