"""Example node: publishes a counter on /chatter at 2 Hz.

Checks that your environment works:
    colcon build && source install/setup.bash
    ros2 run example_py_pkg talker
    # in the other container:
    ros2 topic echo /chatter
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(String, "chatter", 10)
        self.count = 0
        self.create_timer(0.5, self.tick)

    def tick(self):
        msg = String(data=f"tek5 {self.count}")
        self.pub.publish(msg)
        self.count += 1


def main():
    rclpy.init()
    rclpy.spin(Talker())


if __name__ == "__main__":
    main()
