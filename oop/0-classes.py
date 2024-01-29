"""class declaration"""
class person:
    __gender = "DVD"
    """attributes"""
    """access: privet, public, proticted"""
    """class attributes, instance attributes"""
    @property
    def gender(self):
        if self.__gender == "male" or self.__gender == "female":
            return self.__gender
        return "male"

    @gender.setter
    def gender(self, new):
        if new == "male" or new == "female":
            self.__gender = new


obj1 = person()
obj2 = person()
obj3 = person()
obj4 = person()
obj5 = person()

obj2.gender = "email"

print(obj1.gender)
print(obj2.gender)
print(obj3.gender)
print(obj4.gender)
print(obj5.gender)
