#Sao anh không về chơi thôn Vỹ
#Nhìn nắng hàng cau nắng mới lên
fname = open("data.inp", "r", encoding="UTF-8")
data = fname.readlines()
fname.close()
def nhapDL(data):
    ten = []
    diem = []
    hs = []
    for line in data:
        L = line.split()
        ten = L[0]
        diem = L[1]
        hs.append((ten, diem))
    return hs

def bubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j][1] > A[j + 1][1]:
                A[j], A[j+1] = A[j + 1], A[j]

hs = nhapDL(data)
print(hs)
bubbleSort(hs)
print(hs)