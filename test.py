import numpy
import socket

print(numpy.frombuffer(b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00', dtype=numpy.uint8))
print(type(b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'), '\n')
x = numpy.array([[0, 1], [2, 3]])
print("array", x, '\n')

hold = str(x.tobytes(), encoding=utf-8)
print("tostring", hold)
print("tostring", type(hold), '\n')

hold = hold.encode('utf-8')
print("encoded", hold)
print("tostring", type(hold), '\n')

hold2 = hold.decode('utf-8')
print("decoded", hold2)
print(type(hold2), '\n')

hold2 = numpy.frombuffer(hold2, dtype=numpy.uint8)
print("frombuffer", hold2)



