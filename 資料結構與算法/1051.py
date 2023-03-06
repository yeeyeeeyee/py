def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left_half, left_count = merge_sort(arr[:mid])
    right_half, right_count = merge_sort(arr[mid:])
    merged_arr = []
    i = j = count = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            count += (len(left_half) - i)
            j += 1
    merged_arr += left_half[i:]
    merged_arr += right_half[j:]
    return merged_arr, count + left_count + right_count
def count_inversions(arr):
    _, count = merge_sort(arr)
    return count

# 讀取 n
n = int(sys.stdin.readline())

# 讀取數列 A 的元素
arr = list(map(int, sys.stdin.readline().split()))

# 計算逆序數對總數並輸出結果
print(count_inversions(arr))