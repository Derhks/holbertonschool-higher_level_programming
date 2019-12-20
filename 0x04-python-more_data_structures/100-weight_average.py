#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_mul = 0
    sum_div = 0
    if my_list:
        for cnt1 in range(len(my_list)):
            for cnt2 in range(len(my_list)):
                sum_mul += my_list[cnt1][cnt2] * my_list[cnt1][cnt2 + 1]
                break
            sum_div += my_list[cnt1][cnt2 + 1]
        return sum_mul / sum_div
    return 0
