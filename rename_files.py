#import modules
import os

#Taking input from user

#Enter the name of file which you want to rename
input_filename=input('enter_input_file_name=')

#Enter New Name of the file
output_filename=input('enter_output_file_name=')

#os.rename is used to rename files
os.rename(input_filename, output_filename)