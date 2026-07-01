import os

path = "assets"

print("Assets folder exists:", os.path.exists(path))

if os.path.exists(path):
    print("Files:", os.listdir(path))
else:
    print("Create assets folder first")