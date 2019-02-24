class ProgramerTwo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, name):
        return super(ProgramerTwo, self).__getattribute__(name)

    def __setattr__(self, name, value):
        # setattr(self, name, value)
        self.__dict__[name] = value

if __name__ == '__main__':
    p = ProgramerTwo('Albert', 25)
    print(p.name)
