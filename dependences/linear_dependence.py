from dependences.dependence import Dependence


class LinearDependence(Dependence):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sum_x = sum(self.x)
        self.siz = len(x)
        self.sum_xx = sum([x*x for x in self.x])
        self.sum_y = sum(self.y)
        self.sum_xy = 0
        for i in range(self.siz):
            self.sum_xy += x[i] * y[i]
        self.a = (self.siz * self.sum_xy - self.sum_x * self.sum_y ) / (self.siz * self.sum_xx - self.sum_x * self.sum_x)
        self.b = (self.sum_y - self.a * self.sum_x) / self.siz

    def f(self, x):
        return self.a * x + self.b

    def to_str(self):
        return 'Linear Dependence'

    def exp(self):
        return '{}x + {}'.format(self.a, self.b)