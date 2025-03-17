import time
import matplotlib.pyplot as plt

def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])  
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

def mergesort(lst):
    if len(lst) < 2:
        return lst
    middle = len(lst) // 2
    left = mergesort(lst[:middle])
    right = mergesort(lst[middle:])
    return merge(left, right)  

seq = [12, 8, 9, 7, 1]
print("Given array is:")
print(seq)
print("\n")
print("Sorted array is:")
print(mergesort(seq))


x = list(range(1, 1000))  
plt.plot(x,[y*y for y in x])
plt.title("merge sort time complexity")
plt.xlabel("input")
plt.ylabel("time")
plt.show()


