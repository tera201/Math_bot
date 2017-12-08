from math import *
from sympy import symbols, diff, sin, cos, tan, asin, acos, atan, limit, log

x = symbols('x')
y = symbols('y')


class Arithmetic():
    def __init__(self, string):
        self.string = string
        self.symbol = {'mod': '%', 'div': '//', '^': '**', '×': '*', '÷': '/'}
        self.m = []

    def remake_in(self):
        self.string = self.string.lower()
        x = []
# подсчет факториала
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
                if x[n]!='':
                    x[n] = str(factorial(int(x[n])))
            for n in range(i + 2):
                if len(x) < n + 1:
                    self.string += self.m[n]
                else:
                    self.string += self.m[n] + x[n]

# замена операций на питоновские
        for n in self.symbol:
            if self.string.find(n) > -1:
                self.m = self.string.split(n)
                self.string = ''
                for i in range(len(self.m) - 0):
                    if len(self.m)>i+1:
                        self.string += self.m[i] + self.symbol.get(n)
                    else:
                        self.string +=self.m[i]
        return self.string

    def arithmetic(self):
        try:
            if len(self.string)<=3400:
                return (eval(self.string))
            else:
                self.string='слишкоом много символов'
                return self.string
        except ValueError or NameError:
            return ('WTF???')
        except ZeroDivisionError:
            return ('Ты шо ебобо? сейчас бы на ноль делить... (х_х)')
        except MemoryError:
            return ('ай, памяти не хватило (=_=)')
        except NameError:
            return ('И чего ты пытался этим добиться?')
        except Exception:
            return ('Что то идет не по плану...')