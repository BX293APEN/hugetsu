from hugetsu import (
    Metre,
    Ri,
    KiloGram
)

if __name__ == "__main__":
    m = Metre(10)
    r = Ri(20)
    k = KiloGram(30)
    print(m)
    print(r)
    print(r.si())
    print(m + r)
    print(r + m)
    print(k)
    print(m + k)