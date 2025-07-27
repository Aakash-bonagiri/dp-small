class USPlug:
    def connect(self):
        print("Connected to US socket.")

class EuropeanPlug:
    def connect_to_eu_socket(self):
        print("Connected to European socket.")

class PlugAdapter(USPlug):
    def __init__(self, euro_plug):
        self.euro_plug = euro_plug

    def connect(self):
        print("Using adapter...")
        self.euro_plug.connect_to_eu_socket()

def charge_device(plug: USPlug):
    plug.connect()

print("Without Adapter:")
us_plug = USPlug()
charge_device(us_plug)

print("\nWith Adapter:")
euro_plug = EuropeanPlug()
adapter = PlugAdapter(euro_plug)
charge_device(adapter)
