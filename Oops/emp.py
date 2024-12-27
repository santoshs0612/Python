
class Employee:

    name = "Santosh"
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __str__(self):
        return f"The Name of Empolyee : {self.name}"
    
    def __repr__(self): # object recreation
        return f"The Name of Empolyee : {self.name}"
    def __call__(self):
        print("Hey i am good")