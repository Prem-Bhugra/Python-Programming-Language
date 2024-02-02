"""Program to multiply two matrices"""
m1 = [[1,2,3],[5,3,1],[7,9,8]]
m2 = [[3,4],[12,4],[8,14]]  
m1m2 = []  
m = len(m1)
n1 = len(m1[0])
n2 = len(m2)    
p = len(m2[0])    
if n1 != n2:
    print("Dimension Dismatch!")
else:
    for i in range(m):  
        row = []
        for j in range(p):    
            sum = 0
            for k in range(n1):    
                mult = m1[i][k] * m2[k][j]
                sum += mult
            row.append(sum)
        m1m2.append(row)
    print(m1m2)