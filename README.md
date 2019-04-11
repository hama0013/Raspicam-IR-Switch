# https://hama0013.github.io/Raspicam-IR-Switch/
Raspicam IR-Switch by location horizont sunrise/sunset calculation

This described integration is not working with MotionEyeOS because of its limited OS. Better is to install latest Raspbian „https://www.raspberrypi.org/downloads/raspbian/“ and install MotionEye manually. Well described here: „https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian“
I‘ve made all coding with Python over the programming software „Geany“. The Python libraries need an additional installation to use the sunrise/sunset calculations from “ephem”, that can be made very easy with this command in the terminal window:

sudo pip install ephem

The original program is derived from „ http://rhodesmill.org/pyephem/“ The changes are:
- additional text output for local times (current, next sunset/sunrise)
- additional decision of current situation (day/night), text output, set of the IR pin
- cyclically call every 60 seconds

Take the code from this repository: horizont.py and start at your Raspi with following command:

python horizont.py







https://hama0013.github.io/Raspicam-IR-Switch/



