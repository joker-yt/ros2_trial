import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from std_msgs.msg import Empty
import threading

class MainNode(Node):
    def __init__(self):
        super().__init__('main_node')
        self.declare_parameter("my_parameter_int", 123)
        self.declare_parameter("my_parameter_string", "abc")
        
        # Set up a timer to periodically check and log parameter values
        self.create_timer(2, self.timer_callback)

        # Subscribe to a shutdown topic
        self.shutdown_subscription = self.create_subscription(
            Empty,
            'shutdown',
            self.shutdown_callback,
            10)
        
        self.get_logger().info("Node started. Publish to /shutdown topic to stop the node.")
        
        # Flag to indicate if the node should continue running
        self.running = True

    def timer_callback(self):
        my_parameter_int = self.get_parameter("my_parameter_int").value
        my_parameter_string = self.get_parameter("my_parameter_string").value
        
        self.get_logger().info(f'parameters:: int:{my_parameter_int}')
        self.get_logger().info(f'parameters:: string:{my_parameter_string}')

    def shutdown_callback(self, msg):
        self.get_logger().info("Shutdown message received. Stopping the node...")
        self.running = False

def main():
    rclpy.init()
    node = MainNode()
    
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    # Use a separate thread for spinning
    spin_thread = threading.Thread(target=executor.spin, daemon=True)
    spin_thread.start()
    
    try:
        while node.running:
            pass
    finally:
        node.get_logger().info("Shutting down...")
        executor.shutdown()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()