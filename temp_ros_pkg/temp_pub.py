import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_ = self.create_publisher(Float64, 'temperature', 10)
        timer_period = 1.0  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Temperature Publisher Node elkezdődöt.')

    def timer_callback(self):
        temperature = random.uniform(20.0,35.0)
        msg = Float64()
        msg.data = temperature
        self.publisher_.publish(msg)
        self.get_logger().info(f'Hőmérséklet: "{msg.data:.2f}"')

def main(args=None):
    rclpy.init(args=args)
    temperature_publisher = TemperaturePublisher()
    rclpy.spin(temperature_publisher)
    temperature_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()