def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        # Find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: {arr}")
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original Array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted Array:", sorted_arr)
