import subprocess


class RawFanControl:
    backend = 'ipmitool'
    _set_manual_prefix = ['ipmitool', 'raw', '0x30', '0x30', '0x01']
    _set_value_prefix  = ['ipmitool', 'raw', '0x30', '0x30', '0x02', '0xFF']

    def set_manual(self, enabled):
        hex_value = '0x00' if enabled else '0x01'
        subprocess.run(self._set_manual_prefix + [hex_value])

    def set_value(self, value):
        """
        Sets the fan speed value (not necessarily RPM)
        :param value: value between 0 and 255
        """
        hex_value = f'0x{value:02X}'
        subprocess.run(self._set_value_prefix + [hex_value])
