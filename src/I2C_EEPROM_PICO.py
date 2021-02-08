from machine import I2C, Pin
import utime
class EEPROM:
    def __init__(self, channel: int, scl: Pin, sda: Pin, addr: int, typeofIC: int):
        """
        channel: channel of I2C (0 or 1), scl pin, sda pin\n
        addr: I2C address of IC 24CXX\n
        typeofIC: type of IC, ex, IC 24C04 -> type = 4
        """
        self.i2c = I2C(channel, scl=scl, sda=sda, freq=400000)
        self.addr = addr
        self.maxAddr = typeofIC*128
        self.timeSleep = 5

    def clean(self):
        """
        write full address to 0
        """
        for i in range(self.maxAddr):
            self.i2c.writeto_mem(self.addr, i, bytes([0]))
            utime.sleep_ms(self.timeSleep)

    def num2byte(self, nbyte: int, value):
        arraybyte = []
        for i in reversed(range(nbyte)):
            arraybyte.append( (value >> 8*i) & 0xFF )
        return bytearray(arraybyte)


    def read_1_byte(self, addr: int):
        """
        read 1byte at 'addr'\n
        0 - 255
        """
        return ord(self.i2c.readfrom_mem(self.addr, addr, 1))


    def read_2_byte(self, addr: int):
        """
        read 2byte from 'addr'\n
        0 - 65_535
        """
        ret = self.i2c.readfrom_mem(self.addr, addr, 2)
        return  int.from_bytes(ret, 'big')


    def read_4_byte(self, addr: int):
        """
        read 4byte from 'addr'\n
        0 - 4_294_967_295
        """
        ret = self.i2c.readfrom_mem(self.addr, addr, 4)
        return  int.from_bytes(ret, 'big')


    def read_n_byte(self, addr: int, nbyte: int):
        """
        read 'nbyte' from 'addr'
        """
        ret = self.i2c.readfrom_mem(self.addr, addr, nbyte)
        return  int.from_bytes(ret, 'big')


    def write_1_byte(self, addr: int, value):
        """
        write 1byte 'value' at 'addr'\n
        0 - 255
        """
        self.i2c.writeto_mem(self.addr, addr, bytes([value]))
        utime.sleep_ms(self.timeSleep)


    def write_2_byte(self, addr: int, value):
        """
        write 2byte 'value' at 'addr'\n
        0 - 65_535
        """
        byteArray = self.num2byte(2, value)
        self.i2c.writeto_mem(self.addr, addr, byteArray)
        utime.sleep_ms(self.timeSleep)


    def write_4_byte(self, addr: int, value):
        """
        write 4byte 'value' at 'addr'\n
        0 - 4_294_967_295
        """
        byteArray = self.num2byte(4, value)
        self.i2c.writeto_mem(self.addr, addr, byteArray)
        utime.sleep_ms(self.timeSleep)


    def write_n_byte(self, addr: int, nbyte: int, value):
        """
        write 'nbyte' 'value' at 'addr'
        """
        byteArray = self.num2byte(nbyte, value)
        self.i2c.writeto_mem(self.addr, addr, byteArray)
        utime.sleep_ms(self.timeSleep)

