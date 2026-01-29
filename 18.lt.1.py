marks = []
line = input("Nhập điểm các môn, cách nhau bởi dấu cách: ")
marks = [float(x) for x in line.split()]
total = 0
Min = marks[0]
Max = marks[0]
for m in marks:
    total += m
    if m < Min:
        Min = m
    if m > Max:
        Max = m
print("Điểm đã nhập", marks)
print("Điểm trung bình:", round(total / len(marks),2))
print("Điểm cao nhất:", Max)
print("Điểm thấp nhất:", Min)

#a. Điểm đầu tiên và điểm cuối cùng
print("Điểm đầu tiên:", marks[0])
print("Điểm cuối cùng:", marks[-1])

#b. Cho phép người dùng nhập nhiều lần n để kiểm tra
