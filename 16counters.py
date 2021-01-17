
def solution(n,a):#tedad counterha ba liste taghyir o afzayesh
    counters = [0] *n#tedade counterha
    start_line = 0 #khate aghaz
    current_max= 0 #meghdare counter ba bishtarin meghad
    for i in a: # baraye har instruction in karo mikone
        x = i-1 #shomare counter az 1 vali list az 0 hast
        # 3 case motefavet darim
        if i > n: #age instruction bishtar az tedad bashe
            start_line=current_max #khate shoru ro miarim jolo
        elif counters[x] < start_line:#age counteri ro goft k
            #kamtar az khate shoro bashe
            counters[x] = start_line + 1#b andaze khate shoro
            #ba 1 adad barash ezafe mikonim
        else:
            counters[x] +=1#va dar gheir in surat
            #yedune b counter ezafe mikonim
        if i <= n and counters[x]>current_max:
            #age i kamtar az n bashe vali counter bala tar az
            #max bere ,un couter ro be max mizarim
            current_max = counters[x]
    for i in range (0,len(counters)):
        #baraye baghi counter ha k shomarashun tu list nabud
        #be andaze khate shoru miare jolo
        if counters[i] < start_line:
            counters[i] = start_line
    return counters

print(solution(5,[3,4,4,6,1,4,4]))
            
    
