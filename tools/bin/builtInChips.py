## Define the boolean bus, where the first digit in binary is index 0 of the value array

## !! MSB is index 0 !!

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
        self.pinSizes = {
            "a": 1,
            "b": 1,
            "out": 1
        }
    
    def typeCheck(self):
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        self.outputs["out"] = not (self.inputs["a"] & self.inputs["b"])

### Project 1 Chips

class Not(builtInChip):
    def __init__(self):
        self.inputs = {"in": None}
        self.outputs = {"out": None}
        self.pinSizes = {
            "in": 1,
            "out": 1
        }
        
    def typeCheck(self):
        assert type(self.inputs["in"]) == type(False), "Input in is not a boolean"
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        self.outputs["out"] = not self.inputs["in"]

class And(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None
        }
        self.outputs = {"out": None}
        self.pinSizes = {
            "a": 1,
            "b": 1,
            "out": 1
        }
        
    def typeCheck(self):
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        self.outputs["out"] = self.inputs["a"] & self.inputs["b"]

class Or(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None
        }
        self.outputs = {"out": None}
        self.pinSizes = {
            "a": 1,
            "b": 1,
            "out": 1
        }
        
    def typeCheck(self):
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
        
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        self.outputs["out"] = self.inputs["a"] | self.inputs["b"]
    
class Xor(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None
        }
        self.outputs = {"out": None}
        self.pinSizes = {
            "a": 1,
            "b": 1,
            "out": 1
        }
    
    def typeCheck(self):
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        self.outputs["out"] = self.inputs["a"] ^ self.inputs["b"]
    
class Mux(builtInChip):
    def __init__(self):
        self.inputs = {
            "sel": None,
            "a": None,
            "b": None
        }
        self.outputs = {"out": None}
        self.pinSizes = {
            "sel": 1,
            "a": 1,
            "b": 1,
            "out": 1
        }
    
    def typeCheck(self):
        assert type(self.inputs["sel"]) == type(False), "Input sel is not a boolean"
        assert type(self.inputs["a"]) == type(False), "Input a is not a boolean"
        assert type(self.inputs["b"]) == type(False), "Input b is not a boolean"
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
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
        self.pinSizes = {
            "sel": 1,
            "in": 1,
            "a": 1,
            "b": 1
        }
        
    def typeCheck(self):
        assert type(self.inputs["sel"]) == type(False), "Input sel is not a boolean"
        assert type(self.inputs["in"]) == type(False), "Input in is not a boolean"
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        if self.inputs["sel"]:
            self.outputs["a"] = False
            self.outputs["b"] = self.inputs["in"]
        else:
            self.outputs["a"] = self.inputs["in"]
            self.outputs["b"] = False
    
class Not16(builtInChip):
    ## Assumes binary stored as binary string e.g. 0b0000
    def __init__(self):
        ## NOTE that in and out should be 16-bit busses
        self.inputs = {"in": None}
        self.outputs = {"out": None}
        self.pinSizes = {
            "in": 16,
            "out": 16
        }
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        self.outputs["out"] = 0b1111111111111111 - self.inputs["in"]
        
class And16(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None
        }
        self.outputs = {"out": None}
        self.pinSizes = {
            "a": 16,
            "b": 16,
            "out": 16
        }
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        self.outputs["out"] = self.inputs["a"] & self.inputs["b"]
        
class Or8Way(builtInChip):
    def __init__(self):
        self.inputs = {
            "in": None
        }
        self.outputs = {
            "out": None
        }
        self.pinSizes = {
            "in": 8,
            "out": 1
        }
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        # format "in" as an 8 bit binary string
        input = format(self.inputs["in"], '08b')
        self.outputs["out"] = ((input[0] == '1') | 
                               (input[1] == '1') | 
                               (input[2] == '1') | 
                               (input[3] == '1') | 
                               (input[4] == '1') | 
                               (input[5] == '1') | 
                               (input[6] == '1') | 
                               (input[7] == '1'))
        
class Or16(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None
        }
        self.outputs = {
            "out": None
        }
        self.pinSizes = {
            "a": 16,
            "b": 16,
            "out": 16
        }
        
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        self.outputs["out"] = self.inputs["a"] | self.inputs["b"]

## TODO continue implementing built-in chip eval functions
class Mux4Way16(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None,
            "c": None,
            "d": None,
            "sel": None
        }
        self.outputs = {
            "out": None
        }
        self.pinSizes = {
            "a": 16,
            "b": 16,
            "c": 16,
            "d": 16,
            "sel": 2,
            "out": 16
        }
    
    # !! MSB is index 0 !! #
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        sel = format(self.inputs["sel"], '02b')
        if sel[0] == '1':
            if sel[1] == '1':
                ##11
                self.outputs["out"] = self.inputs["d"]
            else:
                #10
                self.outputs["out"] = self.inputs["c"]
        else:
            if sel[1] == '1':
                ##01
                self.outputs["out"] = self.inputs["b"]
            else:
                ##00
                self.outputs["out"] = self.inputs["a"]

class Mux8Way16(builtInChip):
    def __init__(self):
        self.inputs = {
            "a": None,
            "b": None,
            "c": None,
            "d": None,
            "e": None,
            "f": None,
            "g": None,
            "h": None,
            "sel": None
        }
        self.outputs = {
            "out": None
        }
        self.pinSizes = {
            "a": 16,
            "b": 16,
            "c": 16,
            "d": 16,
            "e": 16,
            "f": 16,
            "g": 16,
            "h": 16,
            "sel": 3,
            "out": 16
        }
    
    # !! LSB is index 0 !! #
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        sel = format(self.inputs["sel"], '03b')
        if sel[0] == '1':
            if sel[1] == '1':
                if sel[2] == '1':
                    ##111
                    self.outputs["out"] = self.inputs["h"]
                else:
                    #110
                    self.outputs["out"] = self.inputs["g"]
            else:
                if sel[2] == '1':
                    ##101
                    self.outputs["out"] = self.inputs["f"]
                else:
                    ##100
                    self.outputs["out"] = self.inputs["e"]
        else:
            if sel[1] == '1':
                if sel[2] == '1':
                    ##011
                    self.outputs["out"] = self.inputs["d"]
                else:
                    #010
                    self.outputs["out"] = self.inputs["c"]
            else:
                if sel[2] == '1':
                    ##001
                    self.outputs["out"] = self.inputs["b"]
                else:
                    ##000
                    self.outputs["out"] = self.inputs["a"]

class DMux4Way(builtInChip):
    def __init__(self):
        self.inputs = {
            "in": None,
            "sel": None
        }
        self.outputs = {
            "a": None,
            "b": None,
            "c": None,
            "d": None
        }
        self.pinSizes = {
            "in": 1,
            "sel": 2,
            "a": 1,
            "b": 1,
            "c": 1,
            "d": 1
        }
    
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        sel = format(self.inputs["sel"], '02b')
        self.outputs["a"] = False
        self.outputs["b"] = False
        self.outputs["c"] = False
        self.outputs["d"] = False
        if sel[0] == '1':
            if sel[1] == '1':
                ##11
                self.outputs["d"] = self.inputs["in"]
            else:
                #10
                self.outputs["c"] = self.inputs["in"]
        else:
            if sel[1] == '1':
                ##01
                self.outputs["b"] = self.inputs["in"]
            else:
                ##00
                self.outputs["a"] = self.inputs["in"]

class DMux8Way(builtInChip):
    def __init__(self):
        self.inputs = {
            "in": None,
            "sel": None
        }
        self.outputs = {
            "a": None,
            "b": None,
            "c": None,
            "d": None,
            "e": None,
            "f": None,
            "g": None,
            "h": None
        }
        self.pinSizes = {
            "in": 1,
            "sel": 3,
            "a": 1,
            "b": 1,
            "c": 1,
            "d": 1,
            "e": 1,
            "f": 1,
            "g": 1,
            "h": 1
        }
        
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
        sel = format(self.inputs["sel"], '03b')
        self.outputs["a"] = False
        self.outputs["b"] = False
        self.outputs["c"] = False
        self.outputs["d"] = False
        self.outputs["e"] = False
        self.outputs["f"] = False
        self.outputs["g"] = False
        self.outputs["h"] = False
        if sel[0] == '1':
            if sel[1] == '1':
                if sel[2] == '1':
                    ##111
                    self.outputs["h"] = self.inputs["in"]
                else:
                    #110
                    self.outputs["g"] = self.inputs["in"]
            else:
                if sel[2] == '1':
                    ##101
                    self.outputs["f"] = self.inputs["in"]
                else:
                    ##100
                    self.outputs["e"] = self.inputs["in"]
        else:
            if sel[1] == '1':
                if sel[2] == '1':
                    ##011
                    self.outputs["d"] = self.inputs["in"]
                else:
                    #010
                    self.outputs["c"] = self.inputs["in"]
            else:
                if sel[2] == '1':
                    ##001
                    self.outputs["b"] = self.inputs["in"]
                else:
                    ##000
                    self.outputs["a"] = self.inputs["in"]

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
    def eval(self, inputs=None):
        if inputs is not None:
            self.updateInputs(inputs)
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