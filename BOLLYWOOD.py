import random
l=['fanna','love','ishq','razzi','nawabjade','shole','shor']
s=random.choice(l)
n=len(s)
lst=[]
print("let's start bollywood game")
for i in range(n):
    lst.append('__')
print(lst)
lst1=[]
for i in s:
    lst1.append(i)
m=0
while(m<5):
    a=input("enter any letter:  ")
    f=0 
    for j in range(n):
        if lst1[j]==a:
            lst.pop(j)
            lst.insert(j,a)
            print(lst)
            f=f+1
    if f==0:
        m=m+1
        print("wrong......you have only",5-m,"chance")
    if lst==lst1:
        print("congo......you are winner...........")
        break
    
    
if lst!=lst1:
    print("good try........but you are looser.........")
    print(lst1)
