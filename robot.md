<p align="center">
<img src="images/rahal_robot.png">



- **2D Lidar (A2 RPLIDAR)**: Provides 360-degree distance measurements to create a 2D map of the robot’s surroundings, essential for obstacle detection and mapping.
- **Camera (RealSense D435)**: Captures depth and color images for advanced perception tasks, including object recognition and spatial understanding.
- **IMU (MPU 6050)**: Measures acceleration and angular velocity to provide orientation and movement data, crucial for stabilization and navigation.
- **Ultrasonic Sensor (HC-SR04)**: Uses sound waves to measure distance to nearby objects, useful for collision avoidance and distance sensing.
- **GPS (NEO-6)**: Provides location data by connecting to global satellite networks, enabling accurate position tracking and navigation.

# Steps to Set Up and Run the Robot

## 1. Create and Build the Workspace

Create your ROS workspace and clone the robot package:

```sh
mkdir -p  catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
git clone https://github.com/arab-meet/Rahal_Robot.git
cd ..
catkin_make
```

## 2. Display Our Logo on the Robot

To display our logo on the robot in Gazebo, follow these steps:

1. Navigate to the directory where the relevant texture files are located:

   ```bash
   cd src/rahal_description_pkg/textures
   ```

2. Copy the [`white_material.material`](/rahal_description_pkg//textures/white_material.material) file to Gazebo’s materials scripts directory by running the following command:

   ```bash
   cp white_material.material /usr/share/gazebo-11/media/materials/scripts/
   ```

   > **Note:** If you encounter a `Permission denied` error, use `sudo` to grant the necessary permissions:

   ```bash
   sudo cp white_material.material /usr/share/gazebo-11/media/materials/scripts/
   ```

3. Copy the [`logo.material`](/rahal_description_pkg//textures/logo.material) file to Gazebo’s materials scripts directory:

   ```bash
   sudo cp logo.material /usr/share/gazebo-11/media/materials/scripts/
   ```

4. Copy the [`logo.png`](/rahal_description_pkg//textures/logo.png) image to Gazebo’s materials textures directory:

   ```bash
   sudo cp logo.png /usr/share/gazebo-11/media/
   ```

Following these steps will integrate the logo and ensure it appears on the robot in the Gazebo simulation.

## 3. Running Both Gazebo and RViz Together

to launch both the Gazebo simulation and the RViz visualization simultaneously, use this:

```sh
roslaunch rahal_description_pkg rahal_gazebo.launch
```

<p align="center">
<img src="images/rahal.gif">
