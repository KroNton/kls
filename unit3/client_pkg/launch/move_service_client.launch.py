
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='client_pkg',
            executable='move_client_node',
            output='screen'),
    ])