"""Bosch sensor of circuit/zones entities."""

from ..const import (
    CIRCUIT_DEVICE_TRANSLATION_KEYS,
    CIRCUITS_SENSOR_NAMES,
    SIGNAL_SOLAR_UPDATE_BOSCH,
)
from ..entity_translations import SENSOR_TRANSLATION_KEYS
from .base import BoschBaseSensor


class CircuitSensor(BoschBaseSensor):
    """Representation of a Bosch sensor."""

    signal = SIGNAL_SOLAR_UPDATE_BOSCH
    _translation_keys = SENSOR_TRANSLATION_KEYS

    @property
    def device_name(self):
        """Device name."""
        return (
            CIRCUITS_SENSOR_NAMES[self._circuit_type] + " " + self._domain_name
        )

    @property
    def device_translation_key(self):
        return CIRCUIT_DEVICE_TRANSLATION_KEYS.get(self._circuit_type)

    @property
    def device_translation_placeholders(self):
        return {"circuit": self._domain_name}
