class fraction:
    def __init__(self,s,m):
        self.s=s
        self.m=m

    def show(self):
        print(self.s,"/",self.m) 

    def sum(self,f2):
        result_s = (self.s * f2.m) + (f2.s * self.m)
        result_m = (self.m) * (f2.m)
        result=fraction(result_s,result_m)
        return result

    def mul(self,f2):
       # result=(self.s*f2.s)/(self.m*f2.m) <= def mul(self,f2):
        result_s = (self.s) * (f2.s)
        result_m = (self.m) * (f2.m)
        result=fraction(result_s,result_m)
        return result

    def sub(self,f2):
        result_s = (self.s * f2.m) - (f2.s * self.m)
        result_m = (self.m) * (f2.m)
        result=fraction(result_s,result_m)
        return result

    def div(self,f2):
        if self.m==0 or f2.s==0:
            print('error!')
        else:
            result_s = (self.s) * (f2.m)
            result_m = (self.m) * (f2.s)
            result=fraction(result_s,result_m)
            return result

f1=fraction(2,3)
f1.show()

f2=fraction(4,5)
f2.show()

#result_m
result_1=f1.mul(f2)
#print(result_m)
result_1.show()

result_2=f1.sum(f2)
result_2.show()

result_3=f1.sub(f2)
result_3.show()

result_4=f1.div(f2)
result_4.show()