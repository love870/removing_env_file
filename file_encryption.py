
# # import required module
import os.path
from tkinter.tix import InputOnly
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key() 

#  This method generates a new fernet key. The key must be kept safe as it is the most important component to decrypt the ciphertext.

# Taking input for user
input_file=input("please input file Name")
output_file=input("Enter the name of encrypted file")
# dec_file=input("Enter the name of decrypted files")

# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
print(key)
 
# using the generated key
fernet = Fernet(key)
 
# opening the original file to encrypt
with open(input_file, 'rb') as file:
    original = file.read()
     
# encrypting the file
encrypted = fernet.encrypt(original)
print("*****")
print(encrypted)
 
# opening the file in write mode and
# writing the encrypted data
# with open(input_file, 'wb') as encrypted_file:
#     encrypted_file.write(encrypted)

save_path = 'file_encryption'
file_name = input_file

completeName = os.path.join(save_path, output_file)
print("-----------")
print(completeName)
file1 = open(completeName, "wb")
file1.write(encrypted)
file1.close()
# ---------- code for decrypting the file ---------- 


# # # using the key
# fernet = Fernet(key)

# # # opening the encrypted file
# with open(input_file, 'rb') as enc_file:

# # # Here File can be read
#    encrypted = enc_file.read() 
 

# # # decrypting the file
# decrypted = fernet.decrypt(encrypted)
# print(decrypted)
 
# # # opening the file in write mode and
# # # writing the decrypted data
# # with open(dec_file, 'wb') as dec_file:
# #     dec_file.write(decrypted)