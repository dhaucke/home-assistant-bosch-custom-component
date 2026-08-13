"""Mapping from Bosch attr_id (the internal, stable key the
bosch_thermostat_client library assigns to each sensor/switch - see
that library's db/<system>/<firmware>.json schema files) to a
translation_key.

attr_id is NOT the full API URI. It's a short, schema-defined key (e.g.
"CHpumpModulation", "actualSupplyTemperature", "flameStatus") that the
library uses as a lookup key internally; the full URI lives in a
separate "id"/"path" field it resolves through that key. Verified
directly against bosch_thermostat_client's own db/rc300_rc200/*.json
schema files and a real debug_scan from a live gateway (see CHANGELOG).

Most entity names in this integration come directly from the physical
Bosch gateway's own db schema at runtime, not from static strings in
this codebase - there is no fixed, complete set of them known in
advance (different gateway/appliance models ship different schema
files). These tables only cover attr_ids confirmed against a real
device. Anything not listed here keeps the raw, device-reported name as
before - HA's translation_key mechanism can only translate a known,
closed set of keys, so an untranslated fallback is unavoidable for
attr_ids not yet catalogued here.

Split by platform/sensor kind because the same underlying value can be
exposed by more than one entity kind under a different attr_id (e.g. a
"recording" sensor's attr_id is a synthesized "r"-prefixed key, not the
same attr_id as the "regular" sensor recording the same value), and
each needs its own translation_key/device grouping.
"""

# "Bosch sensors" (regular kind, gateway-level) and circuit sensors
# (hc1/dhw1 etc, same BoschBaseSensor machinery), keyed by attr_id.
SENSOR_TRANSLATION_KEYS: dict[str, str] = {
    # gateway-level (db/rc300_rc200/*.json "sensors")
    "CHpumpModulation": "ch_pump_modulation",
    "actualPower": "actual_power",
    "energyConsumption": "energy_consumption",
    "healthStatus": "health_status",
    "hotWater_t2": "hotwater_temp",
    "notifications": "notifications",
    "outdoor_t1": "outdoor_temperature",
    "systemPressure": "system_pressure",
    "totalSystem": "total_system_uptime",
    "supply_t1_setpoint": "system_supply_temp_setpoint",
    "supply_t1": "system_actual_supply_temp",
    "switch_temperature": "switch_temp",
    "return": "return_temp",
    "chimney": "chimney_temp",
    "actualSupplyTemp": "appliance_supply_temperature",
    "actualModulation": "actual_modulation",
    "startDateTime": "energy_start_time",
    "burnerPowerSetpoint": "burner_power_setpoint",
    "numberOfStarts": "number_of_starts",
    "poolTemperature": "pool_temperature",
    # heatingCircuits.sensors (hc1 etc)
    "actualSupplyTemperature": "hc_actual_supply_temperature",
    "currentSuWiMode": "hc_current_summer_winter_mode",
    "suWiSwitchMode": "hc_summer_winter_switchmode",
    "suWiThreshold": "hc_summer_winter_threshold",
    "supplyTemperatureSetpoint": "hc_supply_temperature_setpoint",
    "pumpModulation": "hc_pump_modulation",
    "currentRoomSetpoint": "hc_current_room_setpoint",
    # dhwCircuits.sensors (dhw1 etc)
    "waterFlow": "dhw_water_flow",
    "workingTime": "dhw_working_time",
}

# "Recording sensors" (statistics/history sensors, RecordingSensor
# class). Their attr_id is synthesized by the library as
# f"r{last_uri_segment}" - see bosch_thermostat_client's
# Sensors.initialize()/get_id().
RECORDING_TRANSLATION_KEYS: dict[str, str] = {
    "ractualCHPower": "recording_actual_ch_power",
    "ractualDHWPower": "recording_actual_dhw_power",
    "ractualPower": "recording_actual_power",
    "ractualTemp": "recording_actual_temp",
    "routdoor_t1": "recording_outdoor_temp",
    "rroomtemperature": "recording_room_temperature",
}

BINARY_SENSOR_TRANSLATION_KEYS: dict[str, str] = {
    "flameStatus": "flame_status",
    "ChimneySweeper": "chimney_sweeper",
}

SWITCH_TRANSLATION_KEYS: dict[str, str] = {
    "charge": "dhw_charge",
}

NUMBER_TRANSLATION_KEYS: dict[str, str] = {
    "chargeDuration": "dhw_charge_duration",
    "singleChargeSetpoint": "dhw_charge_setpoint",
    "poolSetpointTemperature": "pool_setpoint_temperature",
}
