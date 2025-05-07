## Test dev file to test expected functionality of chips, as they are developed

import builtInChips

def test_Nand():
    print("Testing Nand")
    ## set up nand chip with multiple inputs
    testChip = builtInChips.Nand()
    
    inputs = {"a": False, "b": False}
    testChip.updateInputs(inputs)
    testChip.eval()
    assert testChip.outputs["out"] == True, "Input 00 should be 1"
    
    inputs = {"a": False, "b": True}
    testChip.updateInputs(inputs)
    testChip.eval()
    assert testChip.outputs["out"] == True, "Input 01 should be 1"
    
    inputs = {"a": True, "b": False}
    testChip.updateInputs(inputs)
    testChip.eval()
    assert testChip.outputs["out"] == True, "Input 10 should be 1"
    
    inputs = {"a": True, "b": True}
    testChip.updateInputs(inputs)
    testChip.eval()
    assert testChip.outputs["out"] == False, "Input 11 should be 0"
    
def test_Not():
    print("Testing Not")
    testChip = builtInChips.Not()
    
    inputs = {"in": False}
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 0 should be 1"
    
    inputs = {"in": True}
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 1 should be 0"

def test_And():
    print("Testing And")
    testChip = builtInChips.And()
    
    inputs = {
        "a": False,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 00 should be 0"
    
    inputs = {
        "a": False,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 01 should be 0"
    
    inputs = {
        "a": True,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 10 should be 0"
    
    inputs = {
        "a": True,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 11 should be 1"
    
def test_Or():
    print("Testing Or")
    testChip = builtInChips.Or()
    
    inputs = {
        "a": False,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 00 should be 0"
    
    inputs = {
        "a": False,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 01 should be 1"
    
    inputs = {
        "a": True,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 10 should be 1"
    
    inputs = {
        "a": True,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 11 should be 1"

def test_Xor():
    print("Testing Xor")
    testChip = builtInChips.Xor()
    
    inputs = {
        "a": False,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 00 should be 0"
    
    inputs = {
        "a": False,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 01 should be 1"
    
    inputs = {
        "a": True,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 10 should be 1"
    
    inputs = {
        "a": True,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 11 should be 0"
    
def test_Mux():
    print("Testing Mux")
    testChip = builtInChips.Mux()
    
    inputs = {
        "sel": False,
        "a": False,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 000 should be 0"
    
    inputs = {
        "sel": False,
        "a": False,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 001 should be 0"
    
    inputs = {
        "sel": False,
        "a": True,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 010 should be 1"
    
    inputs = {
        "sel": False,
        "a": True,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 011 should be 1"
    
    inputs = {
        "sel": True,
        "a": False,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 100 should be 0"
    
    inputs = {
        "sel": True,
        "a": False,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 101 should be 1"
    
    inputs = {
        "sel": True,
        "a": True,
        "b": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Input 110 should be 0"
    
    inputs = {
        "sel": True,
        "a": True,
        "b": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Input 111 should be 1"
    
def test_DMux():
    print("Testing DMux")
    testChip = builtInChips.DMux()
    
    inputs = {
        "sel": False,
        "in": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "Input 00 should make a=0"
    assert testChip.outputs["b"] == False, "Input 00 should make b=0"
    
    inputs = {
        "sel": False,
        "in": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == True, "Input 01 should make a=1"
    assert testChip.outputs["b"] == False, "Input 01 should make b=0"
    
    inputs = {
        "sel": True,
        "in": False
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "Input 10 should make a=0"
    assert testChip.outputs["b"] == False, "Input 10 should make b=0"
    
    inputs = {
        "sel": True,
        "in": True
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "Input 11 should make a=0"
    assert testChip.outputs["b"] == True, "Input 11 should make b=1"
    
def test_Not16():
    print("Testing Not16")
    testChip = builtInChips.Not16()
    
    inputs = {
        "in": 0x0000
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0xffff, "Output should be 0x1111"
    assert testChip.outputs["out"] == 0b1111111111111111, "Output should translate to binary"
    
    inputs = {
        "in": 0x00ff
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0xff00, "Output should be 0xff00"
    assert testChip.outputs["out"] == 0b1111111100000000, "Output should translate to binary"
    
    inputs = {
        "in": 0x80ff
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x7f00, "Output should be 0xff00"
    assert testChip.outputs["out"] == 0b0111111100000000, "Output should translate to binary"

def test_Or16():
    print("Testing Or16")
    testChip = builtInChips.Or16()
    
    inputs = {
        "a": 0x0000,
        "b": 0x0000
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x0000, "Output should be 0x0000"
    assert testChip.outputs["out"] == 0b0000000000000000, "Output should translate to binary"
    
    inputs = {
        "a": 0x00ff,
        "b": 0x0000
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x00ff, "Output should be 0x00ff"
    assert testChip.outputs["out"] == 0b0000000011111111, "Output should translate to binary"
    
    inputs = {
        "a": 0x00fe,
        "b": 0x00fe
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x00fe, "Output should be 0x00fe"
    assert testChip.outputs["out"] == 0b0000000011111110, "Output should translate to binary"
    
    inputs = {
        "a": 0x80fe,
        "b": 0x00fe
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x80fe, "Output should be 0x00fe"
    assert testChip.outputs["out"] == 0b1000000011111110, "Output should translate to binary"

def test_And16():
    print("Testing And16")
    testChip = builtInChips.And16()
    
    inputs = {
        "a": 0x0000,
        "b": 0x0000
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x0000, "Output should be 0x0000"
    assert testChip.outputs["out"] == 0b0000000000000000, "Output should translate to binary"
    
    inputs = {
        "a": 0x00ff,
        "b": 0x0000
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x0000, "Output should be 0x00ff"
    assert testChip.outputs["out"] == 0b0000000000000000, "Output should translate to binary"
    
    inputs = {
        "a": 0x00fe,
        "b": 0x00fe
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x00fe, "Output should be 0x00fe"
    assert testChip.outputs["out"] == 0b0000000011111110, "Output should translate to binary"
    
    inputs = {
        "a": 0x1100,
        "b": 0xdd00
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x1100, "Output should be 0x00fe"
    assert testChip.outputs["out"] == 0b0001000100000000, "Output should translate to binary"
    
    inputs = {
        "a": 0x8800,
        "b": 0x9900
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x8800, "Output should be 0x00fe"
    assert testChip.outputs["out"] == 0b1000100000000000, "Output should translate to binary"

def test_Or8Way():
    print("Testing Or8Way")
    testChip = builtInChips.Or8Way()
    
    inputs = {
        "in": 0x00
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == False, "Output should be false"
    
    inputs = {
        "in": 0x10
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Output should be true"
    
    inputs = {
        "in": 0xdd
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == True, "Output should be true"

def test_Mux4Way16():
    print("Testing Mux4Way16")
    testChip = builtInChips.Mux4Way16()
    
    inputs = {
        "a": 0x0000,
        "b": 0x0000,
        "c": 0x0000,
        "d": 0x0000,
        "sel": 0b00,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x0000, "Output should be 0x0000"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "sel": 0b00,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x1234, "Output should be 0x1234"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "sel": 0b01,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x5678, "Output should be 0x5678"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "sel": 0b10,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0xabcd, "Output should be 0xabcd"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "sel": 0b11,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0xffcc, "Output should be 0x0000"
    
def test_Mux8Way16():
    print("Testing Mux8Way16")
    testChip = builtInChips.Mux8Way16()
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "e": 0xccff,
        "f": 0xdcba,
        "g": 0x8765,
        "h": 0x4321,
        "sel": 0b000,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x1234, "Output should be 0x1234"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "e": 0xccff,
        "f": 0xdcba,
        "g": 0x8765,
        "h": 0x4321,
        "sel": 0b001,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x5678, "Output should be 0x5678"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "e": 0xccff,
        "f": 0xdcba,
        "g": 0x8765,
        "h": 0x4321,
        "sel": 0b010,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0xabcd, "Output should be 0xabcd"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "e": 0xccff,
        "f": 0xdcba,
        "g": 0x8765,
        "h": 0x4321,
        "sel": 0b011,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0xffcc, "Output should be 0xffcc"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "e": 0xccff,
        "f": 0xdcba,
        "g": 0x8765,
        "h": 0x4321,
        "sel": 0b100,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0xccff, "Output should be 0xccff"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "e": 0xccff,
        "f": 0xdcba,
        "g": 0x8765,
        "h": 0x4321,
        "sel": 0b101,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0xdcba, "Output should be 0xdcba"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "e": 0xccff,
        "f": 0xdcba,
        "g": 0x8765,
        "h": 0x4321,
        "sel": 0b110,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x8765, "Output should be 0x8765"
    
    inputs = {
        "a": 0x1234,
        "b": 0x5678,
        "c": 0xabcd,
        "d": 0xffcc,
        "e": 0xccff,
        "f": 0xdcba,
        "g": 0x8765,
        "h": 0x4321,
        "sel": 0b111,
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0x4321, "Output should be 0x4321"

def test_DMux4Way():
    print("Testing DMux4Way")
    testChip = builtInChips.DMux4Way()
    
    inputs = {
        "in": False,
        "sel": 0b00
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    
    inputs = {
        "in": False,
        "sel": 0b01
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    
    inputs = {
        "in": False,
        "sel": 0b10
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    
    inputs = {
        "in": False,
        "sel": 0b11
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    
    inputs = {
        "in": True,
        "sel": 0b00
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == True, "a should be true"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    
    inputs = {
        "in": True,
        "sel": 0b01
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == True, "b should be true"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    
    inputs = {
        "in": True,
        "sel": 0b10
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == True, "c should be true"
    assert testChip.outputs["d"] == False, "d should be false"
    
    inputs = {
        "in": True,
        "sel": 0b11
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == True, "d should be true"

def test_DMux8Way():
    print("Testing DMux8Way")
    testChip = builtInChips.DMux8Way()
    
    inputs = {
        "in": False,
        "sel": 0b000
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    assert testChip.outputs["e"] == False, "e should be false"
    assert testChip.outputs["f"] == False, "f should be false"
    assert testChip.outputs["g"] == False, "g should be false"
    assert testChip.outputs["h"] == False, "h should be false"
    
    inputs = {
        "in": True,
        "sel": 0b000
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == True, "a should be true"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    assert testChip.outputs["e"] == False, "e should be false"
    assert testChip.outputs["f"] == False, "f should be false"
    assert testChip.outputs["g"] == False, "g should be false"
    assert testChip.outputs["h"] == False, "h should be false"
    
    inputs = {
        "in": True,
        "sel": 0b001
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == True, "b should be true"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    assert testChip.outputs["e"] == False, "e should be false"
    assert testChip.outputs["f"] == False, "f should be false"
    assert testChip.outputs["g"] == False, "g should be false"
    assert testChip.outputs["h"] == False, "h should be false"
    
    inputs = {
        "in": True,
        "sel": 0b010
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == True, "c should be true"
    assert testChip.outputs["d"] == False, "d should be false"
    assert testChip.outputs["e"] == False, "e should be false"
    assert testChip.outputs["f"] == False, "f should be false"
    assert testChip.outputs["g"] == False, "g should be false"
    assert testChip.outputs["h"] == False, "h should be false"
    
    inputs = {
        "in": True,
        "sel": 0b011
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == True, "d should be true"
    assert testChip.outputs["e"] == False, "e should be false"
    assert testChip.outputs["f"] == False, "f should be false"
    assert testChip.outputs["g"] == False, "g should be false"
    assert testChip.outputs["h"] == False, "h should be false"
    
    inputs = {
        "in": True,
        "sel": 0b100
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    assert testChip.outputs["e"] == True, "e should be true"
    assert testChip.outputs["f"] == False, "f should be false"
    assert testChip.outputs["g"] == False, "g should be false"
    assert testChip.outputs["h"] == False, "h should be false"
    
    inputs = {
        "in": True,
        "sel": 0b101
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    assert testChip.outputs["e"] == False, "e should be false"
    assert testChip.outputs["f"] == True, "f should be true"
    assert testChip.outputs["g"] == False, "g should be false"
    assert testChip.outputs["h"] == False, "h should be false"
    
    inputs = {
        "in": True,
        "sel": 0b110
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    assert testChip.outputs["e"] == False, "e should be false"
    assert testChip.outputs["f"] == False, "f should be false"
    assert testChip.outputs["g"] == True, "g should be true"
    assert testChip.outputs["h"] == False, "h should be false"
    
    inputs = {
        "in": True,
        "sel": 0b111
    }
    testChip.eval(inputs)
    assert testChip.outputs["a"] == False, "a should be false"
    assert testChip.outputs["b"] == False, "b should be false"
    assert testChip.outputs["c"] == False, "c should be false"
    assert testChip.outputs["d"] == False, "d should be false"
    assert testChip.outputs["e"] == False, "e should be false"
    assert testChip.outputs["f"] == False, "f should be false"
    assert testChip.outputs["g"] == False, "g should be false"
    assert testChip.outputs["h"] == True, "h should be true"

if __name__ == "__main__":
    test_Nand()
    test_Not()
    test_And()
    test_Or()
    test_Xor()
    test_Mux()
    test_DMux()
    test_Not16()
    test_And16()
    test_Or8Way()
    test_Or16()
    test_Mux4Way16()
    test_Mux8Way16()
    test_DMux4Way()
    test_DMux8Way()
    
    print("Everything passed")