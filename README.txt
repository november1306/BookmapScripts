1. install Sikuli IDE (ensure you have JRE 7,8 or JDK installed)
	https://launchpad.net/sikuli/sikulix/1.1.0/+download/sikulixsetup-1.1.0.jar
	choose to install Pack 1 only with Python

2. Install BookMap 5.0, activate it	
	Ensure that feed_Rithmic_20160923_133501_092.bmf is present in Feeds folder. 

3. Put LaunchAppScript.sikuli folder and runscript.bat into the Sikuli IDE folder
	launch runscript.bat from the package ('as administrator' is desirable )

Script actions: 
- launches the app;
- choos data source on dialog;
- choose file with recorded data;
- wait while visualization starts;
- pin down timer + pause button panel;
- wait for 13:35:30 on timer;
- take screenshot #1;
- continue play, wait for 13:36:10;
- pause, take screenshot #2;
- Exit

