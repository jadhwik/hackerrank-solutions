## printing a list that have a list within it. The sum of each inside list element will be less than or greater than 'n' but not equal to n

def cuboid(x,y,z,n):
    list=[]
    
    for i in range(0,x+1):
        
        for j in range(0,y+1):
            
             for k in range(0,z+1):
                if i+j+k!=n:
                    list.append([i,j,k])
    return list
x=int(input())
y=int(input())
z=int(input())
n=int(input())
print(cuboid(x,y,z,n),end='')   

    
    
           


 
                    
                    
    
    


