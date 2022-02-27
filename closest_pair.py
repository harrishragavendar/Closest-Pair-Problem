import math
def closest_pair(p):
    d = float("inf")
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            d=min(d,math.sqrt((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2))
    return d
n=int(input("Enter the number of points : "))
p=[]
for i in range(n):
    x,y=eval(input("Enter the x and y co-ordinates : "))
    p.append([x,y])
d=closest_pair(p)
print("Distance between the closest pair of points : ",round(d,3))
