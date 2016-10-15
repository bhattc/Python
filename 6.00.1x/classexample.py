class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self,time):
        #time = '6:30'
        print time
        


clock = Clock('5:30')
clock.print_time('10:30')
