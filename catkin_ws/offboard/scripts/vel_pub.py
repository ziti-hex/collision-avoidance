#!/usr/bin/env python

## velocity publisher 

import rospy
from geometry_msgs.msg import Twist as Twist
from geometry_msgs.msg import Vector3 as Vec

def talker_vel():
	pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size=10)
	rospy.init_node('talker_vel', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	
	while not rospy.is_shutdown():
		tw = Twist()
		lin = Vec()
		ang = Vec()
		lin.x = 0
		lin.y = 0
		lin.z = 0
		ang.x = 0
		ang.y = 0
		ang.z = 0
		
		
		tw.linear = lin
		tw.angular = ang
		#tw = [Twist.linear,Twist.angular]
		rospy.loginfo(tw)
		pub.publish(tw)	
		rate.sleep()

if __name__ == '__main__':
    try:
        talker_vel()
    except rospy.ROSInterruptException:
        pass
