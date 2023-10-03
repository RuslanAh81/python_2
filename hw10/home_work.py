from task5 import Dog, Fish, Bird

class Factory:
    anim_type_list = ['dog', 'fish', 'bird']

    def __init__(self, type_animal, name: str, age: int, spec: str):
        self.type_animal = self.check_errors(type_animal)
        self.params = (name, age, spec)

    def return_anim(self):
        match self.type_animal:
            case 'dog':
                return Dog(*self.params)
            case 'cat':
                return Fish(*self.params)
            case 'bird':
                return Bird(*self.params)

    def check_errors(self, type_animal):
        if type_animal in self.anim_type_list:
            return type_animal
        else:
            raise ValueError


if __name__ == '__main__':
    anim_1 = Factory('dog', 'Bobik', 3, 'Gives a voice').return_anim()
    anim_2 = Factory('bird', 'Popka', 8, 'Летаю, но не высоко').return_anim()

    print(f'{anim_1.name} {anim_1.get_spec()}')
    print(f'{anim_2.name} {anim_2.get_spec()}')