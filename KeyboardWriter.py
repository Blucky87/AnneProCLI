import math

class KeyboardWrite(object):
    write_gatt = None
    meta_data = None
    send_data = None
    send_buffer = None

    blocks_sent = None
    max_blocks = None
    bytes_sent = None

    OAD_BLOCK_SIZE = 14
    OAD_BUFFER_SIZE = 20

    def KeyboardWriter(self, write_gatt, meta_data, send_data):
        self.write_gatt = write_gatt
        self.meta_data = meta_data
        self.send_data = send_data

        # array size of OAD_BUFFER_SIZE
        self.send_buffer = []
        self.blocks_sent = 0
        self.bytes_sent = 0
        self.max_blocks = len(meta_data) \
            if send_data is None \
            else math.ceil(len(send_data) * 1.0 / self.OAD_BLOCK_SIZE)

    def ThreadedWriteData(self):
        if(self.blocks_sent < self.max_blocks):
            try:
                if self.send_data is None:
                    #data writer object
                    small_writer = self.unknown()
                    print("small writer write bytes")
                    return
                if len(self.send_data) < self.OAD_BLOCK_SIZE:
                    # copy send_data into send_buffer
                    self.unknown()
                else:
                    if self.bytes_sent + self.OAD_BLOCK_SIZE < len(self.send_data):
                        self.send_buffer[3] = 16
                    else:
                        self.send_buffer[3] = len(self.send_data - self.bytes_sent + 2)
                    self.send_buffer[4] = self.max_blocks
                    self.send_buffer[5] = self.blocks_sent
                    # copy send data into buffer points
                writer = self.unknown()
                # writer write bytes of send_buffer
                result = None

                if result != 'gatt success':
                    return

                self.blocks_sent += 1
                self.bytes_sent += self.OAD_BLOCK_SIZE

                self.write_to_keyboard()
            except Exception as err:
                print(err)


    def write_to_keyboard(self):
        #write_task start
        write_task = self.unknown()



    def unknown(self):
        print("????")
