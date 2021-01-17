def solution (a):
    suffix_sum = [0]*(len(a)+1)
    count=0
    for i in range(len(a) -1,-1,-1):#start,stop,step,
        #dar in mesal akhari shoru ta avali miaym va 
        #yki yki kam mikonim
        print (i,a[i],suffix_sum[i],suffix_sum[i+1])
        print(suffix_sum)
        suffix_sum[i] = a[i] + suffix_sum[i +1]
        if a[i] == 0:
            count +=suffix_sum[i]
        if count > 100000000:
            return -1
        
    return count
    
print(solution([0,1,0,1,1]))

