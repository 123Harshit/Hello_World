my_array = ["A","B","C"]
for x in my_array:
    print(x)

print(len(my_array))

the_list = ["Finger1","Finger2","Finger3"]
print(the_list)
#Question 1
a = [3,4,6,7,8,9]

def har(a,n):
    for x in a:
        if x>=n:
            print(x)
har(a,4)
#Question 2
def count_evens(a):
    ans = 0
    for x in a:
        if x%2==0:
           ans+=x
    print(ans)
count_evens(a)

#Question 3
    
list = [2,1,10,4,3,6,7,9,8,5]
u = 0
v = len(list)-1
while u<=len(list) and v>=0 and v>=u:
    if((list[u]%2!=0) and (list[v]%2==0)):
        var = 0
        var = list[u]
        list[u] = list[v]
        list[v] = var
        u+=1
        v-=1
    elif((list[u]%2!=0) and (list[v]%2!=0)):
        v-=1
    elif((list[u]%2==0) and (list[v]%2==0)):
        u+=1
    else:
        u+=1
        v-=1
count = 0
for x in list:
    if(x%2==0):
        count+=1
print(count)

        
