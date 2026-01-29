fname = "bdiem.inp"
f = open(fname, "r", encoding="UTF-8")
hs = f.readline()
a = hs.split()
print(a[0], float(a[1]) + 100)