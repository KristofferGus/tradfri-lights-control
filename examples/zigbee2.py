from zigpy import zdo
from zigpy.application import ControllerApplication
from zigpy.zdo.types import NodeDescriptor, PowerDescriptor

def scan_zigbee_devices():
    # Create a Zigbee controller application
    app = ControllerApplication()

    # Start the Zigbee network
    app.startup(auto_form=False)

    # Perform a network scan to find Zigbee devices
    scan_results = zdo.ZDO(app)
    nodes = scan_results.active()

    # Print information about each Zigbee device found
    print("Zigbee devices found:")
    for node in nodes:
        ieee = node['ieee']
        network_address = node['nwk']
        node_descriptor = NodeDescriptor.deserialize(node['nodeDescriptor'])
        power_descriptor = PowerDescriptor.deserialize(node['powerDescriptor'])
        print(f"  IEEE Address: {ieee}, Network Address: {network_address}")
        print(f"    Logical Type: {node_descriptor.LogicalType}, Manufacturer Code: {node_descriptor.ManufacturerCode}")
        print(f"    Power Mode: {power_descriptor.PowerMode}, Power Source: {power_descriptor.PowerSource}")
        print()

if __name__ == "__main__":
    scan_zigbee_devices()
