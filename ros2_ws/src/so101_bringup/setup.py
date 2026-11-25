from glob import glob

from setuptools import setup

package_name = "so101_bringup"

setup(
    name=package_name,
    version="0.2.0",
    packages=[],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/launch", glob("launch/*.launch.py")),
    ],
    zip_safe=True,
    description="Launches the whole SO-ARM101 stack.",
    license="Apache-2.0",
)
