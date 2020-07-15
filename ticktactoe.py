import random
class Tic:
    l1=[" "," "," ","|"," "," "," ","|"," "," "]
    l2=[" "," "," ","|"," "," "," ","|"," "," "]
    l3=[" "," "," ","|"," "," "," ","|"," "," "]
    a= "_____________"
    
    
    def design(self):         # 1st fun
        print("")
        print("")
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
        return "  "
        

       
    def details(self,p1,level):
        print("")
        print("")
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


    def easy(self,p1):                        # 3rd fun
        #while(self.l1[1]==" " or self.l1[5]==" " or self.l1[9]==" " or self.l2[1]==" " or self.l2[5]==" " or self.l2[9]==" " or self.l3[1]==" " or self.l3[5]==" " or self.l3[9]==" " ):
        for i in range(0,4):
            
            
            print("Enter number from  ", self.list1)              
            

            fault=int(input())
            if fault not in self.list1:
                print("Number not selected from list ----WORONG INPUT ")
                print("-------GAME OVER -----------")
                break
            
            
            print("")
            print("")
            print("YOUR MOVE")
            print("")
            print("")

            if(fault==1):
                self.l1[1]="O"
            elif(fault==2):
                self.l1[5]="O"
            elif(fault==3):
                self.l1[9]="O"
            elif(fault==4):
                self.l2[1]="O"
            elif(fault==5):
                self.l2[5]="O"
            elif(fault==6):
                self.l2[9]="O"
            elif(fault==7):
                self.l3[1]="O"
            elif(fault==8):
                self.l3[5]="O"
            elif(fault==9):
                self.l3[9]="O"
            
            print(self.design())
            
            
            
            if(self.l1[1]=="O" and self.l1[5]=="O"  and self.l1[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l2[1]=="O" and self.l2[5]=="O"  and self.l2[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l3[1]=="O" and self.l3[5]=="O"  and self.l3[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[1]=="O" and self.l2[1]=="O"  and self.l3[1]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[5]=="O" and self.l2[5]=="O"  and self.l3[5]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[9]=="O" and self.l2[9]=="O"  and self.l3[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[1]=="O" and self.l2[5]=="O"  and self.l3[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[9]=="O" and self.l2[5]=="O"  and self.l3[1]=="O"):
                print("    ",p1, "   WON  ")
                break


            self.list1.remove(fault)

            fault1=random.choice(self.list1)

            if(fault1==1):
                self.l1[1]="X"
            elif(fault1==2):
                self.l1[5]="X"
            elif(fault1==3):
                self.l1[9]="X"
            elif(fault1==4):
                self.l2[1]="X"
            elif(fault1==5):
                self.l2[5]="X"
            elif(fault1==6):
                self.l2[9]="X"
            elif(fault1==7):
                self.l3[1]="X"
            elif(fault1==8):
                self.l3[5]="X"
            elif(fault1==9):
                self.l3[9]="X"
                
            self.list1.remove(fault1)
            print("")
            print("")
            print("COMPUTER MOVE")
            print("")
            print("")
            
            print(self.design())
            
            
            if(self.l1[1]=="X" and self.l1[5]=="X"  and self.l1[9]=="X"):
                print("  COMPUTER WON ")
                break
            if(self.l2[1]=="X" and self.l2[5]=="X"  and self.l2[9]=="X"):
                print("  COMPUTER WON ")
                break
            if(self.l3[1]=="X" and self.l3[5]=="X"  and self.l3[9]=="X"):
                print("  COMPUTER WON ")
                break
            if(self.l1[1]=="X" and self.l2[1]=="X"  and self.l3[1]=="X"):
                print("  COMPUTER WON ")
                break
            if(self.l1[5]=="X" and self.l2[5]=="X"  and self.l3[5]=="X"):
                print("  COMPUTER WON ")
                break
            if(self.l1[9]=="X" and self.l2[9]=="X"  and self.l3[9]=="X"):
                print("  COMPUTER WON ")
                break
            if(self.l1[1]=="X" and self.l2[5]=="X"  and self.l3[9]=="X"):
                print("  COMPUTER WON ")
                break
            if(self.l1[9]=="X" and self.l2[5]=="X"  and self.l3[1]=="X"):
                print("  COMPUTER WON  ")
                break
            
            
            if(len(self.list1)==1):
                if(self.list1[0]==1):
                    self.l1[1]="O"
                elif(self.list1[0]==2):
                    self.l1[5]="O"
                elif(self.list1[0]==3):
                    self.l1[9]="O"
                elif(self.list1[0]==4):
                    self.l2[1]="O"
                elif(self.list1[0]==5):
                    self.l2[5]="O"
                elif(self.list1[0]==6):
                    self.l2[9]="O"
                elif(self.list1[0]==7):
                    self.l3[1]="O"
                elif(self.list1[0]==8):
                    self.l3[5]="O"
                elif(self.list1[0]==9):
                    self.l3[9]="O"
                print("")
                print("")
                print("FINAL MOVE")
                print("")
                print("")
                print(self.design())
            if(self.l1[1]=="O" and self.l1[5]=="O"  and self.l1[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l2[1]=="O" and self.l2[5]=="O"  and self.l2[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l3[1]=="O" and self.l3[5]=="O"  and self.l3[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[1]=="O" and self.l2[1]=="O"  and self.l3[1]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[5]=="O" and self.l2[5]=="O"  and self.l3[5]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[9]=="O" and self.l2[9]=="O"  and self.l3[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[1]=="O" and self.l2[5]=="O"  and self.l3[9]=="O"):
                print("    ",p1, "   WON  ")
                break
            elif(self.l1[9]=="O" and self.l2[5]=="O"  and self.l3[1]=="O"):
                print("    ",p1, "   WON  ")
                break
            else:
                print(" IS'S  A   DRAW ")
                PRINT("---------GAME OVER---------")
                
A=Tic()
print("-------Plese Enter your name------")
p2=input("")
p1=p2.upper()
A.design()


level=" "
A.details(p1,level)

A.easy(p1)
