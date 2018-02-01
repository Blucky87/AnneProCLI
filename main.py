import bluetooth
import KeyboardKey
import KeyboardWriter
import KeyboardProfileItem


# print("performing inquiry...")
#
# nearby_devices = bluetooth.discover_devices(
#         duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
#
# print("found %d devices" % len(nearby_devices))
#
# for addr, name in nearby_devices:
#     try:
#         print("  %s - %s" % (addr, name))
#     except UnicodeEncodeError:
#         print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
#

# import sys
# from gattlib import GATTRequester
#
#
# class Reader(object):
#     def __init__(self, address):
#         self.requester = GATTRequester(address, False)
#         self.connect()
#         self.request_data()
#
#     def connect(self):
#         print("Connecting...", end=' ')
#         sys.stdout.flush()
#
#         self.requester.connect(True)
#         print("OK!")
#
#     def request_data(self):
#         data = self.requester.read_by_handle(0x10)[0]
#
#         print("bytes received:", end=' ')
#         for b in data:
#             print(hex(ord(b)), end=' ')
#         print("")
#
#
# if __name__ == '__main__':
#
#     Reader('60:64:05:B3:C4:53')
#     print("Done.")





# from gattlib import DiscoveryService, GATTRequester
#
#
#
# req = GATTRequester('60:64:05:B3:C4:53')
# req.write_by_handle(0x10, str(bytearray([14, 4, 56])))

# # #
# # import bluetooth
# #
# # print("performing inquiry...")
# #
# # nearby_devices = bluetooth.discover_devices(
# #         duration=8, lookup_names=True, flush_cache=True, lookup_class=False, device_id=0)
# #
# # print("found %d devices" % len(nearby_devices))
# #
# # for addr, name in nearby_devices:
# #     try:
# #         print("  %s - %s" % (addr, name))
# #     except UnicodeEncodeError:
# #         print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
#
# from bluepy.btle import Scanner, DefaultDelegate, Peripheral, ADDR_TYPE_RANDOM, BTLEException, AssignedNumbers
#
# # class ScanDelegate(DefaultDelegate):
# #     def __init__(self):
# #         DefaultDelegate.__init__(self)
# #
# #     def handleDiscovery(self, dev, isNewDev, isNewData):
# #         if isNewDev:
# #             print("Discovered device", dev.addr)
# #         elif isNewData:
# #             print("Received new data from", dev.addr)
# #
# # scanner = Scanner(iface=0).withDelegate(ScanDelegate())
# # devices = scanner.scan(10.0)
# #
# # for dev in devices:
# #     print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
# #     for (adtype, desc, value) in dev.getScanData():
# #         print("  %s = %s" % (desc, value))
# # print("--"*30)
# #
# # item = Peripheral()
# # item.connect('60:64:05:B3:C4:53',iface=1)
#
# conn = Peripheral('60:64:05:B3:C4:53')
# try:
#     for svc in conn.services:
#         print(str(svc), ":")
#         for ch in svc.getCharacteristics():
#             print("    {}, hnd={}, supports {}".format(ch, hex(ch.handle),
#                                                        ch.propertiesToString()))
#             chName = AssignedNumbers.getCommonName(ch.uuid)
#             if (ch.supportsRead()):
#                 try:
#                     print("    ->", repr(ch.read()))
#                 except BTLEException as e:
#                     print("    ->", e)
#
# finally:
#     conn.disconnect()


bytesa = bytearray()

bytesa.append(0x09)
bytesa.append(0xD7)
bytesa.append(0x03)

lighting_meta_data = bytes([0x09, 0xD7, 0x03])

print()