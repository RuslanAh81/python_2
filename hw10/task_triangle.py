class Triangle:

    def __init__(self, side_a, side_b, side_c):
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c

    @property
    def _check_triangle(self):
        if(self.side_a + self.side_b) < self.side_c or(self.side_a + self.side_c) < self.side_b and\
                (self.side_b + self.side_c) < self.side_a:
            raise ValueError
        else:
            if self.side_a == self.side_b == self.side_c:
                return 'Треугольник равностороний'
            elif self.side_a == self.side_b != self.side_c or self.side_b == self.side_c != self.side_a or\
                    self.side_c == self.side_a != self.side_b:
                return 'Треугольник равнобедренный'
            else:
                return 'Просто треугольник'

    def get_result(self):
        return f'{self._check_triangle} со сторонами: {self.side_a}, {self.side_b}, {self.side_c}'


if __name__ == '__main__':
    fig_1 = Triangle(4, 4, 3)
    fig_2 = Triangle(4, 3, 2)
    fig_3 = Triangle(4, 4, 4)
    print(fig_1.get_result())
    print(fig_2.get_result())
    print(fig_3.get_result())