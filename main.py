# OS-Project2
# Authors:
# ...
import random
def printer_func(time):
    if time != 31:
            print("Time: " + str(time) + "------------", queue[0][0],':',queue[0][1],','
                  ,queue[1][0],':',queue[1][1],','
                  ,queue[2][0],':',queue[2][1],')',
                  '***',
                  '(',resources[0], ',', resources[1], ',', resources[2], ')')

totalProcessNumber = 3
time = 1


# while not p1_check:
#     P1_duration = int(input("P1 duration: "))
#     if 0 < P1_duration < 8:
#         p1_check = True
#     else:
#         print("Number should be between 0 and 8")


resources = [10,10,10]

queue = [["P1", 4, 2, 3, 5, False],
         ["P2", 2, 3, 4, 2, False],
         ["P3", 6, 5, 3, 3, False]]

queue = sorted(queue, key=lambda x: x[1])
# total_step = int(input("enter the total number of steps: "))
is_pop = False
to_pop = []
printer_func(time)
time += 1

while time < 30:

    if is_pop:
        to_pop.reverse()
        for el in to_pop:
            queue.pop(el)
            print("popladim", to_pop)
        to_pop.clear()

    queue = sorted(queue, key=lambda x: x[1])
    is_pop = False
    for j in range(3):

        source_used = [queue[0][5], queue[1][5], queue[2][5]]

        #SOURCE KULLANILMADYISA
        if not source_used[j]:
            #VE SOURCE YETERLIYSE
            if (queue[j][2] <= resources[0] and queue[j][3] <= resources[1] and queue[j][4] <= resources[2]):

                resources[0] -= queue[j][2]
                resources[1] -= queue[j][3]
                resources[2] -= queue[j][4]

                queue[j][5] = True
                queue[j][1] -= 1

                printer_func(time)
                time += 1

            #VE SOURCE YETERLI DEGIL
            else:
                printer_func(time)
                time += 1

        #SOURCE KULLANILDIYSA
        else:
            #VE KALAN VAKTI 1 veya 0 ISE
            if (queue[j][1] == 1) or (queue[j][1] == 0):


                resources[0] += queue[j][2]
                resources[1] += queue[j][3]
                resources[2] += queue[j][4]

                if queue[j][1] == 1:
                    queue[j][1] -= 1

                is_pop = True
                to_pop.append(j)
                print("poplanacak adami bulduk: ", to_pop)
                printer_func(time)
                time += 1

                totalProcessNumber += 1
                queue.append(["P" + str(totalProcessNumber), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), False])

            #KALAN VAKTI 1 DEGILSE
            else:
                    queue[j][1] -= 1
                    printer_func(time)
                    time += 1
