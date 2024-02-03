class FCFS:
    def __init__(self):
        print("FCFS algorithm")

    def FCFS(self, processes):
        queue = []
        count = 0
        total_wait_time = 0
        current_time = 0
        total_execution_time = 0
        execution_timeline = []  # List to store information about process execution over time
        execution_order = []  # List to store the order of executed processes
        wait_times = []
        remaining_processes = len(processes)

        while processes or queue:
            # Check for arrived processes and add them to the queue
            arrived_processes = [p for p in processes if p[1] <= current_time]
            queue.extend(arrived_processes)
            processes = [p for p in processes if p not in arrived_processes]

            # Sort the queue by arrival time
            queue = sorted(queue, key=lambda x: x[1])

            if queue:
                # Select the process with the lowest arrival time in the current second
                current_process = queue[0]
                process_name, arrival_time, execution_time = current_process
                start_time = max(current_time, arrival_time)
                end_time = start_time + execution_time

                wait_time = start_time - arrival_time
                execution_timeline.append((process_name, wait_time, start_time, end_time))
                execution_order.append(process_name)

                current_time = end_time
                total_execution_time = current_time
                queue.pop(0)

                wait_times.append(wait_time)
                remaining_processes -= 1

            else:
                current_time += 1

        # Print execution details
        for process in execution_timeline:
            print(
                f"Executing process: {process[0]}, Wait time: {process[1]}, Start time: {process[2]}, End of process: {process[3]}")

        print(f"Time of entire process: {total_execution_time}ms")

        # Print just the names of processes and the order in which they were executed
        print("Execution order:", ", ".join(execution_order))

        # Average wait time
        for time in wait_times:
            total_wait_time += time
            count += 1

        average_wait_time = float(total_wait_time / count)
        print(f"Average wait time: {average_wait_time:.2f}")
