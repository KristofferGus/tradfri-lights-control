from zigpy.zigbee import ZigBee
from zigpy.zigate import ZiGate
from zigpy.config import CONF_DEVICE
import asyncio

async def main():
    # Replace '/dev/ttyUSB0' with your actual device path
    config = {CONF_DEVICE: '/dev/ttyUSB0'}
    zigate = ZiGate()
    await zigate.application_start(config)
    zigbee = ZigBee(zigate)
    await zigbee.startup(auto_form=True)

    # Your code to interact with Tradfri lamps goes here

    await zigbee.shutdown()
    await zigate.close()

asyncio.run(main())
