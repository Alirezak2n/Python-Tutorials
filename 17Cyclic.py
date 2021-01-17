
def solution(a,k):
    result = [None] * len(a) #ye list khali b andaze list vorudi
    

    for i in range(len(a)):#be andaze tedad araye ha
        result[(i+k) % len(a)] = a[i]
    # be andaze k k mikhaym ja b ja shan va baghimande taghsim bar 5 ro dar list jadid mizarim
    
    return result

print(solution([1, 2, 4, 5, 8], 2))
