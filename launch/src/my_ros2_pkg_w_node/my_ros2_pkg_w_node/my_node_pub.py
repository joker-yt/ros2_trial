import rclpy
from std_msgs.msg import String

def publisher_node():
    rclpy.init()
    node = rclpy.create_node('publisher_node')
    publisher = node.create_publisher(String, '/my_namespace/my_topic', 10)
    msg = String()
    msg.data = 'Hello, ROS 2!'
    while rclpy.ok():
        publisher.publish(msg)
        node.get_logger().info('Publishing: %s' % msg.data)
        rclpy.spin_once(node)


def main():
    import threading
    thread1 = threading.Thread(target=publisher_node)
    thread1.start()
    thread1.join()

if __name__ == '__main__':
    main()
