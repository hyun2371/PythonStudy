import sys
sys.setrecursionlimit(10**6)

n = int(input())
nums = list(map(int,input().split()))
nums = list(set(nums))

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(*quick_sort(nums))