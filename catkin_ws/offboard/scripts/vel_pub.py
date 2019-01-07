#!/usr/bin/env python

## velocity publisher 

import rospy
from geometry_msgs.msg import Twist as Twist
from geometry_msgs.msg import Vector3 as Vec

def talker_vel():
	pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size=10)
	rospy.init_node('talker_vel', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	tw = Twist()
	lin = Vec()
	ang = Vec()
	i=0
	while not rospy.is_shutdown():
		i = i+1
		lin.x = i
		lin.y = i
		lin.z = i
		ang.x = i
		ang.y = i
		ang.z = i
		
		
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
