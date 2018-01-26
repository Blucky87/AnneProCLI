
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
        # Empty key
        self.str_keyboard_keys_dict['None'] = KeyboardKey("None", "None", 0)
        self.int_keyboard_keys_dict[0] = self.str_keyboard_keys_dict['None']

        # Anne Key
        self.str_keyboard_keys_dict['Anne'] = KeyboardKey("Anne", "Anne", 250)
        self.int_keyboard_keys_dict[250] = self.str_keyboard_keys_dict['Anne']

        # Fn Key
        self.str_keyboard_keys_dict['Fn'] = KeyboardKey("Fn", "Fn", 254)
        self.int_keyboard_keys_dict[254] = self.str_keyboard_keys_dict['Fn']

        #Windows Lock Key TODO

        # Keys for Alpha (a - Z)

        self.alphabet_key_list = []

        self.alphabet_key_list.append(KeyboardKey("A", "A", 4))
        self.alphabet_key_list.append(KeyboardKey("B", "B", 5))
        self.alphabet_key_list.append(KeyboardKey("C", "C", 6))
        self.alphabet_key_list.append(KeyboardKey("D", "D", 7))
        self.alphabet_key_list.append(KeyboardKey("E", "E", 8))
        self.alphabet_key_list.append(KeyboardKey("F", "F", 9))
        self.alphabet_key_list.append(KeyboardKey("G", "G", 10))
        self.alphabet_key_list.append(KeyboardKey("H", "H", 11))
        self.alphabet_key_list.append(KeyboardKey("I", "I", 12))
        self.alphabet_key_list.append(KeyboardKey("J", "J", 13))
        self.alphabet_key_list.append(KeyboardKey("K", "K", 14))
        self.alphabet_key_list.append(KeyboardKey("L", "L", 15))
        self.alphabet_key_list.append(KeyboardKey("M", "M", 16))
        self.alphabet_key_list.append(KeyboardKey("N", "N", 17))
        self.alphabet_key_list.append(KeyboardKey("O", "O", 18))
        self.alphabet_key_list.append(KeyboardKey("P", "P", 19))
        self.alphabet_key_list.append(KeyboardKey("Q", "Q", 20))
        self.alphabet_key_list.append(KeyboardKey("R", "R", 21))
        self.alphabet_key_list.append(KeyboardKey("S", "S", 22))
        self.alphabet_key_list.append(KeyboardKey("T", "T", 23))
        self.alphabet_key_list.append(KeyboardKey("U", "U", 24))
        self.alphabet_key_list.append(KeyboardKey("V", "V", 25))
        self.alphabet_key_list.append(KeyboardKey("W", "W", 26))
        self.alphabet_key_list.append(KeyboardKey("X", "X", 27))
        self.alphabet_key_list.append(KeyboardKey("Y", "Y", 28))
        self.alphabet_key_list.append(KeyboardKey("Z", "Z", 29))

        self.init_key_dict(self.alphabet_key_list)

        # number pad keys
        self.number_key_list.append(KeyboardKey("0", "0", 39))
        self.number_key_list.append(KeyboardKey("1", "1", 30))
        self.number_key_list.append(KeyboardKey("2", "2", 31))
        self.number_key_list.append(KeyboardKey("3", "3", 32))
        self.number_key_list.append(KeyboardKey("4", "4", 33))
        self.number_key_list.append(KeyboardKey("5", "5", 34))
        self.number_key_list.append(KeyboardKey("6", "6", 35))
        self.number_key_list.append(KeyboardKey("7", "7", 36))
        self.number_key_list.append(KeyboardKey("8", "8", 37))
        self.number_key_list.append(KeyboardKey("9", "9", 38))

        self.init_key_dict(self.number_key_list)

        # modifiers TAB, SHift

        self.mod_key_list.append(KeyboardKey("Escape", "Esc", 41))
        self.mod_key_list.append(KeyboardKey("Tab", "Tab", 43))
        self.mod_key_list.append(KeyboardKey("Caps Lock", "Caps", 57))
        self.mod_key_list.append(KeyboardKey("Left Shift", "L Shft", 225))
        self.mod_key_list.append(KeyboardKey("Left Control", "L Ctrl", 224))
        self.mod_key_list.append(KeyboardKey("Left Windows", "L Win", 227))
        self.mod_key_list.append(KeyboardKey("Right Windows", "R Win", 231))
        self.mod_key_list.append(KeyboardKey("Left Command", "L Cmd", 227))
        self.mod_key_list.append(KeyboardKey("Right Command", "R Cmd", 231))
        self.mod_key_list.append(KeyboardKey("Left Option", "L Opt", 226))
        self.mod_key_list.append(KeyboardKey("Right Option", "R Opt", 230))
        self.mod_key_list.append(KeyboardKey("Left Alt", "L Alt", 226))
        self.mod_key_list.append(KeyboardKey("Spacebar", "Space", 44))
        self.mod_key_list.append(KeyboardKey("Right Alt", "R Alt", 230))
        self.mod_key_list.append(KeyboardKey("Right Control", "R Ctrl", 228))
        self.mod_key_list.append(KeyboardKey("Right Shift", "R Shft", 229))
        self.mod_key_list.append(KeyboardKey("Enter", "Enter", 40))
        self.mod_key_list.append(KeyboardKey("Backspace", "BkSpce", 42))

        self.init_key_dict(self.mod_key_list)

        self.punctuation_key_list.append(KeyboardKey("`~", "`~", 53))
        self.punctuation_key_list.append(KeyboardKey("-_", "-_", 45))
        self.punctuation_key_list.append(KeyboardKey("=+", "=+", 46))
        self.punctuation_key_list.append(KeyboardKey("[{", "[{", 47))
        self.punctuation_key_list.append(KeyboardKey("]}", "]}", 48))
        self.punctuation_key_list.append(KeyboardKey("\\|", "\\|", 49))
        self.punctuation_key_list.append(KeyboardKey(";:", ";:", 51))
        self.punctuation_key_list.append(KeyboardKey("'\"", "'\"", 52))
        self.punctuation_key_list.append(KeyboardKey(",<", ",<", 54))
        self.punctuation_key_list.append(KeyboardKey(".>", ".>", 55))
        self.punctuation_key_list.append(KeyboardKey("/?", "/?", 56))
        
        self.init_key_dict(self.punctuation_key_list)

        self.func_key_list.append(KeyboardKey("F1", "F1", 58))
        self.func_key_list.append(KeyboardKey("F2", "F2", 59))
        self.func_key_list.append(KeyboardKey("F3", "F3", 60))
        self.func_key_list.append(KeyboardKey("F4", "F4", 61))
        self.func_key_list.append(KeyboardKey("F5", "F5", 62))
        self.func_key_list.append(KeyboardKey("F6", "F6", 63))
        self.func_key_list.append(KeyboardKey("F7", "F7", 64))
        self.func_key_list.append(KeyboardKey("F8", "F8", 65))
        self.func_key_list.append(KeyboardKey("F9", "F9", 66))
        self.func_key_list.append(KeyboardKey("F10", "F10", 67))
        self.func_key_list.append(KeyboardKey("F11", "F11", 68))
        self.func_key_list.append(KeyboardKey("F12", "F12", 69))

        self.init_key_dict(self.func_key_list)

        self.special_key_list.append(KeyboardKey("Print Screen", "PrtSc", 70))
        self.special_key_list.append(KeyboardKey("Scroll Lock", "ScrLk", 71))
        self.special_key_list.append(KeyboardKey("Pause", "Pause", 72))
        self.special_key_list.append(KeyboardKey("Insert", "Ins", 73))
        self.special_key_list.append(KeyboardKey("Delete", "Del", 76))
        self.special_key_list.append(KeyboardKey("Home", "Home", 74))
        self.special_key_list.append(KeyboardKey("End", "End", 77))
        self.special_key_list.append(KeyboardKey("Page Down", "PgDn", 78))
        self.special_key_list.append(KeyboardKey("Page Up", "PgUp", 75))
        self.special_key_list.append(KeyboardKey("Left", "Left", 80))
        self.special_key_list.append(KeyboardKey("Up", "Up", 82))
        self.special_key_list.append(KeyboardKey("Down", "Down", 81))
        self.special_key_list.append(KeyboardKey("Right", "Right", 79))

        self.int_keyboard_keys_dict(self.special_key_list)

        self.media_key_list.append(KeyboardKey("Mute", "Mute", 127))
        self.media_key_list.append(KeyboardKey("Volume Up", "Vol. Up", 128))
        self.media_key_list.append(KeyboardKey("Volume Down", "Vol.D.", 129))

        self.init_key_dict(self.media_key_list)



    def KeyboardKey(self,key_label, key_short_label, key_value):
        self.key_label = key_label
        self.key_short_label = key_short_label
        self.key_value = key_value

    def KeyboardKey(self, keyboard_key):
        self.key_label = keyboard_key.key_label
        self.key_short_label = keyboard_key.key_short_label
        self.key_value = keyboard_key.key_value

    def init_key_dict(self, keyboard_key_list):
        for key in keyboard_key_list:
            if key.key_label not in self.str_keyboard_keys_dict:
                self.str_keyboard_keys_dict[key.key_label] = key
            if key.key_value not in self.int_keyboard_keys_dict:
                self.int_keyboard_keys_dict[key.key_value] = key



    def init_keyboard_profile(self, profile):
        profile.normal_keys = []
        profile.fn_keys = []

        profile.normal_keys.append(self.int_keyboard_keys_dict[41])
        profile.normal_keys.append(self.int_keyboard_keys_dict[30])
        profile.normal_keys.append(self.int_keyboard_keys_dict[32])
        profile.normal_keys.append(self.int_keyboard_keys_dict[32])
        profile.normal_keys.append(self.int_keyboard_keys_dict[33])
        profile.normal_keys.append(self.int_keyboard_keys_dict[34])
        profile.normal_keys.append(self.int_keyboard_keys_dict[35])
        profile.normal_keys.append(self.int_keyboard_keys_dict[36])
        profile.normal_keys.append(self.int_keyboard_keys_dict[37])
        profile.normal_keys.append(self.int_keyboard_keys_dict[38])
        profile.normal_keys.append(self.int_keyboard_keys_dict[39])
        profile.normal_keys.append(self.int_keyboard_keys_dict[45])
        profile.normal_keys.append(self.int_keyboard_keys_dict[46])
        profile.normal_keys.append(self.int_keyboard_keys_dict[42])
        profile.normal_keys.append(self.int_keyboard_keys_dict[43])
        profile.normal_keys.append(self.int_keyboard_keys_dict[20])
        profile.normal_keys.append(self.int_keyboard_keys_dict[26])
        profile.normal_keys.append(self.int_keyboard_keys_dict[8])
        profile.normal_keys.append(self.int_keyboard_keys_dict[21])
        profile.normal_keys.append(self.int_keyboard_keys_dict[23])
        profile.normal_keys.append(self.int_keyboard_keys_dict[28])
        profile.normal_keys.append(self.int_keyboard_keys_dict[24])
        profile.normal_keys.append(self.int_keyboard_keys_dict[12])
        profile.normal_keys.append(self.int_keyboard_keys_dict[18])
        profile.normal_keys.append(self.int_keyboard_keys_dict[19])
        profile.normal_keys.append(self.int_keyboard_keys_dict[47])
        profile.normal_keys.append(self.int_keyboard_keys_dict[48])
        profile.normal_keys.append(self.int_keyboard_keys_dict[49])
        profile.normal_keys.append(self.int_keyboard_keys_dict[57])
        profile.normal_keys.append(self.int_keyboard_keys_dict[4])
        profile.normal_keys.append(self.int_keyboard_keys_dict[22])
        profile.normal_keys.append(self.int_keyboard_keys_dict[7])
        profile.normal_keys.append(self.int_keyboard_keys_dict[9])
        profile.normal_keys.append(self.int_keyboard_keys_dict[10])
        profile.normal_keys.append(self.int_keyboard_keys_dict[11])
        profile.normal_keys.append(self.int_keyboard_keys_dict[13])
        profile.normal_keys.append(self.int_keyboard_keys_dict[14])
        profile.normal_keys.append(self.int_keyboard_keys_dict[15])
        profile.normal_keys.append(self.int_keyboard_keys_dict[51])
        profile.normal_keys.append(self.int_keyboard_keys_dict[52])
        profile.normal_keys.append(self.int_keyboard_keys_dict[40])
        profile.normal_keys.append(self.int_keyboard_keys_dict[225])
        profile.normal_keys.append(self.int_keyboard_keys_dict[29])
        profile.normal_keys.append(self.int_keyboard_keys_dict[27])
        profile.normal_keys.append(self.int_keyboard_keys_dict[6])
        profile.normal_keys.append(self.int_keyboard_keys_dict[25])
        profile.normal_keys.append(self.int_keyboard_keys_dict[5])
        profile.normal_keys.append(self.int_keyboard_keys_dict[17])
        profile.normal_keys.append(self.int_keyboard_keys_dict[16])
        profile.normal_keys.append(self.int_keyboard_keys_dict[54])
        profile.normal_keys.append(self.int_keyboard_keys_dict[55])
        profile.normal_keys.append(self.int_keyboard_keys_dict[56])
        profile.normal_keys.append(self.int_keyboard_keys_dict[229])
        profile.normal_keys.append(self.int_keyboard_keys_dict[224])
        profile.normal_keys.append(self.int_keyboard_keys_dict[227])
        profile.normal_keys.append(self.int_keyboard_keys_dict[226])
        profile.normal_keys.append(self.int_keyboard_keys_dict[44])
        profile.normal_keys.append(self.int_keyboard_keys_dict[230])
        profile.normal_keys.append(self.int_keyboard_keys_dict[254])
        profile.normal_keys.append(self.int_keyboard_keys_dict[250])
        profile.normal_keys.append(self.int_keyboard_keys_dict[228])

        # Fn layer keys ( Fn + X )
        profile.fn_keys.append(self.int_keyboard_keys_dict[53])
        profile.fn_keys.append(self.int_keyboard_keys_dict[58])
        profile.fn_keys.append(self.int_keyboard_keys_dict[59])
        profile.fn_keys.append(self.int_keyboard_keys_dict[60])
        profile.fn_keys.append(self.int_keyboard_keys_dict[61])
        profile.fn_keys.append(self.int_keyboard_keys_dict[62])
        profile.fn_keys.append(self.int_keyboard_keys_dict[63])
        profile.fn_keys.append(self.int_keyboard_keys_dict[64])
        profile.fn_keys.append(self.int_keyboard_keys_dict[65])
        profile.fn_keys.append(self.int_keyboard_keys_dict[66])
        profile.fn_keys.append(self.int_keyboard_keys_dict[67])
        profile.fn_keys.append(self.int_keyboard_keys_dict[68])
        profile.fn_keys.append(self.int_keyboard_keys_dict[69])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[82])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[82])
        profile.fn_keys.append(self.int_keyboard_keys_dict[71])
        profile.fn_keys.append(self.int_keyboard_keys_dict[72])
        profile.fn_keys.append(self.int_keyboard_keys_dict[74])
        profile.fn_keys.append(self.int_keyboard_keys_dict[77])
        profile.fn_keys.append(self.int_keyboard_keys_dict[70])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[80])
        profile.fn_keys.append(self.int_keyboard_keys_dict[81])
        profile.fn_keys.append(self.int_keyboard_keys_dict[79])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[80])
        profile.fn_keys.append(self.int_keyboard_keys_dict[81])
        profile.fn_keys.append(self.int_keyboard_keys_dict[79])
        profile.fn_keys.append(self.int_keyboard_keys_dict[75])
        profile.fn_keys.append(self.int_keyboard_keys_dict[78])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[73])
        profile.fn_keys.append(self.int_keyboard_keys_dict[76])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[227])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])
        profile.fn_keys.append(self.int_keyboard_keys_dict[254])
        profile.fn_keys.append(self.int_keyboard_keys_dict[250])
        profile.fn_keys.append(self.int_keyboard_keys_dict[0])






