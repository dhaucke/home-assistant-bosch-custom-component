"""Bosch base entity."""
import logging

from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from .const import DEFAULT_MAX_TEMP, DEFAULT_MIN_TEMP, DOMAIN
from homeassistant.helpers.entity import DeviceInfo

_LOGGER = logging.getLogger(__name__)


def async_migrate_unique_id(
    hass: HomeAssistant,
    platform_domain: str,
    old_unique_id: str,
    new_unique_id: str,
) -> None:
    """Migrate an entity registry entry from an old to a new unique_id.

    Older releases derived unique_id from the (mutable, potentially
    localizable) display name instead of a stable identifier. If an
    entity is still registered under the old unique_id, move it to the
    new one in-place so the entity_id, history and any user
    customizations survive.
    """
    if old_unique_id == new_unique_id:
        return
    registry = er.async_get(hass)
    old_entity_id = registry.async_get_entity_id(
        platform_domain, DOMAIN, old_unique_id
    )
    if not old_entity_id:
        return
    existing_new = registry.async_get_entity_id(
        platform_domain, DOMAIN, new_unique_id
    )
    if existing_new:
        return
    _LOGGER.debug(
        "Migrating unique_id for %s from %s to %s",
        old_entity_id,
        old_unique_id,
        new_unique_id,
    )
    registry.async_update_entity(old_entity_id, new_unique_id=new_unique_id)


class BoschEntity:
    """Bosch base entity class."""

    def __init__(self, **kwargs):
        """Initialize the entity."""
        if not hasattr(self, "_domain_name"):
            self._domain_name = kwargs.get("domain_name")
        self.hass = kwargs.get("hass")
        self._bosch_object = kwargs.get("bosch_object")
        self._gateway = kwargs.get("gateway")
        self._uuid = kwargs.get("uuid")

    @property
    def bosch_object(self):
        """Return upstream component. Used for refreshing."""
        return self._bosch_object

    async def async_added_to_hass(self):
        """Register callbacks."""
        self.async_on_remove(
            async_dispatcher_connect(self.hass, self.signal, self.async_update)
        )

    @property
    def _domain_identifier(self):
        if self._bosch_object.parent_id:
            return {(DOMAIN, self._bosch_object.parent_id, self._uuid)}
        return {(DOMAIN, self._domain_name, self._uuid)}

    @property
    def device_translation_key(self) -> str | None:
        """Translation key for the device name, if translatable."""
        return None

    @property
    def device_translation_placeholders(self) -> dict[str, str] | None:
        """Placeholders for the device name translation, if any."""
        return None

    @property
    def device_info(self) -> DeviceInfo:
        """Get attributes about the device."""
        info = DeviceInfo(
            identifiers=self._domain_identifier,
            manufacturer=self._gateway.device_model,
            model=self._gateway.device_type,
            sw_version=self._gateway.firmware,
            hw_version=self._uuid,
            via_device=(DOMAIN, self._uuid),
        )
        translation_key = self.device_translation_key
        if translation_key:
            info["translation_key"] = translation_key
            placeholders = self.device_translation_placeholders
            if placeholders:
                info["translation_placeholders"] = placeholders
        else:
            info["name"] = self.device_name
        return info


class BoschClimateWaterEntity(BoschEntity):
    """Bosch climate and water entities base class."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._attr_name = self._bosch_object.name
        self._temperature_unit = UnitOfTemperature.CELSIUS
        self._attr_unique_id = f"{self._uuid}{self._bosch_object.id}"
        self._current_temperature = None
        self._state = None
        self._target_temperature = None

    @property
    def _domain_identifier(self):
        return {(DOMAIN, self._bosch_object.id, self._uuid)}

    @property
    def device_name(self):
        """Return name displayed in device_info."""
        return f"{self._name_prefix} {self._attr_name}"

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
        return self._temperature_unit

    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self._current_temperature

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self._target_temperature

    @property
    def min_temp(self):
        """Return the minimum temperature."""
        return (
            self._bosch_object.min_temp
            if self._bosch_object.min_temp
            else DEFAULT_MIN_TEMP
        )

    @property
    def max_temp(self):
        """Return the maximum temperature."""
        return (
            self._bosch_object.max_temp
            if self._bosch_object.max_temp
            else DEFAULT_MAX_TEMP
        )
