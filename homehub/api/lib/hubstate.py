

import json
import os

from api.lib import tmp_lib
from api.lib import script_logger


class HubState:

    STATE_KEY_IS_ONLINE = "isonline"

    def __init__(self):
        self.logger = script_logger.get_hub_logger()

        self._filepath = tmp_lib.generate_named_tmp_file("hub-state.json")
        if not os.path.exists(self._filepath):
            self.logger.warning("hubstate not found, creating hubstate file with default values")
            data = {
                self.STATE_KEY_IS_ONLINE: True
            }
            with open(self._filepath, "w") as f:
                json.dump(data, f)


    def getkey(self, key:str):
        self.logger.debug(f"Feting hubstate key {key}")
        with open(self._filepath, "r") as f:
            value = json.load(f)[key]
        self.logger.debug(f"Found hubstate value of {value}")
        return value


    def setkey(self, key, value):
        self.logger.debug(f"Setting hubstate key {key} to {value}")
        with open(self._filepath, "r") as f:
            data = json.load(f)

        data[key] = value
        with open(self._filepath, "w") as f:
            json.dump(data, f)


    def delete_file(self):
        if os.path.exists(self._filepath):
            os.remove(self._filepath)

