import math
from pickle import TRUE
from matplotlib import pyplot as plt
import numpy as np
from dependences.linear_dependence import LinearDependence
from dependences.quadratic_dependence import QuadraticDependence
from function import Function


class Invoker:
    DASH = '-' * 20

    def __init__(self):
        pass

    def invoke(self):
        print('> Welcome to integral world!')
        while TRUE:
            functions = [
                Function('y = sin(x)', lambda x: np.sin(x)),
                Function('y = sin(x) + cos(x)', lambda x: 3 * np.power(x, 3) - 2 * np.power(x, 2) + 2),
                Function('y = 3x^3 - 2x^2 + 2', lambda x: 3 * np.power(x, 3) - 2 * np.power(x, 2) + 2),
                Function('y = 3x / (x^4 + 3)', lambda x: (3*x) / (np.power(x, 4) + 3))
            ]

            print('> {} Welcome to approximation world {}\n'.format(self.DASH, self.DASH))
            print('> Please choose your function:\n')
            for i, func in enumerate(functions):
                print('> {}. {}'.format(i, func.to_str()))
            
            print('> Enter your option: ', end='')
            opt_func = int(input())

            chosen_func = functions[opt_func]

            print(self.DASH * 3 + '\n')
            
            print('> Enter x(s): ')
            x = list(map(float, input().split()))

            y = [chosen_func.f(xi) for xi in x]

            dependences = [
                LinearDependence(x, y),
                QuadraticDependence(x, y)
            ]
            print(self.DASH * 3 + '\n')
            print('> Please choose the dependence: ')
            for i, d in enumerate(dependences):
                print('> {}. {}'.format(i, d.to_str()))
            print('> Enter the type of dependence: ', end='')
            opt_depend = int(input())

            chosen_depend = dependences[opt_depend]
            
            y_approx = [chosen_depend.f(xi) for xi in x]

            #remove noise
            idx_max = 0
            dis_max = -math.inf
            for i in range(len(y)):
                if abs(y[i] - y_approx[i]) > dis_max:
                    dis_max = abs(y[i] - y_approx[i])
                    idx_max = i
            x.pop(idx_max)
            y.pop(idx_max)
            y_approx.pop(idx_max)
            #draw
            self.draw(x, y, y_approx, chosen_func, chosen_depend)

            print('> Do you want to continue? (Y/N) ', end='')
            opt_continue = input()
            if opt_continue == 'Y':
                continue
            else:
                break

        
    def draw(self, x, y, y_linear, func, approx_func):
        _, axs = plt.subplots(3)
        for i in range(3):
            axs[i].grid(True)

        x1 = np.arange(min(x) - 1, max(x) + 1, 0.1)
        y1 = [func.f(xi) for xi in x1]
        y1_linear = [approx_func.f(xi) for xi in x1]

        axs[0].plot(x1, y1, label = func.to_str(), c ='green')
        axs[0].scatter(x, y, marker = '.', color ='r', s = 100)
        axs[0].legend(loc = 'center')
        
        axs[1].plot(x1, y1_linear, label =approx_func.exp(), c = 'blue')
        axs[1].scatter(x, y_linear, marker ='.', color ='r', s= 100)
        axs[1].legend(loc = 'center')

        axs[2].plot(x1, y1, label = func.to_str(), c = 'green')
        axs[2].plot(x1, y1_linear, label =approx_func.exp(), c ='blue')
        axs[2].scatter(x, y, marker = '.', color ='r', s = 100)
        axs[2].legend()

        plt.show()