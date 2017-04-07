from smbus import SMBus


class PapirusTemperature:

    def __init__(self, i2c_bus=1):
        self.bus = SMBus(i2c_bus)

    def __read_raw(self):
        n = self.bus.read_word_data(0x48, 0x00)
        r = ((((n << 8) & 0xFF00) |
              ((n >> 8) & 0x00FF)) >> 5)
        if r > 2048:  # negative
            r = 2048 - r
        return r

    def read_celsius(self):
        return self.__read_raw() * 0.125

    def read_fahrenheit(self):
        return self.__read_raw() * 0.225 + 32
