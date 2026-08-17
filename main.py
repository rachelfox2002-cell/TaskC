import random
import time

def bubbleSort(arr, order="asc"):  
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if order == "asc":
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
                    swapped = True
            else:
                 if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
                    swapped = True
        if (swapped == False):
            break
    return arr

def heapify(arr, n, i, order="asc"):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2
    
    if order == "asc":
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
    else:
        if l < n and arr[l] < arr[largest]:
            largest = l
        if r < n and arr[r] < arr[largest]:
            largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n , largest, order)

def heapSort(arr, order="asc"):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n , i, order)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, order)
        
    return arr

dataset_sizes = [1000,5000, 15000, 20000, 25000, 30000, 35000, 40000]
num_of_experiments = 3

Orders = ["asc", "desc"]

def generate_dataset(n):
    return [random.randint(0, 100000) for i in range(n)]

def run_experiment(dataset, algorithm, order):
    data = list(dataset)
    start = time.thread_time_ns()
    algorithm(data, order)
    end = time.thread_time_ns()
    duration_ms = (end - start)/1000000
    return duration_ms

def run_sample_experiment(no_experiments, dataset, algorithm, order):
    total = 0
    for i in range(no_experiments):
        duration_ms = run_experiment(dataset, algorithm, order)
        print ("Run", i + 1, duration_ms)
        total = total + duration_ms
    avg = total / no_experiments
    print("Average", avg)
    return avg

def main():
    for size in dataset_sizes:
        dataset = generate_dataset(size)

        for order in Orders:
            bubble_average = run_sample_experiment(num_of_experiments, dataset, bubbleSort, order)
            heap_average = run_sample_experiment(num_of_experiments, dataset, heapSort, order)
            print(size, order, bubble_average, heap_average)

main()


