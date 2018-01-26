
from KeyboardProfileItem import KeyboardProfileItem

class KeyboardKey(object):

    alphabet_key_list = None
    number_key_list = None
    mod_key_list = None
    punctuation_key_list = None
    func_key_list = None
    special_key_list = None
    media_key_list = None

    str_keyboard_keys_dict = None
    int_keyboard_keys_dict = None

    key_label = None
    key_short_label = None
    key_value = None

    def KeyboardKey(self):
        self.str_keyboard_keys_dict['None'] = KeyboardKey("None", "None", 0)

    def KeyboardKey(self,key_label:str, key_short_label:str, key_value:int):
        self.key_label = key_label
        self.key_short_label = key_short_label
        self.key_value = key_value

    def KeyboardKey(self, keyboard_key: type(KeyboardKey)):
        self.key_label = keyboard_key.key_label
        self.key_short_label = keyboard_key.key_short_label
        self.key_value = keyboard_key.key_value

    def init_key_dict(self, keyboard_key_list: type(KeyboardKey)):
        for key in keyboard_key_list:
            if key.key_label not in self.str_keyboard_keys_dict:
                self.str_keyboard_keys_dict[key.key_label] = key
            if key.key_value not in self.int_keyboard_keys_dict:
                self.int_keyboard_keys_dict[key.key_value] = key

    @classmethod
    def init_keyboard_profile(self, profile):
        pass
