from hw_9_task_1 import find_coins_greedy
from hw_9_task_2 import find_min_coins
import timeit



if __name__ == '__main__':
    task_1 = timeit.timeit(lambda: find_coins_greedy(100000), number=5)
    task_2 = timeit.timeit(lambda: find_min_coins(100000), number=5)

    print(f"| {'Algorithm':<30} | {'Greedy algorithm':<30} | {'Dynamic programming':<30} |")
    print(f"| {'-' * 30} | {'-' * 30} | {'-' * 30} |")
    print(f"| {f'Time':<30} | {task_1:30.5f} | {task_2:30.5f} |")