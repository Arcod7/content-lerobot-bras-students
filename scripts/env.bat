@echo off
rem Windows counterpart of env.sh, run by pixi on activation. Do not run directly.

rem Overlay of your workspace, once built (pixi run build).
if exist "%PIXI_PROJECT_ROOT%\ros2_ws\install\setup.bat" call "%PIXI_PROJECT_ROOT%\ros2_ws\install\setup.bat"

rem ROS 2 discovery limited to this machine.
set "ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST"
rem Cyclone DDS on Windows otherwise picks a virtual adapter (Hyper-V, VPN) and finds nobody.
set "CYCLONEDDS_URI=<CycloneDDS><Domain id="any"><General><Interfaces><NetworkInterface address="127.0.0.1" multicast="true"/></Interfaces><AllowMulticast>true</AllowMulticast></General></Domain></CycloneDDS>"
