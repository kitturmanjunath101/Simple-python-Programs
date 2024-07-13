#mail - kitturmanjunath101@gmail.com
# a-z
# 0-9
# . 1 time
# @ 1 time
# . (2,3)

import re
mail_condition = "^[a-z]+[ 0-9]+[@]+[a-z]+[.]+[a-z]"
user_mail=input("enter your mail")
if re.search(mail_condition,user_mail):
    print("valid mail")
else:
    print("invalid mail")