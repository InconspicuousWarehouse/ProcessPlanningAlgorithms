import random
from Algorytmy.FCFS import FCFS
from Algorytmy.LCFS import LCFS
from Algorytmy.FIFO import FIFO
from Algorytmy.LFU import LFU

############################# initialize processes ###################################
def getProcesses():
    return\
        [
            ("P1", 0, 4),# (name, arrival time, execution time)
            ("P2", 3, 5),
            ("P5", 20, 4),
            ("P4", 8, 1),
            ("P3", 2, 6),

        ]
############################# processes randomly assigned #############################
# def getProcesses(num_processes=20, max_arrival_time=20, max_execution_time=200):
#     processes = []
#     for i in range(1, num_processes + 1):
#         arrival_time = random.randint(0, max_arrival_time)
#         execution_time = random.randint(1, max_execution_time)
#         process = (f"P{i}", arrival_time, execution_time)
#         processes.append(process)
#     return processes
#
# def displayProcesses(processes):
#     for process in processes:
#         print(f"Process {process[0]} - Arrival Time: {process[1]}, Execution Time: {process[2]}")

get_processes = getProcesses()
# displayProcesses(get_processes)#displaying randomly assigned processes
print()
################################# List of numebrs ######################################
def List_of_numbers():
    return [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2]

############################# randomly generated numbers #############################
# def List_of_numbers(number_of_data=50, variety_of_data=10):
#     List = []
#     for i in range(0,number_of_data):
#         data = random.randint(0, variety_of_data)
#         List.append(data)
#     return List
#
# def display_List_of_numbers(List):
#     print(list(List))
#     print()

get_list_of_numbers = List_of_numbers()
# display_List_of_numbers(get_list_of_numbers)#displaying randomly generated numbers

########################### Starting FCFS ###########################
fcfs_processes = get_processes.copy()
fcfs = FCFS()
fcfs.FCFS(fcfs_processes)
print("")
############################ Starting LCFS ##########################
lcfs_processes = get_processes.copy()
lcfs = LCFS()
lcfs.LCFS(lcfs_processes)
########################### Starting FIFO ###########################
fifo_processes = get_list_of_numbers.copy()
fifo = FIFO()
fifo.FIFO(fifo_processes)
print()
########################### Starting LFU ############################
lfu_processes = get_list_of_numbers.copy()
lfu = LFU()
lfu.LFU(lfu_processes)
