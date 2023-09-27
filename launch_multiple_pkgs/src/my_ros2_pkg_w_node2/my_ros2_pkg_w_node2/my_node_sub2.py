import rclpy
from std_msgs.msg import String

class MySubscriber:
    def __init__(self, node):
        self.node = node
        self.subscription = self.node.create_subscription(
            String,
            '/my_namespace2/my_topic',
            self.callback,
            10
        )

    def callback(self, msg):
        self.node.get_logger().info('Received: %s' % msg.data)

def main():
    rclpy.init()
    node = rclpy.create_node('subscriber_node')
    subscriber = MySubscriber(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
