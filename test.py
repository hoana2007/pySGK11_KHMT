#Thuật toán sắp xếp nổi bọt
# def bubbleSort(A):
#     n = len(A)
#     global dem
#     dem = 0
#     for i in range(n -1):
#         for j in range(n -1-i):
#             if (A[j] > A[j+1]):
#                 A[j], A[j+1] = A[j + 1], A[j]
#                 dem += 1
#TT Quicksort
def quicksort(A):
    global dem
    dem = 0
    if len(A) < 2:
        return A
        dem = 1
    else:
        import random
        pivot = A[random.randint(0, len(A) - 1)]
        less = [i for i in A if i < pivot]
        equal_nums = [i for i in A if i == pivot]
        greater = [i for i in A if i > pivot]
        dem += 1
        return quicksort(less) + equal_nums + quicksort(greater)

#Đọc dữ liệu đơn giản
fname = "dayso.inp"
f = open(fname, "r", encoding="UTF-8")

dayA = [int(x) for x in f.read().split()]
f.close()
print(dayA)
#bubbleSort(dayA)
quicksort(dayA)
print(dayA)
print(f"So buoc hoan doi: {dem}")
#Kiểm tra dung lượng tạm của file:
import os
file_size = os.path.getsize(fname)
print(f"Kích thước của file: {file_size} bytes")