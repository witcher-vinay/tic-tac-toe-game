import random
class Tic:
    
    
    
    def design(self,l1,l2,l3,a):
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
        

       
    def details(self,p1,level):
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

    #list1=[1,2,3,4,5,6,7,8,9]
    def easy(list1):
        while(l1[1]==" " or l1[5]==" " or l1[9]==" " or l2[1]==" " or l2[5]==" " or l2[9]==" " or l3[1]==" " or l3[5]==" " or l3[9]==" " ):
            
            print("Enter number from  " list1)              
            

            fault=int(input())

            if(fault==1):
                l1[1]="O"
            elif(fault==2):
                l1[5]="O"
            elif(fault==1):
                l1[9]="O"
            elif(fault==1):
                l2[1]="O"
            elif(fault==1):
                l2[5]="O"
            elif(fault==1):
                l2[9]="O"
            elif(fault==1):
                l3[1]="O"
            elif(fault==1):
                l3[5]="O"
            elif(fault==1):
                l3[9]="O"
            else:
                print("wrong input")
            
            design(self,l1,l2,l3,a)


            list1.remove(fault)

            fault1=random.choice(list1)

            if(fault1==1):
                l1[1]="X"
            elif(fault1==2):
                l1[5]="X"
            elif(fault1==1):
                l1[9]="X"
            elif(fault1==1):
                l2[1]="X"
            elif(fault1==1):
                l2[5]="X"
            elif(fault1==1):
                l2[9]="X"
            elif(fault1==1):
                l3[1]="X"
            elif(fault1==1):
                l3[5]="X"
            elif(fault1==1):
                l3[9]="X"

            list1.remove(fault1)
            
            design(self,l1,l2,l3,a)





            

A=Tic()

l1=[" "," "," ","|"," "," "," ","|"," "," "]
l2=[" "," "," ","|"," "," "," ","|"," "," "]
l3=[" "," "," ","|"," "," "," ","|"," "," "]
a= "_____________"
#A.design(l1,l2,l3,a)

p1=0
level=" "
A.details(p1,level)
print(A.details(p1))



list1=[1,2,3,4,5,6,7,8,9]




    
