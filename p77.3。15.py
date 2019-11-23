#e3.15DayDayUp365.py
dayup, dayfactor = 1.0, 0.001
for i in range(360):
   if i % 30 in [10,9,8,7,6,5,4,3,2,1]:
       dayup = dayup*(1)
   else:
       dayup = dayup * (1 + dayfactor)
print("向上10天什么都不做20天的力量:{:.2f}.".format(dayup))
