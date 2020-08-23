


import numpy as np

import pandas as pd


def check_if_player_won(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print('asd')






a =  np.array([[-1, -1, -1], [-1, -1, -1],[-1, -1, -1]], np.int32)
print('initial matrix')
print(a)

print(a[0][0])

count=1
while True:
    if count<3:
        print(" Round : "+str(count))
        player_one_input=input("Player one : -")
        player_one_split=str(player_one_input).split(',')
        a[int(player_one_split[0])][int(player_one_split[1])]=int(player_one_split[2])
        # print(player_one_input)
        print(a)

        player_two_input = input("Player two : -")
        player_two_split = str(player_two_input).split(',')
        a[int(player_two_split[0])][int(player_two_split[1])] = int(player_two_split[2])
        # print(player_two_input)
        print(a)

    else:
        print(" Round : " + str(count))
        player_one_input = input("Player one : -")
        player_one_split = str(player_one_input).split(',')
        a[int(player_one_split[0])][int(player_one_split[1])] = int(player_one_split[2])
        # print(player_one_input)
        print(a)

        player_two_input = input("Player two : -")
        player_two_split = str(player_two_input).split(',')
        a[int(player_two_split[0])][int(player_two_split[1])] = int(player_two_split[2])
        # print(player_two_input)
        print(a)



    count=count+1



