#!/usr/bin/env python3
#
#
#
### Create a python like tester file to  see if we can obtain the international normalized ratio and the ptt of blood. This is going to be used for to get the inital results for the INR ratio. then It'll be called again to figure out what is going on.  
# 
# 
#
__author__ = "Samuel Young"
__copyright__ = " Copyright 2016, The INR project"
__credits__ = ["Samuel Young"]
__license__ = "GPL"
__version__ = "0.0.812"
__maintianer__ = "Samuel Young"
__email__ = "samuel.young.103@gmail.com"
__status__ = "beta"
#### dependencies ##### 

import time
import RPi.GPIO as GPIO
import collections

# from datetime import timedelta
# from threading


#### variables ####
# ptdrawc2= input('INR')
# ptnomdrawc2= int(ptdrawc2)
##### GPIO  #######

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class LightSensor(object):
    def __init__(self, light, reflection):
        self.light = light
        self.reflection = reflection

   # @staticmethod this method causes any error 
    def reset(self):
        GPIO.cleanup()
        print("Gpio Cleanup has been done")

    @property
    def sensor(self):
        change = 0.0
        value = True

        print("setting up  pins")
        GPIO.setup(self.reflection, GPIO.OUT)
        GPIO.output(self.reflection, GPIO.LOW)
        GPIO.setup(self.light, GPIO.OUT)
        
        
        # led_off= GPIO.output(self.light,GPIO.LOW)
        # time.sleep(7.5)
        
        
        print("testing light")
        
        
        on = GPIO.output(self.light, GPIO.HIGH)
        time.sleep(1)
        
        
        print("Setup the input pin")
        
        GPIO.setup(self.reflection, GPIO.IN)
        
        reflector = GPIO.input(self.reflection)
        
        timer = time.perf_counter()
        '''
        This  that the time should be below 90.0 second or until the value does not read as true  it must be reaching the value at the end of the rainbow
        '''
        while (time.perf_counter() - timer) < 90.0 or value is not True:
            reflector
            on
            time.sleep(.0000000001)
            finish = time.perf_counter()
            if reflector == 0:
                on
                time.sleep(.0000000001)
                change = finish - timer
            elif .01 <= reflector <= .99:
                on
                time.sleep(.0000000001)
                change = finish - timer
            else:
                GPIO.output(self.light, GPIO.LOW)
                change = finish - time
                value = False
                break
        return change


#### this is the class that will be defined as how the device will calculate the ptt\ptNorm  values
'''
class ptt_and_norm_reader(object):
    def __init__(self, light, reflection):
        self.light = light
        self.reflection = reflection
    def ptt_draw(self):
        l_sensor=LightSensor(self.light,self.reflection)
        print(" PTT LightSenors array in use")
        light_sensor=l_sensor.light_Sensor()
        l_sensor.reset()
        return light_sensor
    def norm_draw(self):
        l_sensor=LightSensor(self.light,self.reflection)
        print("Norm LightSenors array in use")
        light_sensor=l_sensor.light_Sensor()
        l_sensor,reset()
        return light_sensor
    def ptt_reader(self):
        pt_drawing = self.ptt_draw()
        return pt_drawing
    def norm_reader(self):
        norm_drawing = self.norm_draw()
        return norm_drawing
'''

'''
these are the four threads that I am trying to run to get any average for the individual 
'''


def main():
    '''
   each sensor is being called
   '''
    l_sensor0 = LightSensor(24, 18)
    l_sensor1 = LightSensor(23, 17)
    # l_sensor2 = LightSensor(22,16)
    # l_sensor3 = LightSensor(25,12)
    '''
   each value of the sensor is being retuend then printed
   '''
    val_sensor0 = l_sensor0.sensor
    val_sensor1 = l_sensor1.sensor
    # val_sensor2 = l_sensor2.light_Sensor()
    # val_sensor3 = l_sensor3.light_Sensor()
    '''
   what each value is being sent to the manchine
   '''
    print(val_sensor0)
    print(val_sensor1)
    # print(val_sensor2)
    # print(val_sensor3)

    l_sensor0.reset()

if __name__ == "__main__":
     main()
''' this is any artifact in which I need to find out how it 
GPIO.add_event_callback(l_Sensor0 , t1)
GPIO.add_event_callback(l_Sensor1 , t2)
GPIO.add_event_callback(l_Sensor2 , t3)
GPIO.add_event_callback(l_Sensor3 , t4)
'''
