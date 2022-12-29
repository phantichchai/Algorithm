class MinHeap:
    # 1834. Single-Threaded CPU
    # Time complexity: O(Nlog(N))
    # Space complexity: O(N) 
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # initialize variable for contain each value by:
        #   output: return out put that store the order of process that execute
        #   current_time: the current time of the processes
        #   i: the current index of the processes
        #   next_tasks: min heap for contain all the tasks when the current time is past enqueue time
        output = []
        current_time = 0
        i = 0
        next_tasks = []
        
        # sorted the tasks by enqueue time and store value in the 2D-array by:
        tasks = sorted((enqueue_time, process_time, i) for i, (enqueue_time, process_time) in enumerate(tasks))

        # iterative untial not have tasks in min heap or the current index less than number of all tasks
        while next_tasks or i < len(tasks):

            # check that is min heap empty or not and the current time is less than the enqueue time at the current index
            if not next_tasks and current_time < tasks[i][0]:
                # change current time equal to the enqueue time at the current index
                current_time = tasks[i][0]
            
            # iterative for all tasks when that enqueue time task is less than equal the current time and check that current index is less than number of all tasks 
            while i < len(tasks) and tasks[i][0] <= current_time:
                _, process_time, original_index = tasks[i]
                # heap push the process time and original index to the min heap data 'next_tasks'
                heappush(next_tasks, (process_time, original_index))
                # update current index
                i += 1

            # heap pop and store value to process time and original index
            process_time, original_index = heappop(next_tasks)
            # update current time by add process time
            current_time += process_time
            # append the original index to the output
            output.append(original_index)
        return output