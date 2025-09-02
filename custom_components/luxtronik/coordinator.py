# Updated LuxtronikCoordinator Class

class LuxtronikCoordinator:
    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.device_infos = {
            f"{self.unique_id}_{DeviceKey.heatpump.value}": {},
            # Add other unique keys as needed
        }

    def get_device(self, key):
        # Update to handle unique keys
        return self.device_infos.get(key)

    def _create_device_infos(self):
        # Update to create device info with unique keys
        for device in self.devices:
            self.device_infos[f"{self.unique_id}_{device.key}"] = device.info

    # Update all other methods that access device_infos to use unique keys accordingly
