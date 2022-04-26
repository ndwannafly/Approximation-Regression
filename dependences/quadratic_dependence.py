import numpy as np
from dependences.dependence import Dependence


class QuadraticDependence(Dependence):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sum_x = sum(self.x)
        self.siz = len(x)
        self.sum_xx = sum([x*x for x in self.x])
        self.sum_y = sum(self.y)
        self.sum_xxx = sum([x*x*x for x in self.x])
        self.sum_xxxx = sum([x*x*x*x for x in self.x])
        self.sum_xy = 0
        self.sum_xxy = 0
        for i in range(self.siz):
            self.sum_xy += x[i] * y[i]
            self.sum_xxy += x[i] * x[i] * y[i]
        
        self.delta = np.linalg.det(np.array(
                        [[self.siz, self.sum_x, self.sum_xx], 
                        [self.sum_x, self.sum_xx, self.sum_xxx],
                        [self.sum_xx, self.sum_xxx, self.sum_xxxx]]
        ))
        
        self.delta_1 = np.linalg.det(np.array(
                        [[self.sum_y, self.sum_x, self.sum_xx], 
                        [self.sum_xy, self.sum_xx, self.sum_xxx],
                        [self.sum_xxy, self.sum_xxx, self.sum_xxxx]]
        ))


        self.delta_2 = np.linalg.det(np.array(
                        [[self.siz, self.sum_y, self.sum_xx], 
                        [self.sum_x, self.sum_xy, self.sum_xxx],
                        [self.sum_xx, self.sum_xxy, self.sum_xxxx]]
        ))

        self.delta_3 = np.linalg.det(np.array(
                        [[self.siz, self.sum_x, self.sum_y], 
                        [self.sum_x, self.sum_xx, self.sum_xy],
                        [self.sum_xx, self.sum_xxx, self.sum_xxy]]
        ))
        
        self.c = self.delta_1 / self.delta
        self.b = self.delta_2 / self.delta
        self.a = self.delta_3 / self.delta
    def f(self, x):
        return self.a * x * x + self.b * x + self.c

    def to_str(self):
        return 'Quadratic Dependence'
    
    def exp(self):
        return '{}x^2 + {}x + {}'.format(self.a, self.b, self.c)