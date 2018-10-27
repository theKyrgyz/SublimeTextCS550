# RationalDemoEggers.py

# Lucas Eggers, October 27, 2018
# Quick description: Fleshed-out the starter demo package Ms. Healey provided in class for operations on rational expressions.

''' inspired by: 
    http://anandology.com/python-practice-book/object_oriented_programming.html
    
    other resources:
    https://docs.python.org/3/reference/datamodel.html
    https://docs.python.org/3/library/operator.html
'''

class RationalNumber:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def simplify(self, n, d):
        for i in range(100,1,-1):
            if (n%i == 0) and (d%i == 0):
                n = int(n/i)
                d = int(d/i)
        return RationalNumber(n,d)
    # I defined simplify() before the basic operations not only because of the way Python reads function calling,
    # but also because of the fact that division is still sanitary and unchanged at this stage in the code, making
    # simplification much easier to actually do.

    def __add__(self, other):
        n = self.n*other.d + self.d*other.n
        d = self.d*other.d
        return self.simplify(n,d)

    def __sub__(self, other):
        n = self.n*other.d - self.d*other.n
        d = self.d*other.d
        return self.simplify(n,d)

    def __mul__(self, other):
        n = self.n*other.n
        d = self.d*other.d
        return self.simplify(n,d)

    def __truediv__(self, other):
        n = self.n*other.d
        d = self.d*other.n
        return self.simplify(n,d)

    # complete this first!
    def __str__(self):
        return str(self.n)+"/"+str(self.d) # fill in code (replace 1)

    __repr__ = __str__ # what does this do?
    # unsure. I THINK it determines whether the quotes in, for example, "/", get printed along with the intended text.

def main():
    a = RationalNumber(1, 2)
    b = RationalNumber(1, 3)
    print(a) # 1/2
    print(b) # 1/3
    print(a+b) # 5/6
    print(a-b) # 1/6
    print(a*b) # 1/6
    print(a/b) # 3/2
    # Additional tests for simplification's sake.
    c = RationalNumber(1, 2)
    print(a+c)

main()