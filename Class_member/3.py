class Cs:
    count = 0
# class inside + method outside variable = class variable
    def __init__(self):
        # method inside connection with class variable
        Cs.count = Cs.count +1
    @classmethod
    def getCount(cls):
        # cls = this method-class var
        return Cs.count
        # == cls.count

i1 = Cs()
i2 = Cs()
i3 = Cs()
print(Cs.getCount())
