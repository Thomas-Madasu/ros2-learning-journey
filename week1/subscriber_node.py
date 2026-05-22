import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ThomasSubscriber(Node):
    def __init__(self):
        super().__init__('thomas_subscriber')
        self.subscription = self.create_subscription(
            String, 'thomas_topic', self.listener_callback, 10)
        self.get_logger().info('Thomas Subscriber Started! 👂')

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ThomasSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
