class Rhombus:
    # This approach I like more :)
   # def __init__(self, side_a, corner_a):
        # if side_a > 0:
            # print(f'Creating geometric figure')
        # else:
            # print(f'Invalid value')
        # self.side_a = side_a
        # self.corner_a = corner_a
        # self.corner_b = 180 - self.corner_a
        # or
        # self.__setattr__('side_a', side_a)
        # self.__setattr__('corner_a', corner_a)
        # self.__setattr__('corner_b', 180 - corner_a)

    def __setattr__(self, name, value):
        print(f'Setting {name} to {value}')
        if name == 'side_a' and value > 0:
            print(f'Side_a is {value}')
        elif name == 'corner_a':
            print(f'Corner_a value is {value}')
            self.corner_b = 180 - value
        elif name == 'corner_b':
            print(f'Corner_b value is {value}')
        else:
            pass

my_rhombus = Rhombus()
my_rhombus.side_a = 5
my_rhombus.corner_a = 75