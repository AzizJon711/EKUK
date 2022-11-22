"""
Created on Wed Nov 23 01:40:22 2022

@author: AzizJon711
"""

a=int(input("a= "))
b=int(input("b= "))
def kopaytuvchi(n):
    list1=[]
    for i in range(2,n+1):
        while(True):
            if n%i==0:
                n=n/i
                list1.append(i)
            if n%i!=0:
                break;
    return list1
list1=kopaytuvchi(a)
list2=kopaytuvchi(b)
k=1
for i in range(2,a+1):
    if list1.count(i)<=list2.count(i):
        k*=i**list1.count(i)
    elif list1.count(i)>list2.count(i):
        k*=i**list2.count(i)
print(k)
