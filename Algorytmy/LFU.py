class LFU:
    def __init__(self):
        print("LFU algorithm")

    def LFU(self, numbers):
        main_capacity = []
        max_capacity = 3
        not_swapped_numbers = 0
        priorities = {}  # Dictionary to store priorities for each number; the higher the priority key in the priority queue, the longer it waits for replacement
        repetitive_count = {}

        for number in numbers:
            repetitive_count.setdefault(number, 0)  # Key for each number automatically set to 0
            if number not in main_capacity:
                if len(main_capacity) < max_capacity:  # If there is space in the main capacity
                    main_capacity.append(number)  # Add to main_capacity
                    priorities[number] = max(priorities.values(), default=0) + 1# Assign a new priority; each incoming number gets a priority of the highest number + 1, defaulting to 0
                else:  # If there is no space
                    # Find numbers with the lowest repetitive_count key
                    min_repetitive_counts = [repetitive_count.get(num, 0) for num in main_capacity]
                    min_repetitive_indices = [i for i, count in enumerate(min_repetitive_counts) if count == min(min_repetitive_counts)]

                    # Find the number that has been in main_capacity the longest
                    oldest_number_index = min(range(len(main_capacity)), key=lambda i: priorities.get(main_capacity[i], 0))


                    # If there are at least two numbers with the lowest repetitive_count key, choose the one that has been in main_capacity the longest
                    if len(min_repetitive_indices) > 1:
                        # Check if the number with the lowest repetitive_count key has been in main_capacity the longest
                        if oldest_number_index in min_repetitive_indices:
                            min_repetitive_index = oldest_number_index
                        else:
                            # If not, find the index of the number that has been in main_capacity the longest
                            oldest_index_in_repetitive = min(min_repetitive_indices, key=lambda i: priorities.get(main_capacity[i], 0))
                            min_repetitive_index = oldest_index_in_repetitive
                    else:
                        min_repetitive_index = min_repetitive_indices[0]

                    min_repetitive_number = main_capacity[min_repetitive_index]

                    # Check if the number we want to insert already exists in main_capacity
                    if number != min_repetitive_number:
                        # Replace the number with the lowest repetitive_count key with the new number
                        main_capacity[min_repetitive_index] = number
                        priorities[number] = max(priorities.values()) + 1

                        # Remove the old number from the dictionary
                        del repetitive_count[min_repetitive_number]

                        # Restore the lowest priority of the replaced number
                        priorities[min_repetitive_number] = min(priorities.values()) - 1
                    else:
                        # Update only the number in the repetitive_count dictionary
                        repetitive_count[number] += 1
                        print(f"Number {number} already exists in main_capacity, its repetitive_count +1 ")
            else:
                if number in main_capacity:
                    repetitive_count[number] += 1
                    not_swapped_numbers += 1
                    print(f"Number {number} already exists in main_capacity, its repetitive_count +1 ")
            print(f"{main_capacity} {repetitive_count}")
        print(f"Number hasn't changed: {not_swapped_numbers} times")
