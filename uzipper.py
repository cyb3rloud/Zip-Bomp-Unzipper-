import zipfile
import os

current_zip = "0.zip"
#This starts from the zip file called 0.zip so you should make your adjustments to point to your file name and run the file in the same directory as that zip file
#Each zip file contains another zip file, and:
#The password to unzip each one is the name of the zip file inside.
#For example:
#You unzip 0.zip
#Inside is 83832.zip
#To unzip 83832.zip, you use the password: 83832
#This repeats hundreds or thousands of times — a recursive maze!

while True:
    with zipfile.ZipFile(current_zip) as z:
        # get the name of the next zip file
        inner_file = z.namelist()[0]
        password = os.path.splitext(inner_file)[0]
        print(f"[+] Extracting {inner_file} using password: {password}")
        
        # extract the next zip
        z.extract(inner_file, pwd=bytes(password, 'utf-8'))

    current_zip = inner_file
