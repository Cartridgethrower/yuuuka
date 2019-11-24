dayup, dayfactor = 1.0, 0.01
for i in range(365):
   if i % 7 in [1,2,3]:
       dayup = dayup*(1)
   else:
       dayup = dayup * (1 + dayfactor)
print("平台型期望的力量:{:.2f}.".format(dayup))
