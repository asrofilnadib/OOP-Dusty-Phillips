class BaseClass:
    num_base_class = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_class += 1


class LeftSubClass(BaseClass):
    num_left_subclass = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_subclass += 1


class RightSubClass(BaseClass):
    num_right_subclass = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_subclass += 1


class Subclass(LeftSubClass, RightSubClass):
    num_subclass = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_subclass += 1