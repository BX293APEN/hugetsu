from abc import ABCMeta, abstractmethod
from typing import NewType

class Scalar(float):
    def __new__(cls,val):
        self=super().__new__(cls,val)
        self.___val=val
        return self.___val

class Length:
    def __init__(self,val:Scalar):
        return super().__init__(val)

a = Length(20)