# coding=utf-8

# Ref :http://www.cricode.com/359.html
import ctypes
testlib = ctypes.CDLL("./libpycall.so")
print testlib.foo(1, 3)

