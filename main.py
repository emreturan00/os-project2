# OS-Project2
# Authors:
# ...


import random
import time

totalProcessNumber = 3
queueColumn = 1
sourceFlag1 = 0
sourceFlag2 = 0
sourceFlag3 = 0

p1_check = False
p2_check = False
p3_check = False

while not p1_check:
    P1_duration = int(input("P1 duration: "))
    if 0 < P1_duration < 8:
        p1_check = True
    else:
        print("Number should be between 0 and 8")

while not p2_check:
    P2_duration = int(input("P2 duration: "))
    if 0 < P2_duration < 8:
        p2_check = True
    else:
        print("Number should be between 0 and 8")

while not p3_check:
    P3_duration = int(input("P3 duration: "))
    if 0 < P3_duration < 8:
        p3_check = True
    else:
        print("Number should be between 0 and 8")

resources = [10,10,10]

queue = [[1, P1_duration, random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)],
         [2, P2_duration, random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)],
         [3, P3_duration, random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)],]

sorted_queue = sorted(queue, key=lambda x: x[1])

for process in sorted_queue:
    print(process)



print('(','P',sorted_queue[0][0],':',sorted_queue[0][1],',',
      'P',sorted_queue[1][0],':',sorted_queue[1][1],',',
      'P',sorted_queue[2][0],':',sorted_queue[2][1],')',
      '***',
      '(',resources[0], ',', resources[1], ',', resources[2], ')')

for i in range(4):

    if sorted_queue[0][2] <= resources[0] and sorted_queue[0][3] <= resources[1] and sorted_queue[0][4] <= resources[2] and queueColumn % 3 == 1:

        if sourceFlag1 == 0:

            resources[0] -= sorted_queue[0][2]
            resources[1] -= sorted_queue[0][3]
            resources[2] -= sorted_queue[0][4]
            sourceFlag1 = 1

        sorted_queue[0][1] -= 1

        if sorted_queue [0][1] != 0:

            queueColumn += 1
        else:

            sourceFlag1 = 0
            resources[0] += sorted_queue[0][2]
            resources[1] += sorted_queue[0][3]
            resources[2] += sorted_queue[0][4]
            sorted_queue.pop(0)
            totalProcessNumber += 1
            sorted_queue.append([totalProcessNumber, random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)])
            sorted_queue = sorted(queue, key=lambda x: x[1])
            queueColumn += 1

    elif sorted_queue[1][2] <= resources[0] and sorted_queue[1][3] <= resources[1] and sorted_queue[1][4] <= resources[2] and queueColumn % 3 == 2:

        if sourceFlag2 == 0:

            resources[0] -= sorted_queue[1][2]
            resources[1] -= sorted_queue[1][3]
            resources[2] -= sorted_queue[1][4]
            sourceFlag2 = 1

        sorted_queue[1][1] -= 1

        if sorted_queue [1][1] != 0:

            queueColumn += 1
        else:

            sourceFlag2 = 0
            resources[0] += sorted_queue[1][2]
            resources[1] += sorted_queue[1][3]
            resources[2] += sorted_queue[1][4]
            sorted_queue.pop(1)
            totalProcessNumber += 1
            sorted_queue.append([totalProcessNumber, random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)])
            sorted_queue = sorted(queue, key=lambda x: x[1])
            queueColumn += 1

    elif sorted_queue[2][2] <= resources[0] and sorted_queue[2][3] <= resources[1] and sorted_queue[2][4] <= resources[2] and queueColumn % 3 == 0:

        if sourceFlag3 == 0:

            resources[0] -= sorted_queue[2][2]
            resources[1] -= sorted_queue[2][3]
            resources[2] -= sorted_queue[2][4]
            sourceFlag3 = 1

        sorted_queue[2][1] -= 1

        if sorted_queue [2][1] != 0:

            queueColumn += 1
        else:

            sourceFlag3 = 0
            resources[0] += sorted_queue[2][2]
            resources[1] += sorted_queue[2][3]
            resources[2] += sorted_queue[2][4]
            sorted_queue.pop(2)
            totalProcessNumber += 1
            sorted_queue.append([totalProcessNumber, random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)])
            sorted_queue = sorted(queue, key=lambda x: x[1])
            queueColumn += 1

    print('(','P',sorted_queue[0][0],':',sorted_queue[0][1],',',
          'P',sorted_queue[1][0],':',sorted_queue[1][1],',',
          'P',sorted_queue[2][0],':',sorted_queue[2][1],')',
          '***',
          '(',resources[0], ',', resources[1], ',', resources[2], ')')

    time.sleep(1)