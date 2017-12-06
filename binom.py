class nuiton():
    def __init__(self, string):
        self.string = string
        self.m = []

    def main(self):

        self.m = self.string.split('**')
        flag = True
        try:
            n = int(self.m[1])
        except Exception:
            flag = False
            self.string = 'степень записана не верно, ебанько'
        if flag:
            self.m = self.m[0][1:-1]
            self.m = self.m.split('+')
            v = []
            for i in self.m:
                v.append(i.split('-'))
            self.m = []
            for a in v:
                for i in range(len(a)):
                    if i > 0:
                        self.m.append('-' + a[i])
                    else:
                        self.m.append('+' + a[i])
            if len(self.m) > 2:
                flag = False
                return 'continue'
        if flag and self.m[0][1:].isdigit() and self.m[1][1:].isdigit():
            flag = False
            return 'continue'
        print(n)
        if flag:
            k = ''
            t=float
            import math
            for i in range(n + 1):
                t =int(math.factorial(n) / (math.factorial(i) * math.factorial(n - i)))
                k +='+'+ str(t) + self.m[0][1:] + '^' + str(n - i)+'*' + self.m[1][1:] + '^' + str(i)
            return k
        print(self.m,' ',n)