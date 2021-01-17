digits = [0,1,2,3,4,5,6,7,8,9]

print(digits[-1])
print(digits[-len(digits)])
print(digits[:3])
#stride mige chanta chanta beri
print((digits[0:9:2]))
#bayad az akhar be aval bzanim
print((digits[9:0:-1]))
goods = 'success,win,best_coder,elham'
print(goods)
l = goods.split(",")
#ye string ro migire o split mikone be list
#va az , migire joda mikone
print(l)
# 2 ta string joda mikone az horufe win
l = goods.split("win")
print(l)
goods = 'success,win,best_coder,elham'
l = goods.split(',')
#miad join mikone o vasatesh harchi bkhaym mizare
l = " & ".join(l)
print(l)