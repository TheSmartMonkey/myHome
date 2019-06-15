from smbus import SMBus
import struct


# Address of the Arduino 1 - Adresse de l'Arduino 1
ARDUINO1_I2C_ADDRESS = 18


def get_humidity_temperature():
    """
    Get the humidity and the tempetature by calling the arduino by I2C
    """

    bus = SMBus(1)
    data = bus.read_i2c_block_data(ARDUINO1_I2C_ADDRESS,0)
    humidity, temperature = struct.unpack("ff", struct.pack("B"*8, *data[0:8]))
    return humidity, temperature


humidity, temperature = get_humidity_temperature()
print("Temperature: %4.2f° Humidity: %4.2f%%\n" % (temperature, humidity))
