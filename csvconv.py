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



