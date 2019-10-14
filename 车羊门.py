from random import*
TIMES = 1000
first_choice_n=0#初始不改选择的次数
change_choice_n=0#初始化更改选择的次数
for i in range(TIMES):
    car_in_door=randint(0,2)
    my_guess=randint(0,2)
    if car_in_door==my_guess:
        first_choice_n+=1
    else:
        change_choice_n+=1
print("不改选择：{}".format(first_choice_n/TIMES))
print("改变选择：{}".format(change_choice_n/TIMES))
