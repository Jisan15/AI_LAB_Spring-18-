
# coding: utf-8

# In[7]:


outlook =[0,0,1,0,1,1,0] # sunny = 0 and cloudy = 1
temparature=[0,1,1,1,0,0,0] # cold = 0 and warm = 1
routine=[0,1,0,0,0,1,1] #indoor = 0 and outdoor = 1
coat=[0,0,0,0,1,1,1] # no = 0 and yes = 1

sunny=0
cloudy=0
indoor=0
warm=0
outdoor=0
cold=0
yes=0

t=len(outlook)
for i in range(0,7):
    if coat[i]==1:
        yes=yes+1
        if outlook[i]==1:
            cloudy=cloudy+1
        if temparature[i]==1:
            warm=warm+1
        if routine[i]==1:
            outdoor=outdoor+1
            
if warm==0 or couldy ==0 or outdoor ==0:
    upper=0
else:
    upper=(cloudy/yes)*(warm/yes)*(outdoor/yes)*(yes/t)
    
if warm==0 or couldy ==0 or outdoor ==0:
     lower=0
else:
    lower=(cloudy/t)*(warm/t)*(outdoor/t)

if upper==0 or lower==0:
    total=0
else:
    total=(upper/lower)
print(total)


sunny=0
cloudy=0
indoor=0
warm=0
outdoor=0
cold=0
yes=0
c1=0
w1=0
o1=0

t=len(outlook)
for i in range(0,t):
    if coat[i]==0:
        yes=yes+1
        if outlook[i]==1:
            cloudy=cloudy+1
        if temparature[i]==1:
            warm=warm+1
        if routine[i]==1:
            outdoor=outdoor+1
            
print(cloudy)
print(warm)
print(outdoor)
print(yes)

for i in range(0,t):
    if outlook[i]==1:
            c1=c1+1
    if temparature[i]==1:
            w1=w1+1
    if a3[i]==1:
            o1=o1+1
            
print(o1)  
print(w1) 
print(c1) 

if warm==0 or cloudy ==0 or outdoor ==0:
    upper=0
else:
    upper=(cloudy/yes)*(warm/yes)*(outdoor/yes)*(yes/t)
    
if w1==0 or cloudy ==0 or outdoor ==0:
     lower=0
else:
    lower=(c1/t)*(w1/t)*(o1/t)

if upper==0 or lower==0:
    total=0
else:
    total=(upper/lower)



print(total)


