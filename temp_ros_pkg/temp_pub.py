import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        # Publisher létrehozása a /temperature topic-ra, Float64 üzenettípussal
        self.publisher_ = self.create_publisher(Float64, 'temperature', 10)
        timer_period = 1.0  # másodpercenkénti publikálás
        # Időzítő létrehozása a publikáláshoz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Temperature Publisher Node started.')

    def timer_callback(self):
        # Véletlenszerű hőmérséklet generálása (pl. 20.0 és 35.0 C fok között)
        temperature = random.uniform(20.0, 35.0)
        msg = Float64()
        msg.data = temperature
        # Publikálás a topic-ra
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data:.2f} °C"')

def main(args=None):
    rclpy.init(args=args)
    temperature_publisher = TemperaturePublisher()
    rclpy.spin(temperature_publisher)
    temperature_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()