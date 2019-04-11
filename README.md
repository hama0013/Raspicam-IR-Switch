# Raspicam-IR-Switch
Raspicam IR-Switch by location horizont sunrise/sunset calculation

Complete description as HTML


Motivation:
MotionEye is a great tool for building a surveillance camera. The only problem is the missing night switching functionality but can be simply integrated via Python programming by using a switchable IR-filter camera over GPIO-port. Additional an external IR light spot can be used.
What do we need?:
A RaspberryPi CSI camera with switchable activation port. I recommend this one from Banggood: (It can be used any other one, but note the possibility to connect an activation hardware line with 3.3V support)


Hardware connection:
Typically the CSI cable is delivered with the camera. The hardware wire to the activation port must be welded at the camera and connected over single pin connector to the Raspis GPIO-port. I‘m using port 17(Pin 11). Thats all to make it working…


Software:
Preparation:
This described integration is not working with MotionEyeOS because of its limited OS. Better is to install latest Raspbian „https://www.raspberrypi.org/downloads/raspbian/“ and install MotionEye manually. Well described here: „https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian“
All program I‘ve made with Python over the programming software „Geany“. The Python libraries need an additional installation that can be made very easy with this command in the terminal window:

Sudo pip install ephem

The original program is derived from „ http://rhodesmill.org/pyephem/“ The changes are:
- additional text output for local limes (current, next sunset/sunrise)
- additional decision of current situation (day/night), text output, set of the IR pin
- cyclically call every 60 seconds 
