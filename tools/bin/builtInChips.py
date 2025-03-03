## Define the boolean bus, where the first digit in binary is index 0 of the value array
class boolBus:
    def __init__(self, val = None):
        self.val = val
        
    def toString(val):
        outString = ""
        for element in val:
            if element:
                outString = "1" + outString
            else:
                outString = "0" + outString
        return outString
    
    def stringToBus(val):
        outBus = []
        for element in val:
            if element == "1":
                outBus.insert(0, True)
            elif element == "0":
                outBus.insert(0, False)
        return outBus
        

class builtInChip:
    def __init__(self):
        self.inputLabels = []
        self.outputLabels = []
    
class NAND(builtInChip):
    def __init__(self):
        self.inputLabels = ["a", "b"]
        self.outputLabels = ["out"]
        
    def eval(self, a, b):
        return not (a & b)

class NOT(builtInChip):
    def __init__(self):
        self.inputLabels = ["in"]
        self.outputLabels = ["out"]
    
    def eval(self, input):
        return not input

class AND(builtInChip):
    def __init__(self):
        self.inputLabels = ["a", "b"]
        self.outputLabels = ["out"]
        
    def eval(self, a, b):
        return a & b

class OR(builtInChip):
    def __init__(self):
        self.inputLabels = ["a", "b"]
        self.outputLabels = ["out"]
        
    def eval(self, a, b):
        return a | b
    
class XOR(builtInChip):
    def __init__(self):
        self.inputLabels = ["a", "b"]
        self.outputLabels = ["out"]
    
    def eval(self, a, b):
        return a ^ b
    
class MUX(builtInChip):
    def __init__(self):
        self.inputLabels = ["sel", "a", "b"]
        self.outputLabels = ["out"]
    
    def eval(self, sel, a, b):
        if sel:
            return b
        
        return a
    
class DMUX(builtInChip):
    def __init__(self):
        self.inputLabels = ["sel", "in"]
        self.outputLabels = ["a", "b"]
    
    def eval(self, sel, input):
        if sel:
            return [False, input]
        
        return [input, False]
    
class NOT16(builtInChip):
    def __init__(self):
        self.inputLabels = ["in[16]"]
        self.outputLabels = ["out[16]"]
    
    def eval(self, in16):
        outArr = []
        for val in in16:
            outArr.append(not val)
        return outArr