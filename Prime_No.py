l=[1,2]
import time
n=int(input())
for i in range(3,n):
    if i%2==0:
        pass
    else:
        for j in range(3,i+1,2):
            if i%j==0 and j!=i:
                break
            elif j==i:
                l.append(j)
                #print(j,end=" ")
            else:
                pass
l.sort(key=int)
print(" ".join(map(str,l)))
