import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ThomasPublisher(Node):
    def __init__(self):
        super().__init__('thomas_publisher')
        self.publisher = self.create_publisher(String, 'thomas_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.count = 0
        self.get_logger().info('Thomas Publisher Started! 🚀')

    def publish_message(self):
        msg = String()
        msg.data = f'Hello from Thomas! Count: {self.count}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = ThomasPublisher()
    rclpy.spin(node)
    rclpy.shutdown()
