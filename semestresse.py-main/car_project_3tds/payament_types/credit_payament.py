from payament_times import *
from config import *
from payament_times.in_time import in_time
from payament_times.three_months import payament_three
from payament_times.six_months import payament_six
from payament_times.nine_months import payament_nine
from payament_times.twelve_months import payament_twelve

def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return (in_time(desired_car))
    
    elif(time_option == 2):
        return (payament_three(desired_car))
    
    elif(time_option == 3):
        return (payament_six(desired_car))
    
    elif(time_option == 4):
        return (payament_nine(desired_car))
    
    elif(time_option == 5):
        return (payament_twelve(desired_car))
