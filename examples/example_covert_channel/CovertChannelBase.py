import string
import time
import random

class CovertChannelBase:
    def __init__(self, log_file_name):
        self.bitwise_message_to_transfer = None
        self.message_to_transfer = None
        self.randomized_dump_message = None
        self.sent_log_file_name = log_file_name + "_sent.log"
        self.received_log_file_name = log_file_name + "_received.log"
    def send(self):
        self.generate_convert_and_store_message()
        self.create_randomized_dump_message()
        with open(self.sent_log_file_name, "a") as my_file:
            my_file.write(self.message_to_transfer)
            my_file.write("\n")
    def receive(self, received_message):
        with open(self.received_log_file_name, "a") as my_file:
            my_file.write(received_message)
            my_file.write("\n")
    def generate_random_string(self, min_length=50, max_length=100):
        letters_digits = string.ascii_letters + string.digits
        punctuation = ',?!'
        all_chars = " " * 50 + letters_digits * 5 + punctuation
        length = random.randint(min_length, max_length)
        random_string = ''.join(random.choice(all_chars) for _ in range(length))
        return random_string + "."
    def generate_convert_and_store_message(self):
        self.message_to_transfer = self.generate_random_string(50, 200)
        self.bitwise_message_to_transfer = ''.join(format(i, '08b') for i in bytearray(self.message_to_transfer, encoding='utf-8'))
    def create_randomized_dump_message(self):
        self.randomized_dump_message = self.generate_random_string(5, 10)
    def sleep_random_time_ms(self, start, end):
        time.sleep(random.uniform(start, end) / 1000)
