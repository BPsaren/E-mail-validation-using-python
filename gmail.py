email=input("Checking your valid email id :") #a@gmail.co && a@yahoo.com frist letter isalpha #@ and one:
k,j,d=0,0,0
if len(email)>=10 and len(email)>=11:
    print("Right email id :1")
    if email[0].isalpha():
        print("Right email id:2")
        if ("@" in email) and (email.count("@")==1):
            print("Right email id :3")
            if (email[-3]==".") or (email[-4]=="."):
                    print("Right email id :4")
                    for i in email: 
                       if i==i.isspace():
                            k=1
                       elif i==i.isalpha():
                           if i==i.upper():
                               j=1
                       elif i.digit():
                           continue
                       elif i=="_" or i=="." or i=="@":
                           continue                     
                       else:
                           d=1
                    if k==1 or j==1 or d==1:
                        print("Wrong email id :5")
                    else:
                        print("Right email id:6")   
            else:
                print("Wrong email id : 4")
        else:
            print("Wrong email id :3")
    else:
        print("Wrong email id :2")    
else:
    print("wrong email id :1")
