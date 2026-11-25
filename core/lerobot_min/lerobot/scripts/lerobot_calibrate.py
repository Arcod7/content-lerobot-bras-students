# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Calibrates the SO-ARM101. LeRobot v0.7.0 lerobot-calibrate, robots only
(no teleoperator nor RealSense in this extract).

Example:

```shell
lerobot-calibrate \
    --robot.type=so101_follower \
    --robot.port=/dev/ttyACM0 \
    --robot.id=my_arm
```
"""

import logging
from dataclasses import asdict, dataclass
from pprint import pformat

import draccus

from lerobot.robots import RobotConfig
from lerobot.robots.so_follower import SOFollower
from lerobot.utils.utils import init_logging


@dataclass
class CalibrateConfig:
    robot: RobotConfig


@draccus.wrap()
def calibrate(cfg: CalibrateConfig) -> None:
    init_logging()
    logging.info(pformat(asdict(cfg)))

    robot = SOFollower(cfg.robot)
    robot.connect(calibrate=False)

    try:
        robot.calibrate()
    finally:
        robot.disconnect()


def main():
    calibrate()


if __name__ == "__main__":
    main()
