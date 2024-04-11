import uuid
from pytradfri import Gateway
from pytradfri.device import light_control, light
from pytradfri.api.libcoap_api import APIFactory 
from pytradfri.api.aiocoap_api import APIFactory as APIFactory_async
from pytradfri.util import load_json, save_json
import os
from typing import Callable


CONFIG_FILE = "tradfri_standalone_psk.conf"



def signe_up(ip, key, timeout):
    
    identity = uuid.uuid4().hex
    api_factory =  APIFactory(host=ip, psk_id=identity, timeout=timeout)
    
    psk = api_factory.generate_psk(key)

    return identity, psk

async def signe_up_async(ip, key):
    
    identity = uuid.uuid4().hex
    
    api_factory = await APIFactory_async.init(host=ip, psk_id=identity)

    psk = await api_factory.generate_psk(key)

    return identity, psk


def get_api(address, config_path = None, timeout = 10):
        config_path = config_path if config_path else CONFIG_FILE
        if not os.path.exists(config_path):
            save_json(config_path, {})
        conf = load_json(config_path)
        if not address in conf.keys():
            key = input("Gib key")
            identity, psk = signe_up(address, key, timeout=timeout)
            conf[address] = {"identity": identity, "psk": psk}
            save_json(config_path, conf)
            conf = load_json(config_path)
        identity = conf[address]["identity"]
        psk = conf[address]["psk"]
        api = APIFactory(host=address, psk_id=identity, psk=psk, timeout=timeout).request
        return api

async def get_api_async(address, config_path = None):
        config_path = config_path if config_path else CONFIG_FILE
        if not os.path.exists(config_path):
            save_json(config_path, {})
        conf = load_json(config_path)
        if not address in conf.keys():
            key = input("Gib key")
            identity, psk = await signe_up_async(address, key)
            conf[address] = {"identity": identity, "psk": psk}
            save_json(config_path, conf)
            conf = load_json(config_path)
        identity = conf[address]["identity"]
        psk = conf[address]["psk"]
        api = (await APIFactory_async.init(host=address, psk_id=identity, psk=psk)).request
        return api
        
        
if __name__ == "__main__":
    print(get_api("192.168.1.175"))