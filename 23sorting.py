class disclog():
    def __init__(self,x,start_end):
        #in class noghte va  start o finish o migire
        self.x =x
        self.start_end = start_end
        
def solution(a):
    disc_history=[]
    for i in range(len(a)):
        disc_history.append(disclog(i - a[i] , 1))
        #center - shoa mishe noghte shoto pas 1
        disc_history.append(disclog(i + a[i] , -1))
        #center + shoa mishe noghte payan pas -1
    disc_history.sort( key =lambda d: (d.x, -d.start_end))
    # bar asas noghat shoru o payan sort karde va decending
    
    intersections = 0
    #result ma
    active_intersections = 0
    
    for l in disc_history:
        active_intersections += l.start_end
        # age ye noghte shoro yani ye disk hast
        if l.start_end > 0:
            intersections += active_intersections - 1
        #-1 mizarim ta tedade intersection ha ra peyda konim va na disk ha
        if intersections > 10000000:
            return -1
    return intersections
print(solution([1,5,2,1,4,0]))
print(solution([0]*100000))
    