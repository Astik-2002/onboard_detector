#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

def dummy_pose_publisher():
    rospy.init_node("dummy_pose_publisher", anonymous=True)
    pub = rospy.Publisher("/mavros/local_position/pose", PoseStamped, queue_size=10)

    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        pose = PoseStamped()
        pose.header.stamp = rospy.Time.now()
        pose.header.frame_id = "map"   # or "odom", depending on your setup

        # Zero pose
        pose.pose.position.x = 0.0
        pose.pose.position.y = 0.0
        pose.pose.position.z = 0.0
        pose.pose.orientation.x = 0.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = 0.0
        pose.pose.orientation.w = 1.0  # valid quaternion

        pub.publish(pose)
        rate.sleep()

if __name__ == "__main__":
    try:
        dummy_pose_publisher()
    except rospy.ROSInterruptException:
        pass
