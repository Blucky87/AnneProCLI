from KeyboardKey import *
import OBINS


class KeyboardProfileItem(object):
    id = None
    label = None
    keyboard_colors_list = None
    normal_keyboardkey_list = list()
    fn_keyboardkey_list = None

    def KeyboardProfileItem(self, id: int, label: str):
        self.id = id
        self.label = label
        self.keyboard_colors_list = bytearray()

        for i in range(0, 70):
            self.keyboard_colors_list.append(0xFFFFFF)

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
        self.unknown()
        for i in range(0, 70):
            if i not in [40, 53, 54, 59, 60, 62, 63, 64, 65]:
                color = self.keyboard_colors_list[i]
                green = bytes((65280 & color) >> 8)
                blue = bytes(255 & color)
                bluetooth_data[((i * 3) + 4) + 2] = green
                bluetooth_data[((i * 3) + 4) + 2] = blue

        checksum = OBINS.CRC16.calculate_checksum(bluetooth_data, 4, 210)
        checksum_data = bytearray(checksum)
        self.unknown()
        flipped_checksum_data = checksum_data[-1:]
        # copy the checksum data into the bluetooth data, overwriting len(checksum_data)
        return bluetooth_data

    def generate_keyboard_layout_data(self):
        # array of bytes length 144
        bluetooth_data = bytearray()

        # get all values of the keys as byte
        standard_keys = list(map((lambda key: bytes(key.key_value), self.normal_keyboardkey_list)))
        fn_keys = list(map((lambda key: bytes(key.key_value)), self.fn_keyboardkey_list))

        # arrays of bytes length 70
        standard_converted_keys = bytearray()
        fn_converted_keys = bytearray()

        j = 0
        for i in range(70):
            if i not in [40, 53, 54, 59, 60, 62, 63, 64, 65]:
                standard_converted_keys[i] = standard_keys[j]
                fn_converted_keys[i] = fn_keys[j]
                j += 1

        # KeyboardProfile Item line 160
        self.unknown()

        checksum = OBINS.CRC16.calculate_checksum(bluetooth_data)

        if checksum < 10:
            checksum += 10

        # line 168, array of bytes
        checksum_data = self.unknown()

        # reverse array


        # copy checksum data into bluetooth data,of length checksum list


        return bluetooth_data

    def sync_profile(self, gatt):
        self.sync_profile_phase1(gatt)

    def sync_profile_phase_1(self, gatt):
        lighting_meta_data = bytes([0x09, 0xD7, 0x03])
        light_data = self.generate_keyboard_backlight_data()

        ######## KEYBOARD WRITER line 190+


    def sync_profile_phase_2(self, gatt):
        if not self.validate_keyboard_keys():
            return
        layout_meta_data = [0x7, 0x91, 0x02]
        layout_data = self.generate_keyboard_layout_data()

        ######## Keyboard Writer line 212



    def unknown(self):
        print("OH NO")
