from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_ros2_pkg_w_node1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('launch/*.launch.xml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tk',
    maintainer_email='jokerxx1344xxyt@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node_pub1 = my_ros2_pkg_w_node1.my_node_pub1:main',
            'my_node_sub1 = my_ros2_pkg_w_node1.my_node_sub1:main'
        ],
    },
)
