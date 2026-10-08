#!/usr/bin/env python3
"""brain_node.py - intelligence of the arm: kinematics, then pick & place.

Never talks to the backend: reads /joint_states, commands through /joint_command.

TODO:
  - Forward kinematics: from /joint_states, publish the TCP pose
    (e.g. /end_effector_pose, geometry_msgs/PoseStamped) and show it in RViz
  - Inverse kinematics: reach an XYZ target (ikpy and pinocchio are installed)
  - Later: pick & place state machine
"""
import rclpy
import rclpy.node
from rclpy.executors import ExternalShutdownException
from sensor_msgs.msg import JointState

ARM_JOINT_NAMES = [
    "shoulder_pan",
    "shoulder_lift",
    "elbow_flex",
    "wrist_flex",
    "wrist_roll",
]
JOINT_NAMES = ARM_JOINT_NAMES + ["gripper"]


class BrainNode(rclpy.node.Node):
    """Brain of the arm: kinematics, then pick & place."""

    def __init__(self):
        super().__init__("so101_brain")

        # TODO: subscribe to /joint_states, publish the TCP pose and /joint_command.

        self.get_logger().info("Brain node ready.")

    def _cb_joint_states(self, msg: JointState):
        raise NotImplementedError("TO DO")

    def _forward_kinematics(self, q):
        raise NotImplementedError("TO DO")

    def _publish_end_effector_pose(self):
        raise NotImplementedError("TO DO")

    def _solve_ik(self, target_position):
        raise NotImplementedError("TO DO")

    def _send_joint_command(self, q, gripper_pct=None):
        raise NotImplementedError("TO DO")


def main(args=None):
    rclpy.init(args=args)
    node = BrainNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
