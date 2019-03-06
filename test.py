import numpy
import socket

x = numpy.array([[0, 1], [2, 3]])
print("array", x)

hold = str(x.tostring())
print("tostring", hold)
print("tostring", type(hold))

hold = hold.encode('utf-8')
print("encoded", hold)

hold2 = hold.decode('utf-8')
print("decoded", hold2)
print(type(hold2))

hold2 = numpy.fromstring(hold2, dtype='int8')
print("fromstring", hold2)



