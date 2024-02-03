class student:
    def __init__(self, age, name):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

s1 = student(14, "omar")
print(s1.__dict__)
"""get"""
print(s1.name)
"""setter"""
s1.name = "abbas"

print(s1.__dict__)
