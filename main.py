import random


def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break

    print(" Process No. Process Size	 Block no.")
    for i in range(n):
        print(" ", i + 1, "		 ", processSize[i],
              "		 ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


if __name__ == '__main__':
    blockSize = []
    processSize = []
    disk = 65536
    mem_razdels = []
    control = []
    id_ = 0
    flag = 0
    yacheyki = []

    razdel_count = int(input('На сколько разделов вы хотите разделить память? -> '))
    for i in range(1, (razdel_count + 1)):

        razdels_size = int(input(f'Введите размер раздела памяти(байты) {i} '))
        control.append(razdels_size)
        if razdels_size <= disk and sum(control) != disk:
            mem_razdels.append(razdels_size)
        elif razdels_size == disk and sum(control) == disk:
            mem_razdels.append(razdels_size)
            break

        elif razdels_size > disk:
            print('Столько памяти нет(Максимум 65536 байт )')
            control.pop(0)
            id_ = i
            flag = 1
            break
        else:
            break
    if flag == 1:
        for j in range(id_, (razdel_count + 1)):
            razdels_size = int(input(f'Введите размер раздела памяти(байты) {j} '))
            control.append(razdels_size)
            if razdels_size <= disk and sum(control) != disk:
                mem_razdels.append(razdels_size)
            elif razdels_size == disk and sum(control) == disk:
                mem_razdels.append(razdels_size)
                break
            elif sum(control) == disk:
                mem_razdels.append(razdels_size)
                break
            else:
                break

    count = len(mem_razdels)
    while count != 0:
        for x in mem_razdels:
            y = (random.randint(0, disk - 1))
            if (y+x) <= disk:
                yacheyka = [y, y+x]
                yacheyki.append(yacheyka)
                count = count - 1
                block = (y+x) - y
                blockSize.append(block)

    task = int(input('Введите кол-во задач -> '))
    for i in range(1, task + 1):
        task_size = int(input(f'Введите размер задачи(байты) {i} '))
        processSize.append(task_size)
    # processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)

    firstFit(blockSize, m, processSize, n)

    print(f'Задействованная локация памяти {yacheyki}')


