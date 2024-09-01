#variables
walls=[]
gallons=1/350
total=0

while True:
    n=input("Enter wall size")
    if len(n)==0:
        break
    s=n.split(',')
    if len(s)<2:
        print("invalid input :")
        break
    #convert the string to inputs
 
    w=int(s[0])
    h=int(s[1])
    item=[w,h]
    walls.append(item)
    print(f"adding the item {item}")
for m in walls:
    w=m[0]
    h=m[1]
    n=w*h
    v=n*gallons
    total+=v
print(f"total you need to buy {round(total,2)} gallons of paint")
