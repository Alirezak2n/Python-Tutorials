from math import ceil,floor
def solution (a,b,k):
    start=ceil(a/k)
    end=floor(b/k)
    result = end- start +1
            
        
    return result
    
print(solution(6,12,2))
