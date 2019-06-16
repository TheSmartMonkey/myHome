import json
from datetime import datetime
import time
import threading
from os.path import exists

from smbus import SMBus
import struct


# Address of the Arduino 1 - Adresse de l'Arduino 1
ARDUINO1_I2C_ADDRESS = 18


class BackgroundHistory(object):
    def __init__(self,interval = 10,number_elements = 10):
        self.interval = interval
        self.number_elements = number_elements
        self.elements = []
        self.read()

        thread = threading.Thread(target = self.run)
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            bus = SMBus(1)
            i2c_data1 = bus.read_i2c_block_data(ARDUINO1_I2C_ADDRESS,0)
            humidity, temperature = struct.unpack("ff", struct.pack("B"*8,*i2c_data1[0:8]))
            bus.close()

            data = {"timestamp" : str(datetime.now()),
                    "humidity" : humidity,
                    "temperature" : temperature}

            with open("dataHistory.json","a+") as f:
                f.write(json.dumps(data) + "\n")
            
            self.elements.append(data)

            if len(self.elements) > self.number_elements:
                self.elements.pop(0)

            time.sleep(self.interval)

    def read(self):
        if exists("dataHistory.json"):
            for line in open("dataHistory.json","r"):
                try:
                    data = json.loads(line.strip())
                    self.elements.append(data)
                except:
                    pass

                if len(self.elements) > self.number_elements:
                    self.elements.pop(0)

    def get_elements(self):
        return self.elements