class Unit():
    name: str
    ratio: float
    type: str

    def __init__(self, content = 0):
        self.content = content / self.ratio
    
    def __str__(self):
        return f"{self.content * self.ratio} {self.name}"
    
    def si(self):
        return self.content
    
    def value(self):
        return f"{self.content * self.ratio} {self.name}"
    
    def type_check(self, other):
        return self.type == other.type

    def __add__(self, other):
        if self.type_check(other):
            return type(self)((self.content + other.content) * self.ratio)
        else:
            raise TypeError
    
    def __sub__(self, other):
        if self.type_check(other):
            return type(self)((self.content - other.content) * self.ratio)
    
    def __mul__(self, other):
        if self.type_check(other):
            return type(self)((self.content * other.content) * self.ratio)
    
    def __truediv__(self, other):
        if self.type_check(other):
            return type(self)((self.content / other.content) * self.ratio)
    
    def __floordiv__(self, other):
        if self.type_check(other):
            return type(self)((self.content // other.content) * self.ratio)
    
    def __eq__(self, other):
        if self.type_check(other):
            return self.content == other.content
    
    def __lt__(self, other):
        if self.type_check(other):
            return self.content < other.content
    
    def __gt__(self, other):
        if self.type_check(other):
            return self.content > other.content

    
    
class Length(Unit):
    name    = "m"
    ratio   = 1.0
    type    = "length"

    def __init__(self, content) -> "Length":
        super().__init__(content)

class Weight(Unit):
    name    = "kg"
    ratio   = 1.0
    type    = "weight"

    def __init__(self, content) -> "Weight":
        super().__init__(content)
