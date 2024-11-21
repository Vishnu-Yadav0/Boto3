import os
import sys
import shutil
os.chdir(r"C:\Users\viva8\Desktop")
list_data=os.listdir()
# print(os.getcwd())
# print(list_data)
# shutil.rmtree("Pynat")
# print(list_data)
# directory = "makedir"
# parent_directory = r"C:\Users\viva8\Desktop\Pynat"
# path=os.path.join(parent_directory,directory)
# os.makedirs(path)

print(os.path.exists(r"C:\Users\viva8\Desktop\Pynat"))
