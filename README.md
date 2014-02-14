_______________________________________
UWU_Bot
=======
_______________________________________

This is UWU_Bot which is made for 3D mapping in outdoor purposes but it is capable for indoor also. The documentation is placed at http://wiki.ros.org/UWU_Bot

The total package assembled for easy testings. ccny_rgbd, openni, rosserial packages used for mapping, kinect data, arduino connection respectively. The file names changed for easy understanding. The people who build pervious packages mentioned above have their rights.

Arduino is directly connected to the UWU_Bot main laptop and to the high power motor controller and it handles velocity commands and out the motor commands. No other sensors integrated yet. 


Note: 
-----
If you are facing a rosmake failure issue, do this before open an issue

1. Please check your ROS_PACKAGE_PATH and verify this psckage is in that path.
2. Delete the file UWU_Bot/build/CMakeCache.txt and try.




_____________________________________________________________________

Uva Wellassa University of Sri Lanka
------------------------------------
MECHATRONICS
____________
