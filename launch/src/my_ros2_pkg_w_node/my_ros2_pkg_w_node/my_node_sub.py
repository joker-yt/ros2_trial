import rclpy
from std_msgs.msg import String


def subscriber_node():
    rclpy.init()
    node = rclpy.create_node('subscriber_node')
    subscriber = node.create_subscription(String, '/my_namespace/my_topic', callback, 10)
    rclpy.spin(node)

def callback(msg):
    print('Received: %s' % msg.data)

def main():
    import threading
    thread2 = threading.Thread(target=subscriber_node)
    thread2.start()
    thread2.join()

if __name__ == '__main__':
    main()
