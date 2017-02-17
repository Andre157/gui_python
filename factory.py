import abc
import random


class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_object(self):
        return get_factory()

class ConcreteFactory1(AbstractFactory):
    def make_object(self):
        return SomeObject1()


class ConcreteFactory2(AbstractFactory):
    def make_object(self):
        return SomeObject2()

def SomeObject1():
    pass

def SomeObject2():
    pass

def get_factory():
    a=random.randint(1 , 2)
    if(a==2):
        print("HHHH")
        return ConcreteFactory1()
    else:
        print("YYYY")
        return ConcreteFactory2()

if __name__ == "__main__":
    t = get_factory()
    t.make_object()