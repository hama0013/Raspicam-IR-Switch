<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 5.2.7.2 (Linux)"/>
	<meta name="created" content="00:00:00"/>
	<meta name="changed" content="2019-04-12T00:23:04.840160640"/>
	<style type="text/css">
		@page { margin: 2cm }
		td p { background: transparent; direction: inherit }
		a.western:visited { so-language: en-US }
	</style>
</head>
<body lang="en-US" dir="ltr">
<table width="100%" cellpadding="0" cellspacing="0" style="page-break-before: always; page-break-after: auto; page-break-inside: avoid">
	<col width="34*">
	<col width="185*">
	<col width="37*">
	<tr valign="top">
		<td width="13%" style="border: none; padding: 0cm">
			<p><br/>

			</p>
		</td>
		<td width="72%" style="border: none; padding: 0cm">
			<p align="center"><font color="#cc0000"><font face="Liberation Serif"><font size="7" style="font-size: 32pt"><u><b>Using
			PiCamera (CSI) with switchable IR filter<br/>
and </b></u></font></font></font><font color="#cc0000"><font face="Liberation Serif"><font size="7" style="font-size: 32pt"><u><b>GPS
			</b></u></font></font></font><font color="#cc0000"><font face="Liberation Serif"><font size="7" style="font-size: 32pt"><u><b>horizon
			controlled activation</b></u></font></font></font></p>
		</td>
		<td width="14%" style="border: none; padding: 0cm">
			<p><br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="13%" style="border: none; padding: 0cm">
			<p><br/>

			</p>
		</td>
		<td width="72%" style="border: none; padding: 0cm">
			<p style="background: transparent"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><b>Motivation:<br/>
</b>MotionEye
			is a great tool for building a surveillance camera. The only
			problem is the missing IR switching functionality but can be
			simply integrated via Python programming by using a switchable
			IR-filter camera over GPIO-port. Additionally an external IR spot
			light can/should be used for night recordings/views. I recommend
			something like this:<br/>
</font></font><br/>
<br/>

			</p>
			<table width="100%" cellpadding="4" cellspacing="0">
				<col width="256*">
				<tr>
					<td width="100%" valign="top" style="border: none; padding: 0cm">
						<p><img src="pic_small/irspotlight.png" name="Image4" align="left" width="856" height="268" border="0"/>
<br/>

						</p>
					</td>
				</tr>
			</table>
			<p style="background: transparent"><br/>
<br/>

			</p>
			<p style="background: transparent"><br/>
<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><b>What
			do we need?:</b></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">A
			RaspberryPi CSI camera with switchable IR activation port. I
			recommend this one from Banggood: (It can be used any other one,
			but note the possibility to connect an activation hardware line
			with 3.3V support)</font></font></font></p>
			<table width="100%" cellpadding="4" cellspacing="0">
				<col width="256*">
				<tr>
					<td width="100%" valign="top" style="border: none; padding: 0cm">
						<p align="left"><img src="pic_small/2019-04-11%2022_09_09-geekworm%20camera%20with%20ir-cut%20function%20for%20raspberry%20pi%203b_%202b_%20b+_%20a+_%20zero%20avail.png" name="Image1" align="left" width="753" height="264" border="0"/>
<br/>

						</p>
					</td>
				</tr>
			</table>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><b>Hardware
			connection:</b></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">Typically
			the CSI cable is delivered with the camera. But the hardware wire
			for the IR activator has to be organiced self. The hardware wire
			to the activation port must be soldered at the camera and
			connected over single pin connector to the Raspis GPIO-port. I‘m
			using port 17(Pin 11). That’s all to make it working…</font></font></font></p>
			<table width="100%" cellpadding="4" cellspacing="0">
				<col width="256*">
				<tr>
					<td width="100%" valign="top" style="border: none; padding: 0cm">
						<p align="left"><img src="pic_small/2019-04-11%2022_25_33-CAM_GPIO.png" name="Image2" align="left" width="777" height="230" border="0"/>
<br/>

						</p>
					</td>
				</tr>
			</table>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><b>Software:</b></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><i>Preparation:</i></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">This
			described integration is not working with MotionEyeOS because of
			its limited OS. Better is to install latest Raspbian
			„<a class="western" href="https://www.raspberrypi.org/downloads/raspbian/" name="Raspbian">https://www.raspberrypi.org/downloads/raspbian/</a>“
			and install MotionEye manually. Well described here:
			„<a class="western" href="https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian" name="Motioneye">https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian</a>“</font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; background: transparent; text-decoration: none">
			<font color="#000000"><font face="FreeSans, serif"><font size="5" style="font-size: 18pt"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">I‘ve
			made </span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">a</span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">ll
			</span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">coding</span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">
			with Python over the programming software „Geany“. The Python
			l</span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">i</span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">braries
			need </span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">an
			</span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">a</span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">d</span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">ditional
			installation </span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">to
			use the sunrise/sunset calculations from “ephem”, </span></font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">that
			can be made very easy with this command in the terminal window:<br/>
</span></font></font></font></font></font><br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; background: transparent; text-decoration: none">
			<font color="#000000"><font face="FreeSans, serif"><font size="5" style="font-size: 18pt"><font face="Liberation Sans, serif"><font size="3" style="font-size: 12pt"><b>s</b></font></font><font face="Liberation Sans, serif"><font size="3" style="font-size: 12pt"><b>udo
			pip install ephem<br/>
</b></font></font></font></font></font><br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; background: transparent; text-decoration: none">
			<font color="#000000"><font face="FreeSans, serif"><font size="5" style="font-size: 18pt"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">The
			original program is derived from „
			http://rhodesmill.org/pyephem/“ The changes are</font></font><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><span style="font-weight: normal">:</span></font></font></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">-
			additional text output for local times (current, next
			sunset/sunrise)</font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">-
			additional decision of current situation (day/night), text output,
			set of the IR pin</font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="FreeSans, serif"><font size="5" style="font-size: 18pt"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">-
			cyclically call every 60 seconds</font></font></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="FreeSans, serif"><font size="5" style="font-size: 18pt"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">Take
			the code from this repository: horizont.py and start at your Raspi
			with following command:</font></font></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="FreeSans, serif"><font size="5" style="font-size: 18pt"><b><font face="Liberation Serif"><font size="3" style="font-size: 12pt">python
			horizont.py</font></font></b></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; line-height: 0.35cm; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="FreeSans, serif"><font size="5" style="font-size: 18pt"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">You
			should see something like this:</font></font></font></font></font></p>
		</td>
		<td width="14%" style="border: none; padding: 0cm">
			<p><br/>
<br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="13%" style="border: none; padding: 0cm">
			<p><br/>
<br/>

			</p>
		</td>
		<td width="72%" style="border: none; padding: 0cm">
			<p style="background: transparent"><img src="pic_small/horizont_screen.png" name="Image3" align="left" width="614" height="392" border="0"/>
<br/>
<br/>

			</p>
		</td>
		<td width="14%" style="border: none; padding: 0cm">
			<p><br/>
<br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="13%" style="border: none; padding: 0cm">
			<p><br/>
<br/>

			</p>
		</td>
		<td width="72%" style="border-top: none; border-bottom: 1.00pt solid #000000; border-left: none; border-right: none; padding: 0cm">
			<p><br/>
<br/>

			</p>
		</td>
		<td width="14%" style="border: none; padding: 0cm">
			<p><br/>
<br/>

			</p>
		</td>
	</tr>
</table>
<p><br/>
<br/>

</p>
</body>
</html>
