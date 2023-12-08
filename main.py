import random
def printer_func(time):
    if time <=30:
        print("Time: " + str(time) + "------------", queue[0][0],':',queue[0][1],','
              ,queue[1][0],':',queue[1][1],','
              ,queue[2][0],':',queue[2][1],')',
              '***',
              '(',resources[0], ',', resources[1], ',', resources[2], ')')



resources = [10,10,10]
p_queue = []

queue = [["P1", 4, 2, 3, 5, False],
         ["P2", 2, 3, 4, 2, False],
         ["P3", 6, 5, 3, 3, False]]

for process in queue:
    while True:
        try:
            duration = int(input("Enter the duration (1 to 7) for " + process[0] + ": "))
            if 1 <= duration <= 7:
                process[1] = duration
                break  # Break the loop if a valid input is provided
            else:
                print("Duration must be between 1 and 7. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

queue = sorted(queue, key=lambda x: x[1])
totalProcessNumber = 3
time = 1
dead_lock_counter = 0
match = False
key = True

while time <= 30:

    dead_lock_counter = 0

    for j in range(3):

        printer_func(time)
        time += 1

        source_used = [queue[0][5], queue[1][5], queue[2][5]]

        #SOURCE KULLANILMADYISA
        if match:
            if p_queue[0] == queue[j]:
                key = True
                p_queue.pop(0)
                match = False
            else:
                key = False

        if not source_used[j]:
            if key:
                #VE SOURCE YETERLIYSE
                if (queue[j][2] <= resources[0] and queue[j][3] <= resources[1] and queue[j][4] <= resources[2]):

                    resources[0] -= queue[j][2]
                    resources[1] -= queue[j][3]
                    resources[2] -= queue[j][4]

                    queue[j][5] = True
                    queue[j][1] -= 1

                    #1le doganlar icin cozum lazim
                    # if queue[j][1] == 0:
                    #     break



                #VE SOURCE YETERLI DEGIL
                else:
                    dead_lock_counter += 1
                    if dead_lock_counter == 3:
                        print("!!!!!DEADLOCK OCCURED - PROGRAM TERMINATED!!!!!")
                        exit()

        #SOURCE KULLANILDIYSA
        else:
            if key:
                #VE KALAN VAKTI 0'dan fazlaysa
                if queue[j][1] > 0:
                    queue[j][1] -= 1

                #VE KALAN VAKTI azaldiktan sonra 0 ise
                if queue[j][1] == 0:

                    match = True
                    p_queue.append(queue[(j+1)%3])

                    resources[0] += queue[j][2]
                    resources[1] += queue[j][3]
                    resources[2] += queue[j][4]

                    #additioanl print needed, to show when duration is = 0
                    printer_func(time)
                    time += 1

                    totalProcessNumber += 1
                    new_process = ["P" + str(totalProcessNumber), random.randint(1,7),
                                   random.randint(1, 7), random.randint(1, 7),
                                   random.randint(1, 7), False]
                    if new_process[1] == 1:
                        print("essek oglu essek var arkadaslar!!!!!!!1")


                    queue.pop(j)
                    queue.append(new_process)
                    queue = sorted(queue, key=lambda x: x[1])
                    break



