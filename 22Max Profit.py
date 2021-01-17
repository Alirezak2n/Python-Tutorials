
def solution(a):
    global_max=0
    local_max=0
    for i in range(1,len(a)):#az 1 shoru mikonim chon beyn 1 element va ghablish barresi mikonim
        d=a[i]-a[i-1]#ekhtelaf har adad ba adade ghablish
        print(d)
        #local max ba un ekhtelafe bishtare ye ekhtelaf tanha
        local_max=max(d,local_max+d)
        print(local_max)
        #global max bishtare ya local max
        global_max=max(local_max,global_max)
    return global_max
    
    
print(solution([23171,21011,21123,21366,21013,21367]))       
     
    