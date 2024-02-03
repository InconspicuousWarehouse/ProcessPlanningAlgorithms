class FIFO:
    def __init__(self):
        print("FIFO algorithm")

    def FIFO(self, numbers):
        main_capacity = []
        max_capacity = 3
        not_swapped_numbers = 0
        priorities = {}  # Dictionary to store priorities for each number; the higher the number in the priority queue, the longer it waits for replacement

        for number in numbers:
            if number not in main_capacity:
                if len(main_capacity) < max_capacity:  # If there is space in the main capacity
                    main_capacity.append(number)  # Add to main_capacity
                    priorities[number] = max(priorities.values(), default=0) + 1  # Assign a new priority; each incoming number gets a priority of the highest number + 1, defaulting to 0
                else:  # If there is no space
                    # Find the index of the number with the longest unchanged time in main_capacity, i.e., the one with the lowest priority number
                    min_priority_index = min(range(len(main_capacity)), key=lambda i: priorities.get(main_capacity[i], 0))
                    min_priority_number = main_capacity[min_priority_index]

                    # Case 1: The new number has a lower priority than the number with the longest unchanged time
                    main_capacity[min_priority_index] = number
                    priorities[number] = max(priorities.values()) + 1

                    # Restore the lowest priority of the replaced number
                    priorities[min_priority_number] = min(priorities.values()) - 1
            else:
                print(f"Number {number} already exists in main_capacity, doesn't change anything in FIFO.")
                not_swapped_numbers += 1
            print(f"{main_capacity}")
        print(f"Number hasn't changed: {not_swapped_numbers} times")
