import numpy as np
import pandas as pd
Chicago=pd.read_csv('chicago.csv')
NewYork=pd.read_csv('new_york_city.csv')
Washington=pd.read_csv('washington.csv')
print("Hello let's explore some Us bike share data")
x = input("Would you like see data for Chicago,New York or Washington?\n")
if x == "Chicago":
    df = Chicago
elif x == "New York":
    df=NewYork
elif x == "Washington":
    df = Washington

df['Start Time']=pd.to_datetime(df['Start Time'])
df['Month']=df['Start Time'].dt.month_name()
df['Day']=df['Start Time'].dt.day_name()
df['Hour']=df['Start Time'].dt.hour
df['Day']=df['Day'].replace("Sunday","1")
df['Day']=df['Day'].replace("Monday","2")
df['Day']=df['Day'].replace("Tuesday","3")
df['Day']=df['Day'].replace("Wednesday","4")
df['Day']=df['Day'].replace("Thursday","5")
df['Day']=df['Day'].replace("Friday","6")
df['Day']=df['Day'].replace("Saturday","7")
#print(df)
y= input("Would you like to filter the data by month,day,both or not at all? Type 'none' for no time filter\n")

if y== "month":
    filter = input("which month?January,February,March,April,May or June?\n")
    proc1=df.loc[df['Month'] == filter]
elif y=="day":
    filter2 = input("which day? please type your response as an integer e.g(1=sunday)\n")
    proc1=df.loc[df['Day']==filter2]
elif y =="both":
    filter = input("which month?January,February,March,April,May or June?\n")
    filter2 = input("which day? please type your response as an integer e.g(1=sunday)\n")
    proc1=df.loc[(df['Month'] == filter)&(df['Day']==filter2)]
elif y== "none":
    proc1=df



maxM=proc1["Month"].value_counts().idxmax()
countM=proc1['Month'].value_counts().max()
maxD=proc1["Day"].value_counts().idxmax()
countD=proc1['Day'].value_counts().max()
maxH=proc1['Hour'].value_counts().idxmax()
countH=proc1['Hour'].value_counts().max()
maxStart=proc1['Start Station'].value_counts().idxmax()
maxEnd=proc1['End Station'].value_counts().idxmax()
totaltime=proc1['Trip Duration'].sum()
average=proc1['Trip Duration'].mean()




print("Most popular hour: ",maxH,"Count: ",countH)
print("\nMost popular Day: ",maxD,"Count: ",countD)
print("\nMost popular Month: ",maxM,"Count: ",countM)
print("\nMost common start station",maxStart)
print("\nMost Common end station",maxEnd)
print("\nTotal travel time: ",totaltime)
print("\naverage travel time : ",average)

if x == "Washington":
    print("\nno gender/year of birth related data available!")
else:
    recent=proc1['Birth Year'].max()
    earliest=proc1['Birth Year'].min()
    common=proc1['Birth Year'].value_counts().idxmax()
    print(proc1["Gender"].value_counts())
    print("\nearliest year of birth: ",earliest,"most recent year of birth: ",recent)
    print("\nmost common year of birth: ",common)
