import socket
import time
from CovertChannelBase import CovertChannelBase

class MyCovertTimingChannelSenderUDP(CovertChannelBase):
    def __init__(self, threshold_ms, error_ms):
        super().__init__("covert_timing_channel_message")
        self.time_difference_0_lower_limit_ms = 0
        self.time_difference_0_upper_limit_ms = threshold_ms - error_ms
        self.time_difference_1_lower_limit_ms = threshold_ms + error_ms
        self.time_difference_1_upper_limit_ms = 2 * threshold_ms
        self.receiver_ip = "receiver"
        self.receiver_port = 12000
    def send(self):
        super().send()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(self.randomized_dump_message.encode(), (self.receiver_ip, self.receiver_port))
            for message_bit in self.bitwise_message_to_transfer:
                if message_bit == '0':
                    self.sleep_random_time_ms(self.time_difference_0_lower_limit_ms, self.time_difference_0_upper_limit_ms)
                elif message_bit == '1':
                    self.sleep_random_time_ms(self.time_difference_1_lower_limit_ms, self.time_difference_1_upper_limit_ms)
                self.create_randomized_dump_message()
                sock.sendto(self.randomized_dump_message.encode(), (self.receiver_ip, self.receiver_port))

# Uncomment the following lines to run the Covert Channel Sender

# myCovertTimingChannelSenderUDP = MyCovertTimingChannelSenderUDP(10, 5)
# myCovertTimingChannelSenderUDP.send()