import unittest

class ParentClass:
    INITIAL_VALUE_A = 1

    def __init__(self):
        self.A_value=self.INITIAL_VALUE_A

    def this_function_call_set_value(self, value):
        self.set_value(value)

    def set_value(self,value):
        self.A_value = value

class ChildClass(ParentClass):
    INITIAL_VALUE_B=1
    def __init__(self):
        self.A_value=self.INITIAL_VALUE_B

    def set_value(self, value):
        self.B_value = value

class TestClassBehaviour(unittest.TestCase):
    """
    This test try to show the subtyping properties on Python language:
    -
    """
    TESTING_VALUE=123

    def call_set_value(self, obj: ParentClass, value):
        obj.set_value(value)

    def test_child_class(self):
        b = ChildClass()
        b.set_value(self.TESTING_VALUE)
        self.assertEqual(self.TESTING_VALUE, b.B_value, "set_value call B because obj is a instance of B class")
        self.assertEqual(ParentClass.INITIAL_VALUE_A, b.A_value, "A value remains unchanged")

    def test_function_on_parent_calls_to_override_methods(self):
        obj = ChildClass()
        obj.this_function_call_set_value(self.TESTING_VALUE)
        self.assertEqual(self.TESTING_VALUE, obj.B_value, "Child class have changed because override set_value function")
        self.assertEqual(ParentClass.INITIAL_VALUE_A, obj.A_value, "A value remains unchanged")

    def test_subtying_on_function_call(self):
        obj = ChildClass()
        self.call_set_value(obj,self.TESTING_VALUE)
        self.assertEqual(self.TESTING_VALUE, obj.B_value,
                         "Child class have changed because a function get a ParentClass object but a ChildClass is passed")
        self.assertEqual(ParentClass.INITIAL_VALUE_A, obj.A_value, "A value remains unchanged")

if __name__ == '__main__':
    unittest.main()