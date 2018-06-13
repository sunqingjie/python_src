
# coding:gbk 
import sys  
def matrix(n):
    
    block = n - 1  # there are four block in one circle

    result = dict()
    
    row = 0
    col = 0
    
    number = 1
    while block >= 0:
        row = row + 1
        col = col + 1
        
        if block == 0 : result[(row,col)] = number # number in the center
            
        for direction in [(0,1),(1,0),(0,-1),(-1,0)]:  # [north,east,south,west], clockwise
            drow,dcol = direction
            for i in range(1,block + 1):
                result[(row,col)] = number
                row = row + drow
                col = col + dcol
                number = number + 1
    
    
        
        block = block - 2 # next block length
    
    return result        
    

if __name__ == '__main__':  # test
    
    print "git test"    
    
    n = 5
    result = matrix(n)
    
    for i in range(1,n+1):
        for j in range(1,n+1):        
            print str(result[(i,j)]).rjust( len(str(n*n))),
        print "\n"
        
print "测试"
