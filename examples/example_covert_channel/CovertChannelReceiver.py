import socket
import time
from CovertChannelBase import CovertChannelBase

class MyCovertTimingChannelReceiverUDP(CovertChannelBase):
    def __init__(self, threshold_ms):
        super().__init__("covert_timing_channel_message")
        self.time_difference_0_lower_limit_ms = 0
        self.time_difference_0_upper_limit_ms = threshold_ms
        self.time_difference_1_lower_limit_ms = threshold_ms
        self.time_difference_1_upper_limit_ms = 3 * threshold_ms
        self.ip = "receiver"
        self.port = 12000
    def receive(self):
        print("Here1")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind((self.ip, self.port))
            while True:
                received_string = ""
                final_string = ""
                _, _ = sock.recvfrom(1024)
                print("Here2")
                data_time_1 = time.time()
                while True:
                    _, _ = sock.recvfrom(1024)
                    data_time_2 = time.time()
                    if self.time_difference_0_lower_limit_ms < ((data_time_2 - data_time_1) * 1000) < self.time_difference_0_upper_limit_ms:
                        received_string += "0"
                    elif self.time_difference_1_lower_limit_ms < ((data_time_2 - data_time_1) * 1000) < self.time_difference_1_upper_limit_ms:
                        received_string += "1"
                    if len(received_string) == 8:
                        converted_character = chr(int(received_string, 2))
                        if converted_character == ".":
                            super().receive(final_string)
                            final_string = ""
                            break
                        else:
                            final_string += converted_character
                        received_string = ""
                    data_time_1 = data_time_2

# Uncomment the following lines to run the Covert Channel Receiver

# myCovertTimingChannelReceiverUDP = MyCovertTimingChannelReceiverUDP(10)
# myCovertTimingChannelReceiverUDP.receive()