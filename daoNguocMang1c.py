a = [1,2,3,4,5]
# Cách 1: Dùng slicing
a_dao_1 = a[::-1]
print("Cách 1 (slicing):", a_dao_1)

# Cách 2: Dùng reverse()
a_dao_2 = a.copy()
a_dao_2.reverse()
print("Cách 2 (reverse()):", a_dao_2)

# Cách 3: Dùng reversed()
a_dao_3 = list(reversed(a))
print("Cách 3 (reversed()):", a_dao_3)

# Cách 4: Dùng vòng lặp
a_dao_4 = []
for i in range(len(a)-1, -1, -1):
    a_dao_4.append(a[i])
print("Cách 4 (vòng lặp):", a_dao_4)