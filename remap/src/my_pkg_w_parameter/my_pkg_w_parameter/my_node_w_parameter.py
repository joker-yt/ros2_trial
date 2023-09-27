import rclpy
import time
from std_msgs.msg import String

def main_node():
    rclpy.init()
    node = rclpy.create_node('main_node')
    node.declare_parameter("my_parameter_int", 123)
    node.declare_parameter("my_parameter_string", "abc")

    my_parameter_int = node.get_parameter("my_parameter_int").value
    my_parameter_string = node.get_parameter("my_parameter_string").value
    node.get_logger().info('parameters:: int:{0}'.format(my_parameter_int))
    node.get_logger().info('parameters:: string:{0}'.format (my_parameter_string))

    publisher = node.create_publisher(String, '/default_namespace/default_topic', 10)
    msg = String()
    msg.data = 'default_message'
    time.sleep(2)
    for i in range(1,5):
        publisher.publish(msg)
        node.get_logger().info('Publishing: %s' % msg.data)
    
    rclpy.spin_once(node)

def main():
    import threading
    thread1 = threading.Thread(target=main_node)
    thread1.start()
    thread1.join()

if __name__ == '__main__':
    main()
