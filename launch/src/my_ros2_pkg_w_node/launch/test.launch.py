from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_ros2_pkg_w_node',
            namespace='',
            executable='my_node_sub',
            name='my_launch_test_sub'
        ),
        Node(
            package='my_ros2_pkg_w_node',
            namespace='',
            executable='my_node_pub',
            name='my_launch_test_pub'
        )
    ])
