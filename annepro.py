from gatt import DeviceManager, Device, Service, Characteristic
import time
import re


class AnneManager(DeviceManager):
    def __init__(self, adapter_name):
        print("-- anne pro manager created using bluetooth adapter: " + adapter_name + " --")
        super().__init__(adapter_name)

    def update_devices(self):
        print("BT Adapter: " + self.adapter_name + " | updating devices")
        super().update_devices()

    def make_device(self, mac_address):
        device = Device(mac_address=mac_address, manager=self, managed=False)
        if "anne" in device.alias().lower():
            print("BT Adapter: " + self.adapter_name + " | Anne Pro Keyboard found (" + device.mac_address + ")")
            return AnnePro(mac_address=mac_address, manager=self)




class AnnePro(Device):
    def __init__(self, mac_address, manager):
        super().__init__(mac_address, manager)
        print("-- Discovered: Anne Pro Keyboard:")
        print("\t{}: {}".format("MAC", self.mac_address))
        print("\t{}: {}".format("Alias", self.alias()))
        print("\t{}: {}".format("Adapter", self.manager.adapter_name))

    def connect(self):
        print("BT Adapter: " + self.manager.adapter_name + " | establishing connection with " + self.alias() + " (" + self.mac_address + ")...")
        super().connect()

    def connect_succeeded(self):
        super().connect_succeeded()
        print("BT Adapter: " + self.manager.adapter_name + " | successful connection with " + self.alias() + " (" + self.mac_address + ")!")

    def connect_failed(self, error):
        super().connect_failed(error)
        print("BT Adapter: " + self.manager.adapter_name + " | failed connection with " + self.alias() + " (" + self.mac_address + ")!")
        print(error)

    def services_resolved(self):
        self._disconnect_service_signals()
        self.services = list()

        services_regex = re.compile(self._device_path + '/service[0-9abcdef]{4}$')
        managed_services = [
            service for service in self._object_manager.GetManagedObjects().items()
            if services_regex.match(service[0])]

        for service in managed_services:
            if service[1]['org.bluez.GattService1']['UUID'] == 'f000ffc0-0451-4000-b000-000000000000':
                self.services.append(OverAirDownloadService(device=self, path=service[0]))

        print("BT Device: " + self.mac_address + " | " + str(len(self.services)) + " resolved services saved")

    def characteristic_write_value_succeeded(self, characteristic):
        super().characteristic_write_value_succeeded(characteristic)
        print("Characteristic: " + characteristic.uuid + " | successful write to device " + self.mac_address)

    def characteristic_write_value_failed(self, characteristic, error):
        super().characteristic_write_value_failed(characteristic, error)
        print("Characteristic: " + characteristic.uuid + " | failed write to device " + str(self.mac_address))


class OverAirDownloadService(Service):
    def __init__(self, device, path):
        super().__init__(device, path, 'f000ffc0-0451-4000-b000-000000000000')
        print("-- Discovered: Over Air Download Service")
        print("\t{}: {}".format("UUID", self.uuid))
        print("\t{}: {}".format("Device", self.device.mac_address))
        print("\t{}: {}".format("Adapter", self.device.manager.adapter_name))

    def characteristics_resolved(self):
        """
        Called when all service's characteristics got resolved.
        """
        self._disconnect_characteristic_signals()

        characteristics_regex = re.compile(self._path + '/char[0-9abcdef]{4}$')
        managed_characteristics = [
            char for char in self._object_manager.GetManagedObjects().items()
            if characteristics_regex.match(char[0])]

        self.characteristics = list()
        for characteristic in managed_characteristics:
            if characteristic[1]['org.bluez.GattCharacteristic1']['UUID'] == 'f000ffc2-0451-4000-b000-000000000000':
                self.characteristics.append(OADWriteCharacteristic(service=self,
                                                                  path=characteristic[0],
                                                                  uuid=characteristic[1]['org.bluez.GattCharacteristic1']['UUID']))

            elif characteristic[1]['org.bluez.GattCharacteristic1']['UUID'] == 'f000ffc1-0451-4000-b000-000000000000':
                self.characteristics.append(OADReadCharacteristic(service=self,
                                                                  path=characteristic[0],
                                                                  uuid=characteristic[1]['org.bluez.GattCharacteristic1']['UUID']))

        self._connect_characteristic_signals()

class OADWriteCharacteristic(Characteristic):
    def __init__(self, service, path, uuid):
        super().__init__(service, path, uuid)
        print("-- Discovered: Over Air Download Service - Write Characteristic")
        print("\t{}: {}".format("UUID", self.uuid))
        print("\t{}: {}".format("Service UUID", self.service.uuid))
        print("\t{}: {}".format("Device", self.service.device.mac_address))
        print("\t{}: {}".format("Adapter", self.service.device.manager.adapter_name))

    def write_value(self, value, offset=0):
        print("Characteristic: " + str(self.uuid) + " | writing data with offset " + str(offset))
        print(value)
        super().write_value(value, offset)


class OADReadCharacteristic(Characteristic):
    def __init__(self, service, path, uuid):
        super().__init__(service, path, uuid)
        print("-- Discovered: Over Air Download Service - Read Characteristic")
        print("\t{}: {}".format("UUID", self.uuid))
        print("\t{}: {}".format("Service UUID", self.service.uuid))
        print("\t{}: {}".format("Device", self.service.device.mac_address))
        print("\t{}: {}".format("Adapter", self.service.device.manager.adapter_name))

    def write_value(self, value, offset=0):
        print("Characteristic: " + self.uuid + " | writing data with offset " + offset)
        print(value)
        super().write_value(value, offset)


# def findAnne(deviceList : list(Device)):
#     for item in deviceList:
#         if item.
# test = dict()

class Test(object):
    mac_address = '60:64:05:b3:c4:53'

test = Test()
adaptor = AnneManager("hci0")

theAnne = None
anne = adaptor.devices()
for item in anne:
    theAnne = item
    theAnne.connect()


time.sleep(5)
theAnne.services[0].characteristics[0].write_value([0x02,0x99])
adaptor.run()
print(" d")
