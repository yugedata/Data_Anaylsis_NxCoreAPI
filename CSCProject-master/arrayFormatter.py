import os

files = []

for file in os.listdir(os.getcwd()):
    if "nx2" in str(file):
        print(str(os.getcwd()) + "\\" + str(file))
        files.append(str(os.getcwd()) + "\\" + str(file))

print("std::string files[" + str(len(files)) + "] = " + str(files).replace("[", "{").replace("]", "}").replace("'", "\"") + ";")
input("Press enter to exit")