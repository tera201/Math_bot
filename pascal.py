class Triangle():
    def __init__(self,num):
        self.num=num
        self.k=''

    def soch(self,a,b):
        import math
        return(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))

    def TP(self):
        p=True
        try:
            self.num=int(self.num)
        except Exception:
            p=False

        if p and p<50:
            for i in range(self.num):
                for p in range(self.num - i, 0, -1):
                    self.k += ' '
                for j in range(i + 1):
                    self.k += str(int(self.soch(i, j))) + ' '
                self.k += '\n'
            return self.k
        else:
            self.k = 'ты блять в скобочках цыфру даже написать не могешь?'
            return  self.k
print(Triangle(6).TP())