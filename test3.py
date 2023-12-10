class time:
    def __init__(self,h,m,s):
        self.s=s
        self.m=m
        self.h=h
        '''if self.s>=60:
            self.s-=60
            self.m+=1
            
        if self.m>=60:
            self.m-=60
            self.h+=1
            '''
        #self.show()
        self.fix() #ba gozashtane fix( mitoonim shartaye tavabeo hazf konim chon tabe init bedoone farakhani ejra mishe)
        

    def sum(self,time2):
        self.result_h=self.h+time2.h
        self.result_m=self.m+time2.m
        self.result_s=self.s+time2.s
        if self.result_s>=60:
            self.result_s-=60
            self.result_m+=1
        if self.result_m>=60:
            self.result_m-=60
            self.result_h+=1
        result=time(self.result_h,self.result_m,self.result_s)
        return result


    def sub(self,time2):
        result_h=self.h-time2.h
        result_m=self.m-time2.m
        result_s=self.s-time2.s

        if result_s<=0:
            result_s+=60
            result_m-=1
        if result_m<=0:
            result_m+=60
            result_h-=1
        result=time(result_h,result_m,result_s)
        return result
        

    def show(self):
        print(f"{self.h}:{self.m}:{self.s}")

    def fix(self):

        if self.s<=0:
            self.s+=60
            self.m-=1

        if self.m<=0:
            self.m+=60
            self.h-=1

        if self.s>=60:
            self.s-=60
            self.m+=1

        if self.m>=60:
            self.m-=60
            self.h+=1
        return
            
    def gmt_to_tehran(self):
        t=time(3,30,0)
        tehran_time = self.sum(t)
        return tehran_time 

    @staticmethod
    def time_to_second(h,m,s):
        seconds=s
        s_m=m*60
        s_h=h*3600

        result_s=seconds+s_m+s_h
        return result_s

        
    @staticmethod
    def second_to_time(seconds):
        h = seconds // 3600
        seconds = seconds-(h * 3600)
        m = seconds//60
        seconds = seconds-(m * 60)
        s=seconds

        t=time(h,m,s)
        return t
    
   
        


time1= time(8,20,85)
time1.show()

time2= time(7,35,20)
time2.show()
t5=time.second_to_time(5000)
t5.show()

result_sum=time1.sum(time2)
result_sum.show()

time3=time(7,0,0)
time4=time3.gmt_to_tehran()
time4.show()

time5= time.second_to_time(35000)
time5.show()

time6=time.time_to_second(1,0,0)
print(time6)

