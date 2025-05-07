### Hardware Simulator logic: implement a way for each builtInChip to receive inputs from others / pass outputs to others
### Then, process a .hdl file to implement these connections

### each "part" should contain a dictionary of pins mapped to wires
### a verification function could make sure each pin of a built-in chip is labeled

class Circuit():
    def __init__(self):
        self.inputs = {} # input pin names
        self.outputs = {} # output pin names
        self.internals = {} # internal wire names
        self.parts = {} # parts with dictionaries of pins mapped to wires
        
def tst_parser(filepath):
    with open(filepath, "r") as file:
        for line in file:
            if line.startswith("import"):
                print("importing something")
                
def hdl_parser(filepath):
    with open(filepath, "r") as file:
        for line in file:
            if line.startswith("import"):
                print("importing something")