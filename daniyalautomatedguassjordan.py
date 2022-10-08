def prnt(v):
    for i in range(3):
        for j in range(4):
            print("%.3f"%m[i][j],end='       ')
        print()
       

m=[[2,30,5,1],[1,10,1,3],[5,21,2,1]]
row= 4
column=3
prnt(m) 
for f in range(len(m)):
        
    #for pivot value
    rn=int(input('enter row'))
    cn=int(input('enter column'))
    rn=rn-1
    cn=cn-1
    #to make it userfriendly start the couting from 1
    pivot=m[rn][cn]
    #to make pivot 1
    for j in range(row):
        m[rn][j]=(m[rn][j])/pivot 
    print()
    print('after making pivot value 1')
    print()
    prnt(m)
    for y in range(column):
        if y!=rn:
            zero=m[y][cn]
            for d in range(row):
                m[y][d]=m[y][d]-(zero*m[rn][d])
    print('after making zero')   
    print()
    prnt(m)
for k in range(3):
    for b in range(4):
        t=m[k][b]
        if b==0 and t==1:
            x1=m[k][2]
            print("x1=","%.3f"%x1)
        elif b==1 and t==1:
            x2=m[k][2] 
            print("x2=","%.3f"%x2)  
        elif b==3 and t==1:
            x3=m[k][2] 
            print("x3=","%.3f"%x3) 
input()



    
