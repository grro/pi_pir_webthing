import logging
import RPi.GPIO as GPIO
from datetime import datetime


class MotionSensor:

    def __init__(self, gpio_number):
        self.__listener = lambda: None    # "empty" listener
        self.gpio_number = gpio_number
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_number, GPIO.IN)
        GPIO.add_event_detect(self.gpio_number, GPIO.BOTH, callback=self.__update, bouncetime=5)
        self.is_motion = False
        self.last_motion_date = datetime.now()

    def set_listener(self,listener):
        self.__listener = listener

    def __notify_listener(self):
        try:
            self.__listener()
        except Exception as e:
            logging.warning(str(e))

    def __update(self, channel):
        if GPIO.input(self.gpio_number):
            logging.info("motion detected")
            self.is_motion = True
            self.last_motion_date = datetime.now()
            self.__notify_listener()
        else:
            self.is_motion = False
            self.__notify_listener()


