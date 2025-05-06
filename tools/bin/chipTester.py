## Test dev file to test expected functionality of chips, as they are developed

import builtInChips

def test_Nand():
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
    assert True == True, "How did this fail"

## etc.

if __name__ == "__main__":
    test_Nand()
    test_Not()
    print("Everything passed")