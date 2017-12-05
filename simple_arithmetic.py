from math import *
from sympy import symbols, diff, sin, cos, tan, asin, acos, atan, limit, log

x = symbols('x')
y = symbols('y')


class Arithmetic():
    def __init__(self, string):
        self.string = string
        self.symbol = {'mod': '%', 'div': '//', '^': '**', '×': '*', '÷': '/'}
        self.m = []

    def remake(self):
        self.string = self.string.lower()
        x = []

        flag = False
        if self.string.find('!') > -1:
            self.m = self.string.split('!')
            self.string = ''
            for i in range(len(self.m) - 1):
                for j in range(len(self.m[i]) - 1, -1, -1):
                    try:
                        x.append(int(self.m[i]))
                    except Exception:
                        flag = True
                    if not flag:
                        self.m[i] = ''
                        break
                    if flag:
                        if not self.m[i][j].isdigit():
                            k = j + 1
                            x.append(self.m[i][k:len(self.m[i])])
                            self.m[i] = self.m[i][0:k]
                            break
            for n in range(len(x)):
                #try:
                    #ошибка при ''
                x[n] = str(factorial(int(x[n])))
               # except Exception:
                #    self.string='ты что, ебобо?'
            for n in range(i + 2):
                if len(x) < n + 1:
                    self.string += self.m[n]
                else:
                    self.string += self.m[n] + x[n]


        for n in self.symbol:
            if self.string.find(n) > -1:
                self.m = self.string.split(n)
                self.string = ''
                #print(self.m)
                for i in range(len(self.m) - 0):
                    if len(self.m)>i+1:
                        self.string += self.m[i] + self.symbol.get(n)# + self.m[i + 1]
                    else:
                        self.string +=self.m[i]
                #print(self.string)
        return self.string

    def arithmetic(self):
        #self.string=Arithmetic(self.string).remake()
        #print(self.string)
        try:
            return (eval(self.string))
        except ValueError or NameError:
            return ('WTF???')
        except ZeroDivisionError:
            return ('А ты мозгами думать умеешь? (х_х)')
        except OverflowError:
            return ('this is big number, поэтому я тебе его не скажу (0о0)')
        except MemoryError:
            return ('ай, памяти не хватило (=_=)')
        except NameError:
            return ('Ты тупой? (-_-)')
        except Exception:
            return ('НУ ёбана...')#\n всё поламалося (._.) ( l: ) ( .-. ) ( :l ) (._.)')
#Arithmetic('X^5+x^4+X^3div5').remake()