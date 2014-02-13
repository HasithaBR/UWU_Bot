////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                        //
//     Copyright (c) 2013, Anas Alhashimi LTU.                                                                            //
//     Copyright (c) 2014, HasithaBR, Uva Wellassa University                                                             //  
//     All rights reserved.                                                                                               //
//                                                                                                                        //
//     Redistribution and use in source and binary forms, with or without modification, are permitted provided that the   //
//     following conditions are met:                                                                                      //
//                                                                                                                        //
//      * Redistributions of source code must retain the above copyright notice, this list of conditions and the          //
//        following disclaimer.                                                                                           //
//      * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the       //
//        following disclaimer in the documentation and/or other materials provided with the distribution.                //
//      * Neither the name of Uva Wellassa University nor the names of its contributors may be used to endorse or promote //
//        products derived from this software without specific prior written permission.                                  //
//                                                                                                                        //
//     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, //
//     INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE  //
//     DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,  //
//     SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    //
//     SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,  //
//     WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE   //
//     USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                           //
//                                                                                                                        //
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#include <ros/ros.h>
#include "geometry_msgs/Twist.h"
#include "sensor_msgs/Imu.h"
#include <signal.h>
#include <termios.h>

using geometry_msgs::Twist;
using namespace std;

ros::Publisher chatter_pub;
ros::Time t1;
Twist vel;
int kfd = 0;
struct termios cooked, raw;
unsigned int temp=0;
float x;
float y;
float z;

void quit(int sig){
  tcsetattr(kfd, TCSANOW, &cooked);
  ros::shutdown();
  exit(0);
}

void anCallback(const sensor_msgs::Imu::ConstPtr& ansmsg){
 x=ansmsg->angular_velocity.x;
 y=ansmsg->angular_velocity.y;
 z=ansmsg->angular_velocity.z;
}

int main(int argc, char** argv){ 
  int ther=5;

  ros::init(argc, argv, "android_teleop");
  ros::NodeHandle n;
   chatter_pub = n.advertise<Twist>("/cmd_vel", 1);  
   signal(SIGINT,quit);
        ros::Rate r(5);
   char c;
   bool dirty=false;   
   t1=ros::Time::now();

   tcgetattr(kfd, &cooked);
   memcpy(&raw, &cooked, sizeof(struct termios));
   raw.c_lflag &=~ (ICANON | ECHO);
   raw.c_cc[VEOL] = 1;
   raw.c_cc[VEOF] = 2;
   tcsetattr(kfd, TCSANOW, &raw);

   //subscribe to android imu sensor msgs
   ros::Subscriber imu_pub = n.subscribe<sensor_msgs::Imu>("/android/imu", 1, anCallback);
 
	while (ros::ok()){     
		if(x > ther){
			  vel.linear.x = 0.2;
			  vel.linear.y=0;
			  vel.linear.z=0;
			  vel.angular.x = 0;
			  vel.angular.y = 0;
			  vel.angular.z = 0;
			  ROS_INFO("Forward");
		}
		if(x < -ther){
				vel.linear.x = -0.2;
				vel.linear.y=0;
				vel.linear.z=0;
				vel.angular.x = 0;
				vel.angular.y = 0;
				vel.angular.z = 0;
				ROS_INFO("Backward");
		}
		if(z > ther){
			  vel.linear.x = 0;
			  vel.linear.y=0;
			  vel.linear.z=0;
			  vel.angular.x = 0;
			  vel.angular.y = 0;
			  vel.angular.z = 0.5;
			  ROS_INFO("Turnleft");
		}
		if(z < -ther){
				vel.linear.x = 0;
				vel.linear.y=0;
				vel.linear.z=0;
				vel.angular.x = 0;
				vel.angular.y = 0;
				vel.angular.z = -0.5;
				ROS_INFO("Turnright");
		}
		if(y < -ther){
				vel.linear.x = 0;
				vel.linear.y=0;
				vel.linear.z=0;
				vel.angular.x = 0;
				vel.angular.y = 0;
				vel.angular.z = 0;
				ROS_INFO("STOP");
		}
		if(y > ther){
				vel.linear.x = 0;
				vel.linear.y=0;
				vel.linear.z=0;
				vel.angular.x = 0;
				vel.angular.y = 0;
				vel.angular.z = 0;
				ROS_INFO("STOP");
		}

		chatter_pub.publish(vel);
				     
		ros::Duration(0.1).sleep();
		ros::spinOnce();
	}

return(0);
}


