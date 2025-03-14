# -*- coding: utf-8 -*-
from py4hw.base import *
from py4hw.logic import *
import py4hw.debug

sys = HWSystem()

a = sys.wire("a", 32)
b = sys.wire("b", 32)
c = sys.wire("c", 32)
r1 = sys.wire("r", 32)
r2 = sys.wire("r2", 32)

Add(sys, "add1", a,b, r1)
Add(sys, "add2", r1, c, r2)

Constant(sys, "a", 10, a)
Constant(sys, "b", 20, b)
Constant(sys, "c", 5, c)
Scope(sys, "r2", r2)

py4hw.debug.printHierarchy(sys)

print('RESET')
sim = sys.getSimulator()

print()
print('CLK')
sim.clk(1)


