"""
The "transactive home" component.

"""

import asyncio
import logging
import os
import json
from datetime import timedelta
from homeassistant.config import load_yaml_config_file
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_component import EntityComponent


_LOGGER = logging.getLogger(__name__)

DOMAIN = "transactive_home"
FROM = "from"
SCAN_INTERVAL = timedelta(seconds=30)

DEPENDENCIES = []

def setup(hass, config):
    """Setup our skeleton component."""

    _LOGGER.info("Transacive Home loading.")
    
    component = EntityComponent(_LOGGER, DOMAIN, hass, SCAN_INTERVAL)

    component.setup(config)

    descriptions = load_yaml_config_file(
        os.path.join(os.path.dirname(__file__), 'services.yaml'))

    hass.services.register(
        DOMAIN,
        'update_transactive_home',
        update_transactive_home,
        descriptions['update_transactive_home'])

    return True


def update_transactive_home(call):
    """Do any update to the component."""
    _LOGGER.info("A new transactive home value: %s", call.data.get('value'))


class TransactiveComponent(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""

        _LOGGER.info("TransactivePlatform loading.")

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Transactive Home'

    @property
    def state(self):
        """Camera state."""
        return 'happy'

    @property
    def overall_reduction(self):
        """Return the name of the sensor."""
        return 84

    @property
    def state_attributes(self):
        """Return the optional state attributes."""

        data = {
    "measures": [{
            "label": "overall_reduction",
            "value": 51,
            "unit": "kw"
        },
        {
            "label": "overall_energy",
            "value": 80,
            "unit": "kw-hr/24 hrs"
        },
        {
            "label": "overall_power",
            "value": 12,
            "unit": "kw"
        }
    ],
    "dataPointsEnergy": [
        [3, 4, 6]
    ],
    "dataPointsPower": [
        [7, 8, 9]
    ],
    "device": [{
            "name": "device1",
            "participate": "true",
            "efficiency": 30,
            "zone_min": 35,
            "zone_max": 90,
            "power": 150,
            "energy": 40
        },
        {
            "name": "device2",
            "participate": "true",
            "efficiency": 60,
            "zone_min": 35,
            "zone_max": 90,
            "power": 15,
            "energy": 30
        }
    ]
}

        return data
