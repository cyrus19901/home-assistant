"""
The "transactive home" custom component.

This component implements the bare minimum that a component should implement.

Configuration:

To use the transactive_home component you will need to add the following to your
configuration.yaml file.

transactive_home:
"""

import logging
import json

_LOGGER = logging.getLogger(__name__)

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "transactive_home"
FROM = "from"

# List of component names (string) your component depends upon.
DEPENDENCIES = []


def setup(hass, config):
    """Setup our skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.		
    # hass.states.set('transactive_home.success', config[DOMAIN])
    hass.states.set('transactive_home.success', json.dumps(config[DOMAIN]))

    # reduction = config[DOMAIN].get('overall_reduction', 0)
    # power = config[DOMAIN].get('overall_power', 100)
    # energy = config[DOMAIN].get('overall_energy', 100)

    # # States are in the format DOMAIN.OBJECT_ID
    # hass.states.set('transactive_home.Reduction', reduction)
    # hass.states.set('transactive_home.Power', power)
    # hass.states.set('transactive_home.Energy', energy)


    _LOGGER.info("Transacive Home loading.")
    # Return boolean to indicate that initialization was successfully.
    return True
