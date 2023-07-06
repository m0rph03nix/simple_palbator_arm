# Utilisation de l'image de base ROS Melodic
FROM ros:melodic-ros-base

# Installation des dépendances système pour le paquet ROS
RUN apt-get update && apt-get install -y \
    ros-melodic-ros-controllers \
    ros-melodic-moveit \
    ros-melodic-robot-state-publisher \
    ros-melodic-trac-ik-kinematics-plugin \
    ros-melodic-tf-conversions \
    ros-melodic-pass-through-controllers \ 
    ros-melodic-speed-scaling-state-controller \
    ros-melodic-scaled-joint-trajectory-controller \
    ros-melodic-warehouse-ros-mongo \
    ros-melodic-ur-client-library \
    ros-melodic-ur-msgs \
    ros-melodic-joint-state-publisher-gui \
    ros-melodic-gazebo-ros-control \
    ros-melodic-industrial-robot-status-interface \
    ros-melodic-industrial-robot-status-controller \
    ros-melodic-twist-controller \ 
    ros-melodic-cartesian-trajectory-controller
    # Ajoutez ici d'autres dépendances système si nécessaire \
    
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /catkin_ws/src

# Création du répertoire de travail
WORKDIR /catkin_ws

RUN apt-get update 

RUN apt-get install -y python-pip && pip install --upgrade setuptools pip

# Installation des dépendances Python
COPY simple_palbator_arm /catkin_ws/src/simple_palbator_arm

# Configuration de l'environnement ROS
RUN echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

# create a catkin workspace
RUN . /opt/ros/${ROS_DISTRO}/setup.sh \ 
    && cd /catkin_ws/ \
    && git clone https://github.com/UniversalRobots/Universal_Robots_ROS_Driver.git src/Universal_Robots_ROS_Driver \
    && git clone -b melodic-devel https://github.com/ros-industrial/universal_robot.git src/universal_robot \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src -y


# Construction du paquet ROS
RUN /bin/bash -c "source /opt/ros/melodic/setup.bash && catkin_make && source devel/setup.bash && roscore"

# Exécution du nœud ROS spécifique
CMD ["/bin/bash", "-c", "source /catkin_ws/devel/setup.bash && roslaunch urdf_tutorial display.launch model:=$(find pmb2_description)/robots/pmb2_custom.urdf.xacro"]