from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='thomas_nodes',
            executable='publisher',
            name='thomas_publisher'
        ),
        Node(
            package='thomas_nodes',
            executable='subscriber',
            name='thomas_subscriber'
        ),
    ])
