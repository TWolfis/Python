#!/usr/bin/env python3 
#checks password for validity
#Author: Thomas Wolfis 
import getpass as gp
import re 

str1 = gp.getpass()
lngpwd = len(str1)
while True:   
    if (len(str1)<8): 
        flag = 1
        break
    elif not re.search("[a-z]", str1): 
        flag = 2
        break
    elif not re.search("[A-Z]", str1): 
        flag = 3
        break
    elif not re.search("[0-9]", str1): 
        flag = 4
        break
    elif not re.search("[_, #, @, !,%,^,&,*]", str1): 
        flag = 5
        break
    elif re.search("\s", str1): 
        flag = 6
        break
    else: 
        flag = 0
        print("Valid password") 
        break

if flag == 1: 
    print("Your password only contains %d charactes, it should contain more then 8 characters" %(lngpwd))
elif flag == 2:
        print("Your password can only contain alphabetical characters")
elif flag == 3: 
    print("Your password contains no uppercase letters, for more savety add atleast one uppercase letter.")    
elif flag == 4: 
    print("Your password has no numbers in it. Add atleast one number")
elif flag == 5: 
    print("Your password contains no special characters, add at least one of the following characters: $, #, @, !,%,^,&,* ")
elif flag == 6: 
    print("Your password should not contain an escape character")

	
