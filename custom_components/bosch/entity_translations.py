"""Mapping from Bosch gateway attr_id (stable, protocol-level URI) to a
translation_key.

Most entity names in this integration come directly from the physical
Bosch gateway's own API responses at runtime, not from static strings in
this codebase - there is no fixed, complete set of them known in advance
(different gateway/appliance models expose different attributes). These
tables only cover attr_ids that have been confirmed against a real
device. Anything not listed here keeps the raw, device-reported name as
before - HA's translation_key mechanism can only translate a known,
closed set of keys, so an untranslated fallback is unavoidable for
attr_ids not yet catalogued here.

Split by platform/sensor kind because the same underlying attr_id can be
exposed by more than one entity kind (e.g. a "recording" sensor records
the history of a value also shown live by a "regular" sensor), and each
needs its own translation_key/device grouping.
"""

# "Bosch sensors" (regular kind) and circuit sensors (hc1/dhw1 etc, same
# BoschBaseSensor machinery), keyed by attr_id.
SENSOR_TRANSLATION_KEYS: dict[str, str] = {
    "/heatSources/CHpumpModulation": "ch_pump_modulation",
    "/heatSources/actualPower": "actual_power",
    "/heatSources/energyMonitoring/consumption": "energy_consumption",
    "/system/healthStatus": "health_status",
    "/system/sensors/temperatures/hotWater_t2": "hotwater_temp",
    "/notifications": "notifications",
    "/system/sensors/temperatures/outdoor_t1": "outdoor_temperature",
    "/heatSources/systemPressure": "system_pressure",
    "/heatSources/workingTime": "total_system_uptime",
    "/heatingCircuits/hc1/actualSupplyTemperature": "hc_actual_supply_temperature",
    "/heatingCircuits/hc1/currentSuWiMode": "hc_current_summer_winter_mode",
    "/heatingCircuits/hc1/suWiSwitchMode": "hc_summer_winter_switchmode",
    "/heatingCircuits/hc1/suWiThreshold": "hc_summer_winter_threshold",
    "/heatingCircuits/hc1/supplyTemperatureSetpoint": "hc_supply_temperature_setpoint",
    "/dhwCircuits/dhw1/waterFlow": "dhw_water_flow",
    "/dhwCircuits/dhw1/workingTime": "dhw_working_time",
}

# "Recording sensors" (statistics/history sensors, RecordingSensor class).
RECORDING_TRANSLATION_KEYS: dict[str, str] = {
    "/heatSources/actualCHPower": "recording_actual_ch_power",
    "/heatSources/actualDHWPower": "recording_actual_dhw_power",
    "/heatSources/actualPower": "recording_actual_power",
    "/dhwCircuits/dhw1/actualTemp": "recording_actual_temp",
    "/system/sensors/temperatures/outdoor_t1": "recording_outdoor_temp",
    "/heatingCircuits/hc1/roomtemperature": "recording_room_temperature",
}

BINARY_SENSOR_TRANSLATION_KEYS: dict[str, str] = {
    "/heatSources/flameStatus": "flame_status",
}

SWITCH_TRANSLATION_KEYS: dict[str, str] = {
    "/dhwCircuits/dhw1/charge": "dhw_charge",
}
