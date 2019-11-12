import subprocess


class RawFanControl:
    backend = 'ipmitool'
    _set_value_prefix  = ['ipmitool', 'raw', '0x30', '0x30', '0x02', '0xFF']

    def set_value(self, value):
        """
        Sets the fan speed value (not necessarily RPM)
        :param value: value between 0 and 255
        """
        hex_value = f'0x{value:02X}'
        subprocess.run(self._set_value_prefix + [hex_value])
