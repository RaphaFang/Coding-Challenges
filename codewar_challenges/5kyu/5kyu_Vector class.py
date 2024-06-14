class Vector:
    def __init__(self, ll):
        self.ll = ll

    def add(self,other_vector):
        if len(self.ll)==len(other_vector.ll):
            result = [a + b for a, b in zip(self.ll, other_vector.ll)]
            return Vector(result)
        else:
            raise ValueError
        
    def subtract(self, other_vector):
        if len(self.ll)==len(other_vector.ll):
            result = [a - b for a, b in zip(self.ll, other_vector.ll)]
            return Vector(result)
        else:
            raise ValueError

    def dot(self, other_vector):
        if len(self.ll)==len(other_vector.ll):
            return sum(a * b for a, b in zip(self.ll, other_vector.ll))
        else:
            raise ValueError

    def norm(self):
        result = sum(a**2 for a in self.ll)
        print(result**0.5)
        return result**0.5
    
    def __str__(self):
        return f"({','.join(map(str, self.ll))})"

    def equals(self, other_vector):
        return self.ll == other_vector.ll


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.__str__()