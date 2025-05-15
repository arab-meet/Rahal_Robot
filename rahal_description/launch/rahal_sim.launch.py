import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from launch.actions import DeclareLaunchArgument,SetEnvironmentVariable
from pathlib import Path
from launch_ros.actions import Node
from math import radians
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():

    # Setup project paths
    pkg_project_description = get_package_share_directory('rahal_description')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    gz_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=':'.join([
            os.path.join(pkg_project_description,"worlds"),
            str(Path(pkg_project_description).parent.resolve())
        ])
    )

    # Load the SDF file from "description" package
    sdf_file  =  os.path.join(pkg_project_description, 'models', 'robot.sdf')
    with open(sdf_file, 'r') as infp:
        robot_desc = infp.read()

    # Setup to launch the simulator and Gazebo world
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': PathJoinSubstitution([
            pkg_project_description,
            'worlds',
            'turtlebot3_world.sdf'
        ])}.items(),
    )

        
    
    # Takes the description and joint angles as inputs and publishes the 3D poses of the robot links
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[
            {'use_sim_time': True},
            {'robot_description': robot_desc},
        ]  
)
    

    joint_state_publisher_node =  Node(
            package="joint_state_publisher",
            executable="joint_state_publisher",
            parameters=[
            {'use_sim_time': True},]


 )



    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': os.path.join(pkg_project_description, 'config', 'gz_bridge.yaml'),
            'qos_overrides./tf_static.publisher.durability': 'transient_local',
        }],
        output='screen'
    )
  
    spawn_robot_node = Node(
        package='ros_gz_sim',
        executable= 'create',
        arguments= [
            '-name', 'rahal_robot',
            '-topic', 'robot_description',
        ],
        output = 'screen'
    )
    
    
    
    # rviz_node = Node(
    #     package='rviz2',
    #     executable='rviz2',
    #     output='screen',
    #     name='sim_rviz2',
    #     arguments=['-d' + os.path.join(pkg_project_description, 'rviz', 'rahal.rviz')]
    # )
    return LaunchDescription([
        gz_resource_path,
        gz_sim,
        bridge,
        spawn_robot_node,
        robot_state_publisher,
        # rviz_node,
        joint_state_publisher_node,
    
    ])

