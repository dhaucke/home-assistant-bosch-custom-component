![Bosch thermostat Integration für Home Assistant](https://raw.githubusercontent.com/dhaucke/home-assistant-bosch-custom-component/master/assets/bosch-banner.svg)

# Bosch thermostat

**Bosch/Buderus/Nefit/IVT-Heizungssteuerung in Home Assistant.**

[![Release](https://img.shields.io/github/v/release/dhaucke/home-assistant-bosch-custom-component?style=flat-square)](https://github.com/dhaucke/home-assistant-bosch-custom-component/releases/latest)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5?style=flat-square)](https://github.com/hacs/integration)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Custom%20Integration-18BCF2?style=flat-square)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/dhaucke/home-assistant-bosch-custom-component?style=flat-square)](https://github.com/dhaucke/home-assistant-bosch-custom-component/blob/master/LICENSE)

[Mit HACS installieren](https://my.home-assistant.io/redirect/hacs_repository/?owner=dhaucke&repository=home-assistant-bosch-custom-component&category=integration) · [Problem melden](https://github.com/dhaucke/home-assistant-bosch-custom-component/issues)

**Sprache:** [Deutsch](#deutsch) · [English](#english)

---

# Deutsch

## Warum dieser Fork existiert

Dies ist ein Fork von [bosch-thermostat/home-assistant-bosch-custom-component](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component). Der Original-Maintainer sucht seit [Issue #414](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component/issues/414) einen zweiten Maintainer und pflegt das Projekt entsprechend zurückhaltend. Ein konkretes Beispiel: Sensoren mit einem nicht erreichbaren Gerät stürzten alle ~30 Sekunden mit `AttributeError: 'BoschSensor' object has no attribute '_attr_state_class'` ab und fluteten damit das Log ([Issue #560](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component/issues/560)). Ein passender, sauberer Fix lag als [PR #563](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component/pull/563) bereit, aber ungemergt.

Dieser Fork übernimmt genau diesen Fix und hält die Integration am Laufen.

### Bekannte, noch offene Baustelle: XMPP → OAuth2/SingleKey ID

Bosch hat die Cloud-Anbindung für EasyControl-Geräte (u. a. CT200) mit EU-Firmware ≥ 05.04.00 von XMPP auf OAuth2/SingleKey ID über die Bosch-POINTT-Cloud-API umgestellt ([Issue #554](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component/issues/554)). Für Geräte mit dieser neuen Firmware funktioniert die Verbindung aktuell **weder im Original noch in diesem Fork**. Es gibt einen experimentellen Community-Fork ([CaseyRo/ha_bosch](https://github.com/CaseyRo/ha_bosch)), der einen funktionierenden, aber selbst als WIP markierten OAuth2-Ansatz zeigt. Eine vollständige Migration ist ein größeres Vorhaben (neuer Cloud-Auth-Flow, eigene Testhardware nötig) und noch nicht Teil dieses Forks.

## Installation

### HACS (empfohlen)

1. In HACS das Drei-Punkte-Menü öffnen → **Custom repositories**.
2. `https://github.com/dhaucke/home-assistant-bosch-custom-component` als Typ **Integration** hinzufügen.
3. **Bosch thermostat** installieren und Home Assistant neu starten.

### Manuell

- Den Ordner `custom_components/bosch` aus diesem Repo in dein Home-Assistant-Verzeichnis `custom_components/bosch` kopieren.
- Home Assistant neu starten.

## Unterstützte Geräte

- IVT (HTTP/XMPP): RC300, RC200, RC35, RC30, RC20
- NEFIT (nur XMPP): Junkers CT100, Bosch Remote room controller CT100
- EASYCONTROL (nur XMPP, siehe Einschränkung oben bei neuerer Firmware): Bosch CT200, Buderus Logamatic TC100.2

## Support

Dies ist ein kleiner, unbezahlter Fork, der gepflegt wird, um reale, bekannte Bugs zu beheben, die im Original unbearbeitet liegen bleiben — kein finanziertes oder im Team betreutes Projekt.

- [Issues](https://github.com/dhaucke/home-assistant-bosch-custom-component/issues)

Wenn du die Arbeit am Original unterstützen möchtest: [:heart: Sponsor (pszafer)](https://github.com/sponsors/pszafer)

## Haftungsausschluss

Dieses Paket und sein Autor stehen in keiner Verbindung zu Bosch, Buderus, Nefit oder IVT. Nutzung auf eigene Gefahr.

## Lizenz

Veröffentlicht unter der ursprünglichen Lizenz von [bosch-thermostat/home-assistant-bosch-custom-component](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component), erhalten in [LICENSE](LICENSE) und in der Projekthistorie.

---

# English

## Why this fork exists

This is a fork of [bosch-thermostat/home-assistant-bosch-custom-component](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component). The original maintainer has been looking for a second maintainer since [issue #414](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component/issues/414) and maintenance has slowed accordingly. Concrete example: sensors on an unreachable device crashed every ~30 seconds with `AttributeError: 'BoschSensor' object has no attribute '_attr_state_class'`, flooding the log ([issue #560](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component/issues/560)). A clean, working fix sat as [PR #563](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component/pull/563), unmerged.

This fork adopts that exact fix and keeps the integration running.

### Known, still-open issue: XMPP → OAuth2/SingleKey ID

Bosch changed cloud connectivity for EasyControl devices (including CT200) on EU firmware ≥ 05.04.00 from XMPP to OAuth2/SingleKey ID via the Bosch POINTT cloud API ([issue #554](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component/issues/554)). Devices on that newer firmware currently work in **neither the original nor this fork**. There's an experimental community fork ([CaseyRo/ha_bosch](https://github.com/CaseyRo/ha_bosch)) with a working but self-described WIP OAuth2 approach. A full migration is a larger undertaking (new cloud auth flow, needs real test hardware) and is not yet part of this fork.

## Installation

### HACS (preferred)

1. In HACS, open the three-dot menu → **Custom repositories**.
2. Add `https://github.com/dhaucke/home-assistant-bosch-custom-component` as type **Integration**.
3. Install **Bosch thermostat** and restart Home Assistant.

### Manual

- Copy `custom_components/bosch` from this repo into your Home Assistant `custom_components/bosch`.
- Restart Home Assistant.

## Supported devices

- IVT (HTTP/XMPP): RC300, RC200, RC35, RC30, RC20
- NEFIT (XMPP only): Junkers CT100, Bosch Remote room controller CT100
- EASYCONTROL (XMPP only, see the limitation above for newer firmware): Bosch CT200, Buderus Logamatic TC100.2

## Support

This is a small, unpaid fork maintained to fix real, known bugs left unaddressed upstream — not a funded or team-maintained project.

- [Issues](https://github.com/dhaucke/home-assistant-bosch-custom-component/issues)

If you'd like to support work on the original: [:heart: Sponsor (pszafer)](https://github.com/sponsors/pszafer)

## Disclaimer

This package and its author are not affiliated with Bosch, Buderus, Nefit, or IVT. Use at your own risk.

## License

Released under the original license from [bosch-thermostat/home-assistant-bosch-custom-component](https://github.com/bosch-thermostat/home-assistant-bosch-custom-component), preserved in [LICENSE](LICENSE) and in the project history.
