## Temp file to test expected functionality of chips, as they are developed

import builtInChips

chipToTest = "NOT16"

testChip = eval("builtInChips." + chipToTest + "()")

## One 1-bit input
# result1 = testChip.eval(False)
# result2 = testChip.eval(True)

# print("0: ", result1)
# print("1: ", result2)

## Two 1-bit inputs
# result1 = testChip.eval(False, False)
# result2 = testChip.eval(False, True)
# result3 = testChip.eval(True, False)
# result4 = testChip.eval(True, True)

# print("00: ", result1)
# print("01: ", result2)
# print("10: ", result3)
# print("11: ", result4)

## Mux
# result1 = testChip.eval(False, False, False)
# result2 = testChip.eval(False, False, True)
# result3 = testChip.eval(False, True, False)
# result4 = testChip.eval(False, True, True)
# result5 = testChip.eval(True, False, False)
# result6 = testChip.eval(True, False, True)
# result7 = testChip.eval(True, True, False)
# result8 = testChip.eval(True, True, True)

# print("sel, a, b")
# print("0, 0, 0: ", result1)
# print("0, 0, 1: ", result2)
# print("0, 1, 0: ", result3)
# print("0, 1, 1: ", result4)
# print("1, 0, 0: ", result5)
# print("1, 0, 1: ", result6)
# print("1, 1, 0: ", result7)
# print("1, 1, 1: ", result8)

## DMux
# result1 = testChip.eval(False, False)
# result2 = testChip.eval(False, True)
# result3 = testChip.eval(True, False)
# result4 = testChip.eval(True, True)

# print("sel, in")
# print("0, 0: ", result1)
# print("0, 1: ", result2)
# print("1, 0: ", result3)
# print("1, 1: ", result4)

## Not16
result1 = testChip.eval(builtInChips.boolBus.stringToBus("0000000000000000"))
result2 = testChip.eval(builtInChips.boolBus.stringToBus("1111111111111111"))
result3 = testChip.eval(builtInChips.boolBus.stringToBus("1111111100000000"))
result4 = testChip.eval(builtInChips.boolBus.stringToBus("1111000011110000"))

print("0000000000000000", builtInChips.boolBus.toString(result1))
print("1111111111111111", builtInChips.boolBus.toString(result2))
print("1111111100000000", builtInChips.boolBus.toString(result3))
print("1111000011110000", builtInChips.boolBus.toString(result4))
