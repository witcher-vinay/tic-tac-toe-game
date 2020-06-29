l1=[" "," "," ","|"," "," "," ","|"," "," "]
l2=[" "," "," ","|"," "," "," ","|"," "," "]
l3=[" "," "," ","|"," "," "," ","|"," "," "]
a= "_____________"

def design():
    for i in l1:
        print(i,end="")
    print("")
    print(a)
    print("")

    for i in l2:
        print(i,end="")
    print("")
    print(a)
    print("")

    for i in l3:
        print(i,end="")
    print("")
    

p1=0
level=" "   
def details(p1,level):
    print("-------Plese Enter your name------")
    p1=input("")
    print("""-------Select Level you want to play---------
            Enter 1 for  ----- Easy
            Enter 2 for  ----- Medium
            Enter 3 for  ----- Hard
    """)
    level=int(input())

    if(level==1 or level==2 or level==3):
        print("--------Level selected Sucessfully--------")

    else:
        print("------Selcted level is wrong-------")
        print("----------Please try again----------")
        details()

details(p1,level)

print(details.name())


   