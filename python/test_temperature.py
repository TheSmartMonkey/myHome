from smbus import SMBus
import struct

def get_humidity_temperature():
    "get the humidity and the tempetature by calling the arduino by I2C"
    bus=SMBus(1)
    data=bus.read_i2c_block_data(18,0)
    humidity,temperature=struct.unpack("ff",struct.pack("B"*8,*data[0:8]))
    return humidity,temperature

humidity,temperature=get_humidity_temperature()
print("Temperature: %4.2f° Humidity: %4.2f%%\n"%(temperature,humidity))

