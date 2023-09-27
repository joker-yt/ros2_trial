from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_ros2_pkg_w_node2',
            namespace='/my_namespace2',
            executable='my_node_pub2',
            name='my_launch_test_pub2'
        ),
        Node(
            package='my_ros2_pkg_w_node2',
            namespace='/my_namespace2',
            executable='my_node_sub2',
            name='my_launch_test_sub2'
        ),
    ])
