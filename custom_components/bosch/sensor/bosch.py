"""Bosch regular sensor."""
from ..const import SIGNAL_SENSOR_UPDATE_BOSCH
from ..entity_translations import SENSOR_TRANSLATION_KEYS
from .base import BoschBaseSensor


class BoschSensor(BoschBaseSensor):
    """Representation of a Bosch sensor."""

    signal = SIGNAL_SENSOR_UPDATE_BOSCH
    _domain_name = "Sensors"
    _translation_keys = SENSOR_TRANSLATION_KEYS

    @property
    def device_name(self):
        return "Bosch sensors"

    @property
    def device_translation_key(self):
        return "bosch_sensors"
