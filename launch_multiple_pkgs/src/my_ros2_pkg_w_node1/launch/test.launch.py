from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_ros2_pkg_w_node1',
            namespace='/my_namespace',
            executable='my_node_pub1',
            name='my_launch_test_pub1'
        ),
        Node(
            package='my_ros2_pkg_w_node1',
            namespace='/my_namespace',
            executable='my_node_sub1',
            name='my_launch_test_sub1'
        ),
    ])
