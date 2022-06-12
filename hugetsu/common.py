class Unit:
    """単位型クラス

    Parameters::

        name : str
            単位名
        ratio : float
            SI単位系に対する比率
        type :int
            単位の種類
            1: 長さ
            2: 質量
    """
    name: str
    ratio: float
    type: 1 | 2

def __ScalarCalc(func)->"Length"|"Weight":
    def switch(*args, **kwargs):
        result:__Scalar = func(*args, **kwargs)
        if isinstance(result,Length):
            return Length(result)
        elif isinstance(result,Weight):
            return Weight(result)
    return switch
class __Scalar(float):
    def __new__(self, ___x:int|float, unit: Unit) -> "__Scalar":
        self.___x = float(___x)
        self.unit = unit
        return float.__new__(self, ___x)
    
    def __init__(self, ___x: int | float, unit: Unit) -> "__Scalar":
        self.___x = float(___x)
        self.unit = unit
        super().__init__()

    @__ScalarCalc
    def __add__(
        self, __x: float) -> "__Scalar": return __Scalar(super().__add__(__x), self.unit)
    
    @__ScalarCalc
    def __sub__(
        self, __x: float) -> "__Scalar": return __Scalar(super().__sub__(__x), self.unit)
    @__ScalarCalc
    def __mul__(
        self, __x: float) -> "__Scalar": return __Scalar(super().__mul__(__x), self.unit)
    @__ScalarCalc
    def __truediv__(
        self, __x: float) -> "__Scalar": return __Scalar(super().__truediv__(__x), self.unit)
    @__ScalarCalc
    def __floordiv__(
        self, __x: float) -> "__Scalar": return __Scalar(super().__floordiv__(__x), self.unit)
    @__ScalarCalc
    def __eq__(self, __x: "__Scalar") -> bool:
        if type(__x) != __Scalar:
            return False
        return (self.___x/self.unit.ratio) == __x/__x.unit.ratio
    @__ScalarCalc
    def __lt__(self, __x: "__Scalar") -> bool:
        return (self.___x/self.unit.ratio) < __x.___x/__x.unit.ratio
    @__ScalarCalc
    def __gt__(self, __x: "__Scalar") -> bool:
        return (self.___x/self.unit.ratio) > __x.___x/__x.unit.ratio

    def format(self):
        return f"{self.___x} {self.unit.name}"

    def convert(self, unit: Unit) -> "__Scalar":
        if self.unit.type != unit.type:
            raise NotImplementedError("Unsupported unit type")
        return __Scalar((self.___x/self.unit.ratio)*unit.ratio, unit)

class Length(__Scalar):
    def __init__(self, ___x: int | float, unit: Unit) -> "Length":
        super().__init__(___x,unit)
class Weight(__Scalar):
    def __init__(self, ___x: int | float, unit: Unit) -> "Weight":
        super().__init__(___x,unit)
