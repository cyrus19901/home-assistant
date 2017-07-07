"""
The "transactive platform" platform.

"""

import logging
from custom_components.transactive_home import TransactiveComponent

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""

    _LOGGER.info("Setting up TransactivePlatform.")

    add_devices([TransactivePlatform()])


class TransactivePlatform(TransactiveComponent):
    """Representation of a demo climate device."""

    def __init__(self):
        """Initialize the climate device."""
        self._state = 'On'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Transactive Home'

