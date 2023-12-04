# OS-Project2
# Authors:
# ...


import random
import time

totalProcessNumber = 3


p1_check = False
p2_check = False
p3_check = False

# while not p1_check:
#     P1_duration = int(input("P1 duration: "))
#     if 0 < P1_duration < 8:
#         p1_check = True
#     else:
#         print("Number should be between 0 and 8")
#
# while not p2_check:
#     P2_duration = int(input("P2 duration: "))
#     if 0 < P2_duration < 8:
#         p2_check = True
#     else:
#         print("Number should be between 0 and 8")
#
# while not p3_check:
#     P3_duration = int(input("P3 duration: "))
#     if 0 < P3_duration < 8:
#         p3_check = True
#     else:
#         print("Number should be between 0 and 8")

resources = [10,10,10]

queue = [["P1", 4, 2, 3, 5, False],
         ["P2", 2, 3, 4, 2, False],
         ["P3", 6, 5, 3, 3, False]]

sorted_queue = sorted(queue, key=lambda x: x[1])


for process in sorted_queue:
    print(process)



# print('(','P',sorted_queue[0][0],':',sorted_queue[0][1],',',
#       'P',sorted_queue[1][0],':',sorted_queue[1][1],',',
#       'P',sorted_queue[2][0],':',sorted_queue[2][1],')',
#       '***',
#       '(',resources[0], ',', resources[1], ',', resources[2], ')')

total_step = int(input("enter the total number of steps: "))

for i in range(total_step):
    for j in range(3):
        source_used = [sorted_queue[0][5], sorted_queue[1][5], sorted_queue[2][5]]

        #SOURCE KULLANILMADYISA
        if not source_used[j]:
            #VE SOURCE YETERLIYSE
            if sorted_queue[j][2] <= resources[0] and sorted_queue[j][3] <= resources[1] and sorted_queue[j][4] <= resources[2]:

                resources[0] -= sorted_queue[j][2]
                resources[1] -= sorted_queue[j][3]
                resources[2] -= sorted_queue[j][4]

                sorted_queue[j][5] = True
                sorted_queue[j][1] -= 1
            #VE SOURCE YETERLI DEGIL
            else:
                continue
        #SOURCE KULLANILDIYSA
        else:
            #VE KALAN VAKTI 1 ISE
            if sorted_queue[j][1] == 1:

                resources[0] += sorted_queue[j][2]
                resources[1] += sorted_queue[j][3]
                resources[2] += sorted_queue[j][4]
                queue.pop(0)
                totalProcessNumber += 1
                queue.append(["P" + str(totalProcessNumber), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), False])
                sorted_queue = sorted(queue, key=lambda x: x[1])
            #KALAN VAKTI 1 DEGILSE
            else:
                sorted_queue[j][1] -= 1



    print(sorted_queue[0][0],':',sorted_queue[0][1],','
          ,sorted_queue[1][0],':',sorted_queue[1][1],','
          ,sorted_queue[2][0],':',sorted_queue[2][1],')',
          '***',
          '(',resources[0], ',', resources[1], ',', resources[2], ')')

    # time.sleep(1)