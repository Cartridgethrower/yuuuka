power = 1.0
for i in range(365):    
    if i % 11 in [0,1,2,7,8,9,10]:  #由于休息一天，所以循环又开始
        power = power * 1
    else:
        power = power * (1+0.01)
print("能力值为{:.2f}".format(power))
