
def solution(a,b):#a weight anha va b jahat harekat anhas
    survivors=0#tedad mande ha
    stack=[]#0 samte chap, 1 samte rast
    for i in range(len(a)):
        weight = a[i]
        if b[i] ==1:#age be rast miraft
            stack.append(weight) #vazn ro bzar tu stack
        else:
            ghadimi=stack.pop() if stack else -1 # agar stack ppor bud pop kon mahi ghadimi vagar na -1 bzar
            while ghadimi != -1 and ghadimi < weight:#agar 
                ghadimi = stack.pop() if stack else -1
            if ghadimi == -1:# agar jaye mahi ghadimi -1 bud yani ye survivor ezafe kon
                    survivors +=1
            else:
                    stack.append(ghadimi)
    return survivors + len (stack)
    
print(solution([4,8,2,6,7],[0,1,1,0,0]))       
print(solution([4,3,2,1,5],[0,1,0,0,0]))       
    