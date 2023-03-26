
def getdate():
           import datetime
           return datetime.datetime.now()

import datetime
def gettime():
    return datetime.datetime.now()



def enter_data():
    entry_choice = int(input("\n 1. EXERCISE \n 2. FOOD \n"))
    while entry_choice not in [1,2]:
         entry_choice=int (input("\n 1. EXERCISE \n 2. FOOD \n")) 

         

    if entry_choice ==1:
       filename=name+"exercise"
       ex_info=input("type here\n")
       with open("filename","a") as op:
                op.write(str([str(gettime())])+": "+ex_info+"\n")
                print("\n\t DONE \n")
    else :
        food_info=input("enter here \n")
        filename= name+"food"
        with open("filename","a") as op:
                op.write(str([str(gettime())])+ " : " + food_info+ "\n")
                print("\n\t DONE \n")



def show_data():
   entry_choice =int(input("\n 1. EXERCISE \n 2. FOOD\n"))
   while entry_choice not in [1,2]:
       entry_choice = int (input("\n 1. EXERCISE \n 2. FOOD\n"))
    
   if entry_choice ==1:
      filename= name+"exercise"
      with open("filename","r+") as op:
           for i in op:
              print(i ,end=" ")
   if entry_choice ==2:
      filename= name+"food"
      with open ("filename", "r+") as op:
          for i in op:
            print(i , end=" ")

       

print("\t\tHEALTH MANAGMENT SYSTEM\n\n")


name= input("ENTER YOUR NAME :  ")



main_choice=int(input("enter whether you want to input or output the data\n 1. INPUT \n 2. OUTPUT  :  "))
while main_choice not in [1,2]:
      
      main_choice=int(input("please enter the required character  :   "))
if main_choice== 1:
    enter_data()
if main_choice==2:
    show_data()


