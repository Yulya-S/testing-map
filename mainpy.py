import matplotlib.pyplot as plt
import sys
import time

def memroy_allocation(n: int) -> float:
    result = {}
    t1 = time.perf_counter()
    for i in range(0, n):
        result.update({i : 0})
    return ( [n, (time.perf_counter()-t1) * 1000, sys.getsizeof(result)] )

values=[]
for i in range(1, 6):
    n = 10 ** i
    values.append(memroy_allocation(n))


x = []
y = [[],[]]
for i in range(len(values)):
    x.append(values[i][0])
    y[0].append(values[i][1])
    y[1].append(values[i][2])

plt.figure()

plt.subplot(221).set_title("Python work times")
plt.plot(x, y[0], label = "Python work times")
plt.subplot(222).set_title("Python real capacity")
plt.plot(x, y[1], label = "Python real capacity")

y1 = [[],[]]
file=open('values.txt', 'r', encoding='utf-8')
k= 0
x=[]
while k != '':
    k = file.readline()
    k = k.replace('\n','')
    k = k.split(' ')
    if k[0] == '':
        break
    x.append(int(k[0]))
    y1[0].append(int(k[1]))
    y1[1].append(int(k[2]))

plt.subplot(223).set_title("C++ work times")
plt.plot(x, y1[0], label = "C++ work times")
plt.subplot(224).set_title("C++ real capacity")
plt.plot(x, y1[1], label = "C++ real capacity")

plt.show()