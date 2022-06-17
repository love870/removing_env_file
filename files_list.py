# import OS module
import os

# Get the list of all files and directories

#Taking User Input
file_path=input('Enter the path of file=')
#path of the directory

path = file_path
#directory_list is used to get the list of all the files and directories in the given path
dir_list = os.listdir(path)

#print the list of all the files and directories in the given path
print("Files and directories in ',", path, "', :")

# prints all files 
print(dir_list)
