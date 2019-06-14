a=[1,2,3,4]
def leftrotatebyone(a):
    temp=a[0]
    for i in range(len(a)-1):
        a[i]=a[i+1]
    a[len(a)-1]=temp
    return(a)
def leftrotate(a,d):
    for i in range(1,d+1):
        leftrotatebyone(a)
    return(a)
print(leftrotate(a,2))
        
