from msilib.schema import Error
from typing import Any

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


class Scalar(float):
    def __new__(self, ___x:int|float, unit: Unit) -> "Scalar":
        self.___x = float(___x)
        self.unit = unit
        return float.__new__(self, ___x)
    
    def __init__(self, ___x: int | float, unit: Unit) -> "Scalar":
        self.___x = float(___x)
        self.unit = unit
        super().__init__()

    def __add__(
        self, __x: float) -> "Scalar": return Scalar(super().__add__(__x), self.unit)

    def __sub__(
        self, __x: float) -> "Scalar": return Scalar(super().__sub__(__x), self.unit)

    def __mul__(
        self, __x: float) -> "Scalar": return Scalar(super().__mul__(__x), self.unit)

    def __truediv__(
        self, __x: float) -> "Scalar": return Scalar(super().__truediv__(__x), self.unit)

    def __floordiv__(
        self, __x: float) -> "Scalar": return Scalar(super().__floordiv__(__x), self.unit)
    
    def __eq__(self, __x: "Scalar") -> bool:
        if type(__x) != Scalar:
            return False
        return (self.___x/self.unit.ratio) == __x/__x.unit.ratio

    def __lt__(self, __x: "Scalar") -> bool:
        return (self.___x/self.unit.ratio) < __x.___x/__x.unit.ratio
    
    def __gt__(self, __x: "Scalar") -> bool:
        return (self.___x/self.unit.ratio) > __x.___x/__x.unit.ratio

    def format(self):
        return f"{self.___x} {self.unit.name}"

    def convert(self, unit: Unit) -> "Scalar":
        if self.unit.type != unit.type:
            raise NotImplementedError("Unsupported unit type")
        return Scalar((self.___x/self.unit.ratio)*unit.ratio, unit)