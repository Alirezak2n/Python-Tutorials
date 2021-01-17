
def solution(a):#a weight anha va b jahat harekat anhas
   counter = 0#tedade tekrar
   candidate = 0#ebteda candid nadarim
   for i in a:#baraye har item ddar a
       if counter == 0: #age counter 0 bud uno 1 mikonim
           candidate = i #va candidate ro mizarim jaa candidate
           counter +=1
       elif candidate == i:#agar ccandidate dashtim check mikonim 
           #agar barabar budan counter ro afzayesh ya kahesh midim
           counter += 1
       else: 
           counter -=1
   occur=a.count(candidate) #tedad tekrar ye candidate ro mishmorim
   if occur > (len(a)/2):       #agar bishtar az nesfe tedad bud
       #be onvan leader midim birun
       print (candidate)
       return a.index(candidate)
   
   else:
       return -1
    
    
    
print(solution([3,2,0,1,1,1,1]))       
     
    