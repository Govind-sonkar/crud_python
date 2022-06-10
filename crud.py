import json  ,os

print("1.Insert \n 2.Update \n 3.Delete \n 4.Get")


def insert():
    if(os.path.exists("crud.json")):
        f=open("crud.json","r")
        b=json.load(f)
        c={}
        c["Name"]=input("Enter the name: ")
        c["Email"]=input("Enter the Email: ")
        c["Password"]=input("Enter the password: ")
        b.append(c)
        ff=open("crud.json","w")
        json.dump(b,ff,indent=4)
        print("data inserted")
    else:
        b=[]
        c={}
        c["Name"]=input("Enter the name: ")
        c["Email"]=input("Enter the Email: ")
        c["Password"]=input("Enter the password: ")
        b.append(c)
        ff=open("crud.json","w")
        json.dump(b,ff,indent=4)
        print("data inserted")

def update():
    aa=open("crud.json","r")
    ff=json.load(aa)
    n=input("Insert the Email: ")
    cc=0
    for i in ff:
        if i["Email"]== n:
            g={}
            g["Name"]=input("Enter the Name : ")
            g["Password"]=input("Enter the password : ")
            g["Email"]=n
            ff[cc]=g
            f=open("crud.json","w")
            json.dump(ff,f,indent=4)
            print("data inserted")
            break
        cc+=1
    else:
        print("Invalid email")
def Delete():
    aaa=open("crud.json","r")
    ff=json.load(aaa)
    length=len(ff)
    m=input("Emter the Email : ")
    dd=0
    for i in ff:
        if i["Email"]==m:
            ff.remove(i)
            if length==1:
                os.remove("crud.json")
                break
            else:
                file=open("crud.json","w")
                json.dump(ff,file,indent=4)
                break
    else:
        print("invalid Email")
    
a=int(input("Choose the option : "))
if a==1:
    insert()
elif a==2:
    update()
elif a==3:
    Delete()
