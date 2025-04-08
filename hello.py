import rclpy
from rclpy.node import Node

class HelloWorldNode(Node):
    def __init__(self):
        super().__init__('hello_world_node')
        self._counter = 0
        self._timer = self.create_timer(1.0, self._tick)
        self.get_logger().info('Started hello_world_node')

    def _tick(self):
        self._counter += 1
        self.get_logger().info(f'[{self._counter}] Hello from the node')

def main(args=None):
    rclpy.init(args=args)
    node = HelloWorldNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
