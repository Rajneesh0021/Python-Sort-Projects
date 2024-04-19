import re


email=input("Enter Email :  ")


def check_email(email):
 condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

 if re.search(condition,email):
    print("correct email")
 else :
    print("wrong email")


check_email(email)