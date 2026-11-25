# Sourced by pixi on activation (pixi run / pixi shell). Do not run directly.

# Overlay of your workspace, once built (pixi run build).
if [ -f "$PIXI_PROJECT_ROOT/ros2_ws/install/setup.bash" ]; then
  # shellcheck disable=SC1091
  source "$PIXI_PROJECT_ROOT/ros2_ws/install/setup.bash"
fi

# ROS 2 discovery limited to this machine.
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
