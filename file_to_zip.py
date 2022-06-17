# importing zipfile module
import zipfile
# Taking input from user
enter_file=input("File convert into Zip: ")
output_file=input('zip file name saved as: ')+'.zip'

# Assigning enter_file variable to target
target=enter_file

# Opening  a zip file in Write mode
handle=zipfile.ZipFile(output_file,'w')
handle.write(target,compress_type=zipfile.ZIP_DEFLATED)
# Closing the zip file
handle.close()
# Message
print('file created')
