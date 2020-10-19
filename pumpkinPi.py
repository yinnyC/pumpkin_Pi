# pumpkinPi.py
# Measure distance using an ultrasonic module
# in a loop. Plays Mp3 at certain distance detection
#

# --------------------------------
# Import required Python libraries
# --------------------------------
import time
import datetime
import os
import random
import RPi.GPIO as GPIO
import statistics
import random
import picamera
import json

# --------------------------------
# Declear Global Variables
# --------------------------------
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 18
GPIO_ECHO = 24

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO, GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)
time.sleep(0.5)  # Allow module to settle
speedSound = 34300

filepath = os.path.dirname(__file__)
dir_path = os.path.join(filepath, "static/target_captured")


soundPathList = [os.path.join(filepath, 'Resources/sounds/Cat_Scream.mp3'),
                 os.path.join(filepath, 'Resources/sounds/Dark_Laugh.mp3'),
                 os.path.join(filepath, 'Resources/sounds/Evil_Laugh.mp3'),
                 os.path.join(
                     filepath, 'Resources/sounds/I_will_kill_you.mp3'),
                 os.path.join(filepath, 'Resources/sounds/Witches_Laugh.mp3')
                 ]

camera = picamera.PiCamera()
print("Ultrasonic Measurement")


def get_distance():
    """ This function takes in data and calculate the distance """
    GPIO.output(GPIO_TRIGGER, True)  # Send 10us pulse to trigger
    time.sleep(0.00001)              # Wait 10us
    GPIO.output(GPIO_TRIGGER, False)  # Set trigger to False (Low)
    start = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * speedSound) / 2

    return distance


def get_avgdistance():
    """ This function takes 3 measurements and return Avg distance """
    distanceList = []
    for _ in range(3):
        d = get_distance()
        time.sleep(0.1)
        distanceList.append(d)
    return statistics.mean(distanceList)


def readExistingImgPath():
    dataList = []
    for (path, dirList, fileList) in os.walk(dir_path):
        for f in fileList:
            dataList.append(os.path.join("/static/target_captured", f))
    return dataList


def dumpInData(imgList):
    with open(os.path.join(filepath, 'ImgData.json'), 'w') as fh:
        json.dump(imgList, fh, indent=3)


def captureTarget():
    timestamp = datetime.datetime.now()
    relativePath = f"static/target_captured/{timestamp.strftime('%d%b%Y_%H%M%S')}.jpg"
    img_filepath = os.path.join(filepath, relativePath)
    camera.capture(img_filepath)
    updateFile()

def updateFile():
    imgList = readExistingImgPath()
    dumpInData(imgList)

while True:
    try:
        distance = get_avgdistance()
        updateFile()
        print("Distance : %.1f" % distance)
        if(distance == 0 or distance < 100):
            path = random.choice(soundPathList)
            captureTarget()
            os.system(f"mpg321 {path}")
            time.sleep(3)  # time between loop iterations
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        GPIO.cleanup()