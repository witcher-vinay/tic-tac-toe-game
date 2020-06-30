import random
class Tic:
    l1=[" "," "," ","|"," "," "," ","|"," "," "]
    l2=[" "," "," ","|"," "," "," ","|"," "," "]
    l3=[" "," "," ","|"," "," "," ","|"," "," "]
    a= "_____________"
    
    
    def design(self):         # 1st fun
        for i in self.l1:
            print(i,end="")
        print("")
        print(self.a)
        print("")

        for i in self.l2:
            print(i,end="")
        print("")
        print(self.a)
        print("")

        for i in self.l3:
            print(i,end="")
        print("")
        

       
    def details(self,p1,level):
        print("-------Plese Enter your name------")               # 2nf fun
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

    
    list1=[1,2,3,4,5,6,7,8,9]


    def easy(self):                        # 3rd fun
        #while(self.l1[1]==" " or self.l1[5]==" " or self.l1[9]==" " or self.l2[1]==" " or self.l2[5]==" " or self.l2[9]==" " or self.l3[1]==" " or self.l3[5]==" " or self.l3[9]==" " ):
        for i in range(0,4):    
            print("Enter number from  ", self.list1)              
            

            fault=int(input())

            if(fault==1):
                self.l1[1]="O"
            if(fault==2):
                print("asdfghgfdsasdfgh")
                self.l1[5]="O"
            if(fault==1):
                self.l1[9]="O"
            if(fault==1):
                self.l2[1]="O"
            if(fault==1):
                self.l2[5]="O"
            if(fault==1):
                self.l2[9]="O"
            if(fault==1):
                self.l3[1]="O"
            if(fault==1):
                self.l3[5]="O"
            if(fault==1):
                self.l3[9]="O"
            else:
                print("wrong inputtttttttttttttttt" ,fault)
            
            print(self.design())


            self.list1.remove(fault)

            fault1=random.choice(self.list1)

            if(fault1==1):
                self.l1[1]="X"
            if(fault1==2):
                self.l1[5]="X"
            if(fault1==1):
                self.l1[9]="X"
            if(fault1==1):
                self.l2[1]="X"
            if(fault1==1):
                self.l2[5]="X"
            if(fault1==1):
                self.l2[9]="X"
            if(fault1==1):
                self.l3[1]="X"
            if(fault1==1):
                self.l3[5]="X"
            if(fault1==1):
                self.l3[9]="X"
            else:
                print("SystemErrorrrrrrrrrr  ", fault1)
            self.list1.remove(fault1)
            
            print(self.design())



A=Tic()
A.design()

p1=0
level=" "
A.details(p1,level)

A.easy()








    
