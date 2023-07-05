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

- 
```bash
rosrun simple_palbator_arm native_mvt.py
```

- Call the service 
```bash
rosservice call /point_front "{}"
```

- Pour se lancer depuis un code python, importez ce srv standard
```python
from std_srvs.srv import Trigger
```