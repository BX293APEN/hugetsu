from hugetsu import (
    Metre,
    Ri,
    KiloGram
)

if __name__ == "__main__":
    m = Metre(10)
    r = Ri(20)
    k = KiloGram()
    print(m)
    print(r)
    print(r.si())
    print(m + r)
    print(r + m)
    print(k)
    k.value(20)
    print(k)
    print(m + k)
