"""
There are two ways of doing Abstract Class:
old one:
=======
- Definying a regular class raising 'not implemented exception' on abstract methods

class MyAbstract:
    def my_func(self):
        raise NotImplementedError()

new one (prefered)
==================
- Using ABC module (Abstract Base Classes)
- [documentation for ABC on python3](https://docs.python.org/3/library/abc.html)
- PEP 3119 and PEP 3141
- Another good tutorial [here](https://dmerej.info/blog/post/interfaces-and-annotations-in-python3/)

"""
import unittest
import abc

class ITelevisionChannel(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_channel_description(self) -> str:
        pass

    @abc.abstractmethod
    def is_(self) -> str:
        pass

class ChannelTV3(ITelevisionChannel):

    def get_channel_description(self) -> str:
        return "Main public channel on Catalonia"


class TestInterfaces(unittest.TestCase):
    def test_implementation_class(self):
        channel = ChannelTV3()
        self.assertGreater(len(channel.get_channel_description()), 0, "must return something" )

if __name__ == '__main__':
    unittest.main()