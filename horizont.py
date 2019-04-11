#!/usr/local/bin/python

# Modified code for PyEphem to use with Motioneye
# and switchable IR camera at GPIO-port 17
# The code will decide to turn on/off the IR filter
# depending on its location set by the 
# GPS latitude/longitude/elevation
# **********************************************
# Original code from:
# a Python script for PyEphem
# http://rhodesmill.org/pyephem/
# to find out the sunrise and sunset time
# in UTC
# (add more code for the local time by yourself)
# by Kenji Rikitake 6-OCT-2009

from datetime import datetime, timedelta
from time import localtime, strftime
import time
import ephem
import RPi.GPIO as GPIO
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


def set_IR():

    SEC30 = timedelta(seconds=30)

    home = ephem.Observer()
    # replace lat, long, and elevation to yours
    home.lat = '48.8833'
    home.long = '8.3333'
    home.elevation = 172

    sun = ephem.Sun()

    fmt = "%d.%b.%Y %H:%M UTC"
    
    lfmt = "%d.%b.%Y %H:%M"
    sun.compute(home)
    lcurrtime=datetime.datetime.now()
    currtime=datetime.datetime.utcnow()
    nextrise = home.next_rising(sun)
    nextset = home.next_setting(sun)
    
    utcdiff=datetime.datetime.now()-datetime.datetime.utcnow()
    
    nextriseutc= nextrise.datetime() + SEC30
    nextsetutc= nextset.datetime() + SEC30
    nextrise= nextrise.datetime() + SEC30 + utcdiff
    nextset= nextset.datetime() + SEC30 + utcdiff    
    print "+++++++++++++++++++++++++++++++++++"
    print "current local time: ", lcurrtime.strftime(lfmt)
    #print "next local sunrise: ", nextrise.strftime(lfmt) 
    #print "next local sunset:  ", nextset.strftime(lfmt)     
    #print "current UTC time:   ", currtime.strftime(fmt)
    #print "next UTC sunrise:   ", nextriseutc.strftime(fmt)
    #print "next UTC sunset:    ", nextsetutc.strftime(fmt)
    #print "timediff:    ", utcdiff
    
    
    if nextriseutc.strftime(fmt)>nextsetutc.strftime(fmt):
        print "next is sunset at:  ", nextset.strftime(lfmt)
        print "IR is on -> GPIO17=1 "
        print "pesent: daylight "
        GPIO.output(17, GPIO.HIGH)
        
        
    if nextriseutc.strftime(fmt)<nextsetutc.strftime(fmt):
        print "next is sunrise at: ", nextrise.strftime(lfmt)
        print "present: night "
        print "IR is off -> GPIO17=0 "
        GPIO.output(17, GPIO.LOW)


if __name__ == '__main__':

    while True:
        set_IR()
        time.sleep(60)

# end of code
