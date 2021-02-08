from machine import Pin
import I2C_EEPROM_PICO

eeprom = I2C_EEPROM_PICO.EEPROM(channel=1, scl=Pin(15), sda=Pin(14), addr=0x50, typeofIC=4)

# clean all data
# eeprom.clean()


eeprom.write_1_byte(0, 255)
resutl = eeprom.read_1_byte(0)

# eeprom.write_2_byte(0, 65_535)
# resutl = eeprom.read_2_byte(0)


# eeprom.write_4_byte(0, 4_294_967_295)
# resutl = eeprom.read_4_byte(0)


# nbyte = 10
# eeprom.write_n_byte(0, nbyte, 199999999999999999999999)
# resutl = eeprom.read_n_byte(0, nbyte)

print(resutl)
