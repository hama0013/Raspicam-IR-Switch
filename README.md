# https://hama0013.github.io/Raspicam-IR-Switch/
MotionEye is a great tool for building a surveillance camera. The only problem is the missing IR switching functionality but can be simply integrated via Python programming by using a switchable IR-filter camera over GPIO-port. The control to turn on/off should be calculated for every sunrise/sunset automatically by its location defined coordinates(latitude/longitude). Additionally an external IR spot light can/should be used for night recordings/views. I recommend	something like this:
![ScreenShot](https://github.com/hama0013/Raspicam-IR-Switch/blob/master/pic_small/irspotlight.png)<br>
**What do we need?:**<br>
RaspberryPi CSI camera with switchable IR activation port. I recommend this one from Banggood: (It can be used any other one, but note the possibility to connect an activation hardware line with 3.3V support)
![ScreenShot](https://github.com/hama0013/Raspicam-IR-Switch/blob/master/pic_small/2019-04-11%2022_09_09-geekworm%20camera%20with%20ir-cut%20function%20for%20raspberry%20pi%203b_%202b_%20b+_%20a+_%20zero%20avail.png)<br>

**Hardware connection:**<br>
Typically the CSI cable is delivered with the camera. But the hardware wire for the IR activator has to be organiced self. The hardware wire	to the activation port must be soldered at the camera and connected over single pin connector to the Raspis GPIO-port. I‘m using port 17(Pin 11). That’s all to make it working…
![ScreenShot](https://github.com/hama0013/Raspicam-IR-Switch/blob/master/pic_small/2019-04-11%2022_25_33-CAM_GPIO.png)<br>
**Software:**<br>
_**Preparation:**_<br>
This described integration is not working with MotionEyeOS because of its limited OS. Better is to install latest Raspbian https://www.raspberrypi.org/downloads/raspbian/ and install MotionEye manually. Well described here: https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian
I‘ve made all coding with Python over the programming software „Geany“. The programing should calculate next nunrise/sunset automatically every minute and decide what's the current situation (day/night) and turn on/of the IR filter over GPIO-17. The Python libraries need an additional installation to use the sunrise/sunset calculations from “ephem”, that can be made very easy with this command in the terminal window:

<pre><code><B>sudo pip install ephem</B></pre></code>

The original program is derived from http://rhodesmill.org/pyephem/ The changes are:
- additional text output for local times (current, next sunset/sunrise)
- additional decision of current situation (day/night), text output, set of the IR pin
- cyclically call every 60 seconds

Take the code from this repository: horizont.py and start at your Raspi with following command:

<pre><code><B>python horizont.py</B></pre></code>

You should see something like this:<br>
![ScreenShot](https://github.com/hama0013/Raspicam-IR-Switch/blob/master/pic_small/horizont_screen.png)
