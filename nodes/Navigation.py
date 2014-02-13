#!/usr/bin/env python

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                        //
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
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''


import roslib; roslib.load_manifest('UWU_Bot')
import rospy

from geometry_msgs.msg import Twist

def nav():
    pub = rospy.Publisher('cmd_vel', Twist)
    rospy.init_node('UWU_Bot')

    rospy.loginfo("______________________________________________________")   
    rospy.loginfo("       **       Initiallizing UWU_Bot        **       ")
    rospy.loginfo("________________________***___________________________")
    rospy.loginfo("")
    rospy.sleep(3)

    twist = Twist()

    twist.linear.x = 0.5						# nav uwu_bot foward 0.1 m/s for 5s   
    rospy.loginfo("Moving	FOWARD")
    pub.publish(twist)
    rospy.sleep(5.3)

    twist.linear.x = -0.1 						# nav uwu_bot backward 0.1 m/s for 8.5s
    rospy.loginfo("Moving	BACKWARD")
    pub.publish(twist)
    rospy.sleep(4.5)

    twist = Twist()

    twist.angular.z = 0.5						# Turn uwu_bot left only at 0.5 rad/s for 3.9s, No linear velocity
    rospy.loginfo("Turning	LEFT")
    pub.publish(twist)
    rospy.sleep(7.9)
    
    twist.angular.z = -0.5						# Turn uwu_bot right only at 0.5 rad/s for 6.4s, No linear velocity
    rospy.loginfo("Turning	RIGHT")
    pub.publish(twist)
    rospy.sleep(6.4)

    twist = Twist()

    rospy.loginfo("UWU_Bot 	STOP...!")				# Stop uwu_bot, So no linear or angular velocity commands
    rospy.loginfo("")
    pub.publish(twist)

    rospy.loginfo("Shutting Down UWU_Bot Navigation System....!!!")	# At the same time the uwu_bot stopped shutdown the node
    rospy.sleep(2)
    rospy.loginfo("______________________________________________________")
    rospy.loginfo("Copyright (c) 2014, HasithaBR, Uva Wellassa University")
    rospy.loginfo("________________________***___________________________")


if __name__ == '__main__':
    try:
        nav()
    except rospy.ROSInterruptException: pass
