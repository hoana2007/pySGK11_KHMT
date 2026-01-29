#Đọc dữ liệu đơn giản
fname = "dulieu.inp"
f = open(fname, "r", encoding="UTF-8")
#daySo = f.readlines()
#Đây là 1 danh sách:
#print(daySo)
#Đây là đọc từng dòng:
dayA = []
for line in f:
    dayA.append(line)
f.close()
print(dayA)
# for i in range(len(dayA)):
#     print(dayA[i])