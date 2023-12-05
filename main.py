from tabulate import tabulate  # Perlu instalasi library tabulate
import time
import memory_profiler
import numpy as np

from Greedy import main as greedy_algo
from BranchnBound import main as branchnbound_algo 

def calculate_algo(algorithm, *args):
    start_time = time.time()
    memory_usage = memory_profiler.memory_usage((algorithm, args), interval=0.1)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Ubah ke milidetik
    max_memory_usage = max(memory_usage)
    return execution_time, max_memory_usage



if __name__ == "__main__":
    scale = [20, 200, 2000]

    for files in scale:
        if files == 20:
            file_name = "Small"
        elif files == 200:
            file_name = "Medium"
        else:
            file_name = "Large"

        with open(f'DataSet_{file_name}.txt') as file:
            size  = scale
            subset = []
            costs =  []
            
            #asign darta in file to list
            file.readline()
            for line in file:
                subset.append(np.array(line.strip().split(),dtype=int))
            costs = np.array(subset.pop(), dtype=int)

        execution_time_branch, max_memory_usage_branch = calculate_algo(branchnbound_algo,files, subset,costs)
        execution_time_greedy, max_memory_usage_greedy = calculate_algo(greedy_algo,files, subset,costs)

        print("\n======================================")
        print(f'{file_name.upper()}')
        print("======================================")
        print(f'Algo   | Execution Time |  Memory Use')
        print(f'Greedy | {execution_time_greedy:.5f}      | {max_memory_usage_greedy:.5f}    ')
        print(f'Branch | {execution_time_branch:.5f}      | {max_memory_usage_branch:.5f}    ')


