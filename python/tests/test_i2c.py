import smbus
import time
import sys


# Replace 0 with 1 if new Raspberry - Remplacer 0 par 1 si nouveau Raspberry
bus = smbus.SMBus(1)
address = int(sys.argv[1])
value = int(sys.argv[2])
print("Envoi de la valeur %d" % value)
bus.write_byte(address, value)

# 1 second break to allow time for processing to take place - Pause de 1 seconde pour laisser le temps au traitement de se faire
time.sleep(1)
reponse = bus.read_byte(address)
print("La reponse de l'arduino : ", reponse)