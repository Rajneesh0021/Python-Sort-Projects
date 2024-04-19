email = input('Enter Email :')



def emial_validate(email):
 j=0
 if len(email)>=6 :
    if email[0].isalpha():
        if ("@" in email) and (email.count('@')==1) :
            if (email[-3]==".") ^ (email[-4]=="."):
                for i in email:
                    if i.isspace():
                        print('ERROR: No space allowed')
                        break
                    elif i.isalpha():
                        if i==i.upper():
                            print("ERROR: Uppercase not allowed")
                            break
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        j=1 
                        break  
                if j==1:
                    print("ERROR: Invalid character involved")
                else:
                    print("correct email address")
            else :
                print('ERROR: . is not present ')    
        else:
            print("ERROR: @ is not present")
    else:
        print('ERROR: first character is a number')
 else :
    print('ERROR: email has less character')   


emial_validate(email)