# from __future__ import division

# def_op('STOP_CODE', 0)
# ignore

# def_op('POP_TOP', 1)
a()

# def_op('ROT_TWO', 2)
(a, b) = (b, a)

# def_op('ROT_THREE', 3)
(a, a, a) = (a, a, a)

# def_op('DUP_TOP', 4)
exec 1

# def_op('ROT_FOUR', 5)
a[2:4] += 'abc'

# def_op('NOP', 9)
# ignore

# def_op('UNARY_POSITIVE', 10)
+ a

# def_op('UNARY_NEGATIVE', 11)
- a

# def_op('UNARY_NOT', 12)
not a

# def_op('UNARY_CONVERT', 13)
a = `a`

# def_op('UNARY_INVERT', 15)
a = ~a

# def_op('BINARY_POWER', 19)
a ** 1

# def_op('BINARY_MULTIPLY', 20)
a * 1

# def_op('BINARY_DIVIDE', 21)
a / 1

# def_op('BINARY_MODULO', 22)
a % 1

# def_op('BINARY_ADD', 23)
a + 1

# def_op('BINARY_SUBTRACT', 24)
a - 1

# def_op('BINARY_SUBSCR', 25)
a[1]

# def_op('BINARY_FLOOR_DIVIDE', 26)
a // 1

# def_op('BINARY_TRUE_DIVIDE', 27)
# add 'from __future__ import division' to header

# def_op('INPLACE_FLOOR_DIVIDE', 28)
a //= 1

# def_op('INPLACE_TRUE_DIVIDE', 29)
# add 'from __future__ import division' to header

# def_op('SLICE+0', 30)
a[:]

# def_op('SLICE+1', 31)
a[1:]

# def_op('SLICE+2', 32)
a[:2]

# def_op('SLICE+3', 33)
a[1:2]

# def_op('STORE_SLICE+0', 40)
a[:] = 1

# def_op('STORE_SLICE+1', 41)
a[1:] = 1

# def_op('STORE_SLICE+2', 42)
a[:2] = 1

# def_op('STORE_SLICE+3', 43)
a[1:2] =1

# def_op('DELETE_SLICE+0', 50)
del a[:]

# def_op('DELETE_SLICE+1', 51)
del a[1:]

# def_op('DELETE_SLICE+2', 52)
del a[:2]

# def_op('DELETE_SLICE+3', 53)
del a[1:2]

# def_op('STORE_MAP', 54)
{"1": 1}

# def_op('INPLACE_ADD', 55)
a += 1

# def_op('INPLACE_SUBTRACT', 56)
a -= 1

# def_op('INPLACE_MULTIPLY', 57)
a *= 1

# def_op('INPLACE_DIVIDE', 58)
a /= 1

# def_op('INPLACE_MODULO', 59)
a %= 1

# def_op('STORE_SUBSCR', 60)
a[1] = 1

# def_op('DELETE_SUBSCR', 61)
del a[1]

# def_op('BINARY_LSHIFT', 62)
a << 1

# def_op('BINARY_RSHIFT', 63)
a >> 1

# def_op('BINARY_AND', 64)
a & 1

# def_op('BINARY_XOR', 65)
a ^ 1

# def_op('BINARY_OR', 66)
a | 1

# def_op('INPLACE_POWER', 67)
a **= 1

# def_op('GET_ITER', 68)
for i in a:
    pass

# def_op('PRINT_EXPR', 70)
# ignore

# def_op('PRINT_ITEM', 71)
print(1)

# def_op('PRINT_NEWLINE', 72)
print(1)

# def_op('PRINT_ITEM_TO', 73)
print >> fd, 1

# def_op('PRINT_NEWLINE_TO', 74)
print >> fd, 1

# def_op('INPLACE_LSHIFT', 75)
a <<= 1

# def_op('INPLACE_RSHIFT', 76)
a >>= 1

# def_op('INPLACE_AND', 77)
a &= 1

# def_op('INPLACE_XOR', 78)
a ^= 1

# def_op('INPLACE_OR', 79)
a |= 1

# def_op('BREAK_LOOP', 80)
while True:
    break

# def_op('WITH_CLEANUP', 81)
with a:
    pass

# def_op('LOAD_LOCALS', 82)
class a:
    pass

# def_op('RETURN_VALUE', 83)
def a():
    return

# def_op('IMPORT_STAR', 84)
from module import *

# def_op('EXEC_STMT', 85)
exec 1

# def_op('YIELD_VALUE', 86)
def a():
    yield 1

# def_op('POP_BLOCK', 87)
while True:
    pass

# def_op('END_FINALLY', 88)
with a:
    pass

# def_op('BUILD_CLASS', 89)
class a:
    pass

# name_op('STORE_NAME', 90)       # Index in name list
a = 1

# name_op('DELETE_NAME', 91)      # ""
del a

# def_op('UNPACK_SEQUENCE', 92)   # Number of tuple items
a, b = 1, 2

# jrel_op('FOR_ITER', 93)
for i in a:
    pass

# def_op('LIST_APPEND', 94)
[i for i in a]

# name_op('STORE_ATTR', 95)       # Index in name list
a.a = 1

# name_op('DELETE_ATTR', 96)      # ""
del a.a

# name_op('STORE_GLOBAL', 97)     # ""
def a():
    global aa
    aa = 1

# name_op('DELETE_GLOBAL', 98)    # ""
def a():
    global aa
    del aa

# def_op('DUP_TOPX', 99)          # number of items to duplicate
b[a] += 1

# def_op('LOAD_CONST', 100)       # Index in const list
123

# name_op('LOAD_NAME', 101)       # Index in name list
a

# def_op('BUILD_TUPLE', 102)      # Number of tuple items
(a, )

# def_op('BUILD_LIST', 103)       # Number of list items
[]

# def_op('BUILD_SET', 104)        # Number of set items
{1}

# def_op('BUILD_MAP', 105)        # Number of dict entries (upto 255)
{}

# name_op('LOAD_ATTR', 106)       # Index in name list
a.a

# def_op('COMPARE_OP', 107)       # Comparison operator
a == a

# name_op('IMPORT_NAME', 108)     # Index in name list
import a

# name_op('IMPORT_FROM', 109)     # Index in name list
from a import b

# jrel_op('JUMP_FORWARD', 110)    # Number of bytes to skip
if True:
    pass

# jabs_op('JUMP_IF_FALSE_OR_POP', 111) # Target byte offset from beginning of code
0 and False

# jabs_op('JUMP_IF_TRUE_OR_POP', 112)  # ""
0 or False


# jabs_op('JUMP_ABSOLUTE', 113)        # ""
def a():
    if b:
        if c:
            print('')

# jabs_op('POP_JUMP_IF_FALSE', 114)    # ""
if True:
    pass

# jabs_op('POP_JUMP_IF_TRUE', 115)     # ""
if not True:
    pass

# name_op('LOAD_GLOBAL', 116)     # Index in name list
def a():
    global b
    return b

# jabs_op('CONTINUE_LOOP', 119)   # Target address
while True:
    try: 
        continue
    except: 
        pass


# jrel_op('SETUP_LOOP', 120)      # Distance to target address
while True:
    pass

# jrel_op('SETUP_EXCEPT', 121)    # ""
# jrel_op('SETUP_FINALLY', 122)   # ""
try:
    pass
except:
    pass
finally:
    pass

# def_op('LOAD_FAST', 124)        # Local variable number
def a():
    aa = 1
    return aa

# def_op('STORE_FAST', 125)       # Local variable number
def a():
    aa = 1

# def_op('DELETE_FAST', 126)      # Local variable number
def a():
    aa = 1
    del aa

# def_op('RAISE_VARARGS', 130)    # Number of raise arguments (1, 2, or 3)
raise

# def_op('CALL_FUNCTION', 131)    # #args + (#kwargs << 8)
a()

# def_op('MAKE_FUNCTION', 132)    # Number of args with default values
def a():
    pass

# def_op('BUILD_SLICE', 133)      # Number of items
a[::]

# def_op('MAKE_CLOSURE', 134)
# def_op('LOAD_CLOSURE', 135)
# def_op('LOAD_DEREF', 136)
# def_op('STORE_DEREF', 137)
def f():
    a = 1
    def g():
        return a + 1
    return g()


# def_op('CALL_FUNCTION_VAR', 140)     # #args + (#kwargs << 8)
a(*args)

# def_op('CALL_FUNCTION_KW', 141)      # #args + (#kwargs << 8)
a(**kwargs)

# def_op('CALL_FUNCTION_VAR_KW', 142)  # #args + (#kwargs << 8)
a(*args, **kwargs)

# jrel_op('SETUP_WITH', 143)
with a:
    pass

# def_op('EXTENDED_ARG', 145)
# ignore

# def_op('SET_ADD', 146)
{i for i in a}

# def_op('MAP_ADD', 147)
{i:i for i in a}
