class Cs:
    @staticmethod
    def static_method():
        print("Static_method")
    @classmethod
    def class_method(cls):
        print("Class_method")
    def instance_method(self):
        print("Instance_method")

i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()
