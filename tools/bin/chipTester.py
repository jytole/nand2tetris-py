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
    
def test_DMux():
    print("Testing DMux")
    
def test_Not16():
    print("Testing Not16")
    testChip = builtInChips.Not16()
    
    inputs = {
        "in": 0x0000
    }
    testChip.eval(inputs)
    assert testChip.outputs["out"] == 0xffff, "Output should be 0x1111"
    assert testChip.outputs["out"] == 0b1111111111111111, "Output should be binary"

## etc.

if __name__ == "__main__":
    test_Nand()
    test_Not()
    test_And()
    test_Or()
    test_Xor()
    test_Mux()
    test_DMux()
    test_Not16()
    print("Everything passed")