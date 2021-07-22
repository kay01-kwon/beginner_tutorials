#! /usr/bin/env python
import rospy
from beginner_tutorials.msg import Num


class MySubscriber(object):
    def __init__(self):
        self.data1 = 0
        self.data2 = 0
        self.subscriber1 = rospy.Subscriber("chatter1", Num, self.callback)
        self.subscriber2 = rospy.Subscriber("chatter2", Num, self.callback2)

    def callback(self, msg1):
        self.data1 = msg1.num
        rospy.loginfo("%d", self.data1 + self.data2)

    def callback2(self, msg2):
        self.data2 = msg2.num


if __name__ == '__main__':
    rospy.init_node("listener", anonymous=True)
    MySub = MySubscriber()
    rospy.spin()
