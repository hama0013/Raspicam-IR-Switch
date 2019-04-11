# Raspicam-IR-Switch
Raspicam IR-Switch by location horizont sunrise/sunset calculation

Complete description as HTML


<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 5.2.7.2 (Linux)"/>
	<meta name="created" content="00:00:00"/>
	<meta name="changed" content="2019-04-11T22:44:45.142091062"/>
	<style type="text/css">
		@page { margin: 2cm }
		td p { background: transparent; direction: inherit }
		a.western:visited { so-language: en-US }
	</style>
</head>
<body lang="en-US" dir="ltr">
<table width="100%" cellpadding="0" cellspacing="0" style="page-break-before: auto; page-break-after: auto; page-break-inside: avoid">
	<col width="34*">
	<col width="185*">
	<col width="37*">
	<tr valign="top">
		<td width="13%" style="border: none; padding: 0cm">
			<p><br/>

			</p>
		</td>
		<td width="72%" style="border: none; padding: 0cm">
			<p align="center"><font color="#cc0000"><font size="7" style="font-size: 32pt"><u><b><font face="Liberation Serif">Using
			PiCamera (CSI) with switchable IR filter and horizon controlled
			activation</font></b></u></font></font></p>
			<p align="center"><br/>

			</p>
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
			problem is the missing night switching functionality but can be
			simply integrated via Python programming by using a switchable
			IR-filter camera over GPIO-port. Additional an external IR light
			spot can be used.</font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><b>What
			do we need?:</b></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">A
			RaspberryPi CSI camera with switchable activation port. I
			recommend this one from Banggood: (It can be used any other one,
			but note the possibility to connect an activation hardware line
			with 3.3V support)</font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<img src="horizont_html_bb18e393298be4f.png" name="Image1" align="left" width="455" height="159" border="0"/>
<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><b>Hardware
			connection:</b></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">Typically
			the CSI cable is delivered with the camera. The hardware wire to
			the activation port must be welded at the camera and connected
			over single pin connector to the Raspis GPIO-port. I‘m using
			port 17(Pin 11). Thats all to make it working…</font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<img src="horizont_html_ac6f71762774137a.png" name="Image2" align="left" width="464" height="138" border="0"/>
<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><b>Software:</b></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><i>Preparation:</i></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">This
			described integration is not working with MotionEyeOS because of
			its limited OS. Better is to install latest Raspbian
			„<a class="western" href="https://www.raspberrypi.org/downloads/raspbian/" name="Raspbian">https://www.raspberrypi.org/downloads/raspbian/</a>“
			and install MotionEye manually. Well described here:
			„<a class="western" href="https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian" name="Motioneye">https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian</a>“</font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; background: transparent; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">All
			program I‘ve made with Python over the programming software
			„Geany“. The Python libraries need an additional installation
			that can be made very easy with this command in the terminal
			window:</font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; background: transparent; text-decoration: none">
			<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; background: transparent; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt"><font face="Liberation Sans, serif">Sudo
			pip install ephem</font></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<br/>

			</p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">The
			original program is derived from „
			http://rhodesmill.org/pyephem/“ The changes are<span style="font-weight: normal">:</span></font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">-
			additional text output for local limes (current, next
			sunset/sunrise)</font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">-
			additional decision of current situation (day/night), text output,
			set of the IR pin</font></font></font></p>
			<p align="left" style="margin-bottom: 0cm; font-style: normal; font-weight: normal; orphans: 2; widows: 2; text-decoration: none">
			<font color="#000000"><font face="Liberation Serif"><font size="3" style="font-size: 12pt">-
			cyclically call every 60 seconds </font></font></font>
			</p>
			<p style="margin-bottom: 0cm; font-weight: normal; background: transparent">
			<br/>

			</p>
			<p style="background: transparent"><br/>
<br/>

			</p>
			<p style="background: transparent"><br/>

			</p>
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
		<td width="72%" style="border-top: none; border-bottom: 1.00pt solid #000000; border-left: none; border-right: none; padding: 0cm">
			<p><br/>

			</p>
		</td>
		<td width="14%" style="border: none; padding: 0cm">
			<p><br/>

			</p>
		</td>
	</tr>
</table>
<p><br/>
<br/>

</p>
</body>
</html>
