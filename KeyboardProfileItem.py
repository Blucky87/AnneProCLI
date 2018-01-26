from KeyboardKey import *
import OBINS


class KeyboardProfileItem(object):
    id = None
    label = None
    keyboard_colors_list = None
    normal_keyboardkey_list = None
    fn_keyboardkey_list = None

    def KeyboardProfileItem(self, id: int, label: str):
        self.id = id
        self.label = label
        self.keyboard_colors_list = list()

        for i in range(0, 70):
            self.keyboard_colors_list.append(b'0xFFFFFF')

        KeyboardKey.init_keyboard_profile(self)


    def validate_keyboard_keys(self):
        norm_important_keys = self.special_key_exists(self.normal_keyboardkey_list)
        fn_important_keys = self.special_key_exists(self.fn_keyboardkey_list)

        return norm_important_keys and fn_important_keys

    def special_key_exists(self, keyboardkey_list):
        anne_key = False
        fn_key = False

        for key in keyboardkey_list:
            if key.key_value == 250:
                anne_key = True
            if key.key_value == 254:
                fn_key = True

        return anne_key and fn_key

    def generate_keyboard_backlight_data(self):
        bluetooth_data = bytearray()
        for i in range(0, 70):
            if i not in [40, 53, 54, 59, 60, 62, 63, 64, 65]:
                color = self.keyboard_colors_list[i]
                green = bytes((65280 & color) >> 8)
                blue = bytes(255 & color)
                bluetooth_data[((i * 3) + 4) + 2] = green
                bluetooth_data[((i * 3) + 4) + 2] = blue

        checksum = OBINS.CRC16.calculate_checksum(bluetooth_data, 4, 210)
        checksum_data = bytearray(checksum)
        flipped_checksum_data = checksum_data[-1:]
        bluetooth_data.