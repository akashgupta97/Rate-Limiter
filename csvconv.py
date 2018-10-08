#File to write in CSV FILE "FinalResults.csv"

#importing header files
import os
import csv

#Initializing parameters
Main_List=list()   # List storing final values
Temp_List1=list()
Temp_List2=list()
tuple=()
count=0

i=0  #Temporary variable to traverse through the Main_List

FileName1=open("outp.txt",'r')   #opening file

# Creating list of developers to write in CSV FILE "FinalResults.csv"

for line in FileName1:
    Temp_List1=line.split(",")
    if(count==0):
        Temp1=Temp_List1[3]
        Main_List.append(Temp_List1[0:4])
        Temp_List1[5]=Temp_List1[5].rstrip("\n")
        tuple=(Temp_List1[4],Temp_List1[5])
        Temp_List2.append(tuple)
        count=1
    else:
        Temp_List1[5] = Temp_List1[5].rstrip("\n")
        tuple = (Temp_List1[4], Temp_List1[5])
        if(Temp1==Temp_List1[3]):
            Temp_List2.append(tuple)
        else:
                Main_List[i].append(Temp_List2)
                Temp_List2=list()
                Temp_List2.append(tuple)
                Main_List.append(Temp_List1[0:4])
                Temp1=Temp_List1[3]
                i=i+1

Main_List[i].append(Temp_List2)
FileName1.close()



Temp_List3 = []
for loc1 in range(0,len(Main_List)):
    FileStr = os.getcwd() + "\\pdata.txt"
    FileName2=open(FileStr,'r')
    for line in FileName2:
        Temp_List3=line.split("###")
        if(Temp_List3[0]==Main_List[loc1][3]):
            Main_List[loc1].append(Temp_List3[1])
            Main_List[loc1].append(Temp_List3[3])
            Temp_List3[4]=Temp_List3[4]
            Temp_List3[5]=Temp_List3[5].rstrip("\n")
            Main_List[loc1].append(Temp_List3[4])
            Main_List[loc1].append(Temp_List3[5])
FileName2.close()
#Creating a list of developers with zero repositories on GitHub

print(Main_List)

Zero_List=[]
FileStr = os.getcwd() +  "\\pdata.txt"
FileName2 = open(FileStr, 'r')
for line in FileName2:
    Temp_List3 = line.split("###")

    if(Temp_List3[1]=='0'):
        Temp_List3[5]=Temp_List3[5].rstrip("\n")
        Temp_List4=Temp_List3[2].split("_")
        Zero_List.append(Temp_List4[0:3] + Temp_List3[0:2] + Temp_List3[3:6])
FileName2.close()

