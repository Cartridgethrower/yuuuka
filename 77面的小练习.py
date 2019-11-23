#e3.12DayDayUp365.py
dayup, dayfactor = 1.0, 0.001
for i in range(365):
   if i % 7 in [6, 5, 0]:
       dayup = dayup*(1)
   else:
       dayup = dayup * (1 + dayfactor)
print("向上4天什么都不做3天的力量:{:.2f}.".format(dayup))
