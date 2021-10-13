#0,1,1,2,3,5,8,13,21,34.....


a=int(input("Enter a number of your choice: "))
d = 0
e = 1
f = 0
while(f <= a):
    print(f)
    d=e
    e=f
    f=d+e