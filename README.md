# simple_palbator_arm


## Dépendance

Install UR arm

```bash
# source global ros
source /opt/ros/<your_ros_version>/setup.bash

# create a catkin workspace
mkdir -p catkin_ws/src && cd catkin_ws

# clone the driver
git clone https://github.com/UniversalRobots/Universal_Robots_ROS_Driver.git src/Universal_Robots_ROS_Driver

# clone the description. Currently, it is necessary to use the melodic-devel branch.
git clone -b melodic-devel https://github.com/ros-industrial/universal_robot.git src/universal_robot

# install dependencies
sudo apt update -qq
rosdep update
rosdep install --from-paths src --ignore-src -y

# build the workspace
catkin_make

# activate the workspace (ie: source it)
source devel/setup.bash
```


## Lancement

- **Une fois pour toute**
  - `Installation` --> `URCaps` --> `External Control` 
    - Mettre l'IP du PC de commande


- **Launch Arm driver** 
  - Communication Interface (UR Tablet), click below on "Play" and execute the external_control program
    ```bash
    roslaunch ur_robot_driver ur5e_bringup.launch robot_ip:=10.68.0.101 use_tool_communication:=true tool_voltage:=24 tool_parity:=0 tool_baud_rate:=115200 tool_stop_bits:=1 tool_rx_idle_chars:=1.5 tool_tx_idle_chars:=3.5 tool_device_name:=/tmp/ttyUR
    ```
  - Communication Interface (UR Tablet), click below on "Play" and execute the external_control program

- **Arm service** 
```bash
rosrun simple_palbator_arm native_mvt.py
```

- **Call the service** 
```bash
rosservice call /point_front "{}"
```

- **Pour se lancer depuis un code python, importez ce srv standard**
```python
from std_srvs.srv import Trigger
```


## DOCKER

### Build the Dockerfile
```bash
cd simple_palbator_arm
docker build -t test .
```

### Run the docker image
```bash
docker run -it -p 54321:54321 -p 50001:50001 -p 50002:50002 -p 50003:50003 -p 50004:50004 test
```

### Commands in temrinal

1. 
```bash
cd /catkin_ws
source devel/setup.bash
rosrun robotiq_2f_gripper_control Robotiq2FGripperRtuNode.py /tmp/ttyUR
```

2.
```bash
cd /catkin_ws
source devel/setup.bash
roslaunch robotiq_2f_gripper_action_server robotiq_2f_gripper_action_server.launch
```

3.
```bash
cd /catkin_ws
source devel/setup.bash
rosrun robotiq_2f_gripper_control Robotiq2FGripperSimpleController.py 
```