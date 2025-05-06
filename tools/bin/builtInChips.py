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
        
## TODO implement input bus size logic, possibly in a run-time check of user file syntax
### NOTE bus checking should be implemented in typeCheck() functions as further asserts

class builtInChip:
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
    
    def updateInputs(self, dict):
        for key, value in dict.items():
            if key in self.inputs:
                self.inputs[key] = value
            else:
                print("Warning: Input field " + key + " not found")

### THE chip

class Nand(builtInChip):
    def __init__(self, a=None, b=None):
        self.inputs = {
            "a": a, 
            "b": b
        }
        self.outputs = {"out": None}
    
    def typeCheck(self):
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
    
    def eval(self):
        self.outputs["out"] = not (self.inputs["a"] & self.inputs["b"])

### Project 1 Chips

class Not(builtInChip):
    def __init__(self):
        self.inputs = {"in": None}
        self.outputs = {"out": None}
        
    def typeCheck(self):
        assert type(self.inputs["in"]) == type(False), "Input in is not a boolean"
    
    def eval(self):
        self.outputs["out"] = not self.inputs["in"]

class And(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None
        }
        self.outputs = {"out": None}
        
    def typeCheck(self):
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
    
    def eval(self):
        self.outputs["out"] = self.inputs["a"] & self.inputs["b"]

class Or(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None
        }
        self.outputs = {"out": None}
        
    def typeCheck(self):
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
        
    def eval(self):
        self.outputs["out"] = self.inputs["a"] | self.inputs["b"]
    
class Xor(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None
        }
        self.outputs = {"out": None}
    
    def typeCheck(self):
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
    
    def eval(self):
        self.outputs["out"] = self.inputs["a"] ^ self.inputs["b"]
    
class Mux(builtInChip):
    def __init__(self):
        self.inputs = {
            "sel": None,
            "a": None,
            "b": None
        }
        self.outputs = {"out": None}
    
    def typeCheck(self):
        assert type(self.inputs["sel"]) == type(False), "Input sel is not a boolean"
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
    
    def eval(self):
        if self.inputs["sel"]:
            self.outputs["out"] = self.inputs["b"]
        else:
            self.outputs["out"] = self.inputs["a"]
    
class DMux(builtInChip):
    def __init__(self):
        self.inputs = {
            "sel": None,
            "in": None
        }
        self.outputs = {
            "a": None,
            "b": None
        }
        
    def typeCheck(self):
        assert type(self.inputs["sel"]) == type(False), "Input sel is not a boolean"
        assert type(self.inputs["in"]) == type(False), "Input in is not a boolean"
    
    def eval(self):
        if self.inputs["sel"]:
            self.outputs["a"] = False
            self.outputs["b"] = self.inputs["input"]
        else:
            self.outputs["a"] = self.inputs["input"]
            self.outputs["b"] = False
    
class Not16(builtInChip):
    def __init__(self):
        ## NOTE that in and out should be 16-bit busses
        self.inputs = {"in": None}
        self.outputs = {"out": None}
    
    def eval(self, in16):
        outArr = []
        for val in self.inputs["in"]:
            outArr.append(not val)
        self.outputs["out"] = outArr
        
## TODO continue implementing built-in chip eval functions
class And16(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        
class Or8Way(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        
class Or16(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class Mux4Way16(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class Mux8Way16(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class DMux4Way(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class DMux8Way(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

### Project 2 Chips

class HalfAdder(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class FullAdder(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class Add16(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class Inc16(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        
class ALU(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        
### Project 3 Prereq

class DFF(builtInChip):
    def __init__(self):
        self.inputs = {"in": None}
        self.outputs = {"out": None}
        self.prevOutput = None
    
    ## DFF assumes eval is run on every clock cycle
    def eval(self):
        self.outputs["out"] = self.inputs["in"]
        
### Project 3 Chips
        
class Bit(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        
class PC(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        
class Register(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        
## class RegisterWithGUI??

class RAM(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class RAM8(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        
class RAM64(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class RAM512(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class RAM4K(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class RAM16K(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        
class ROM32K(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}        

class ARegister(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class DRegister(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class Keyboard(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

class Screen(builtInChip):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}