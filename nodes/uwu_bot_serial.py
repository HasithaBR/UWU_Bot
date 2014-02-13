#!/usr/bin/env python

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                        //
//     Copyright (c) 2011, Willow Garage, Inc.				                                                  //
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
//      * Neither the name of Willow Garage, Inc.,Uva Wellassa University nor the names of its contributors may be used   //
//	  to endorse or promote products derived from this software without specific prior writtenpermission.             //
//                                                                                                                        //
//     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, //
//     INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE  //
//     DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,  //
//     SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    //
//     SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,  //
//     WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE   //
//     USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                           //
//                    __author__ = "mferguson@willowgarage.com (Michael Ferguson)"                                        //
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''


import rospy
from rosserial_python import SerialClient
import multiprocessing

import sys
   
if __name__=="__main__":

    rospy.init_node("uwu_bot_serial")
    rospy.loginfo("______________________________________________________")
    rospy.loginfo("		   UWU_Bot Initiallizing	         ")
    rospy.loginfo("______________________________________________________")
    rospy.loginfo("")
    port_name = rospy.get_param('~port','/dev/ttyUSB0')
    baud = int(rospy.get_param('~baud','57600'))
    rospy.loginfo("Connecting to UWU_Bot on port %s at %d" % (port_name,baud) )
    client = SerialClient(port_name, baud)
    rospy.loginfo("______________________________________________________")
    try:
        client.run()
    except KeyboardInterrupt:
        pass

