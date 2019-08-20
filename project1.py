import pandas as pd
data=pd.read_csv("employee.csv")
ch=' '
while(1):
    choice=int(input(" 1.Sort By Age 2.Sort By Salary \n Enter the option: "))
    if(choice==1):
        data.sort_values(["Age"],axis=0,ascending=True,inplace=True)
        print(data)
    elif(choice==2):
        data.sort_values(["Salary"],axis=0,ascending=True,inplace=True)
        print(data)
    ch=input("Do u want to continue y/n ")
    if(ch=='y'):
        continue
    else:
        break
