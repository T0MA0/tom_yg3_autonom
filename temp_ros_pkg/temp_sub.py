import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float64

class TemperatureSubscriber(Node):
    def __init__(self):
        super().__init__('temperature_subscriber')
        self.subscription = self.create_subscription(Float64, 'temperature',self.listener_callback,10)
        self.subscription

        self.normal_min = 22.0
        self.normal_max = 28.0
        self.get_logger().info('Temperature Subscriber Node elkezdődöt. Normális tartomany: 22.0 - 28.0 °C')


    def listener_callback(self,mgs):
        temperature = msg.data
        self.get_logger().info(f'Kapot hőmérséklet: {temperature:.2f} °C.')


def main(args=None):
    rclpy.init(args=args)
    temperature_subscriber = TemperatureSubscriber()
    rclpy.spin(temperature_subscriber)
    temperature_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()