# Monimoto for Home Assistant

Custom Home Assistant integratie voor Monimoto trackers.

## Status

Deze integratie is een niet-officiële Home Assistant custom integration voor Monimoto.  
De integratie logt in via de Monimoto e-mail loginflow, slaat tokens op in de config entry en haalt daarna periodiek trackerdata op uit de Monimoto cloud.

## Ondersteunde functies

### Config flow
- inloggen met e-mailadres
- bevestigen met e-mailcode
- automatische opslag van access token en refresh token

### Data ophalen
- devices ophalen
- rapporten/history ophalen
- automatische token refresh
- periodieke polling via DataUpdateCoordinator

### Entiteiten
De integratie maakt onder meer deze entiteiten aan:

#### Sensors
- batterijpercentage
- key fob batterij
- tracker temperatuur
- SIM status
- firmware
- device status
- laatste bericht
- laatste rapporttijd
- laatste bekende locatie update
- regular ping interval
- IMEI
- ICCID
- GSM level
- latitude
- longitude

#### Binary sensors
- batterij laag
- batterij laden
- SIM gedeactiveerd
- tracking actief

#### Device tracker
- GPS-locatie op basis van de laatste bekende report/location

#### Buttons
- refresh now
- start tracking
- stop tracking
- trigger alarm

#### Number
- snooze duration

#### Select
- tracking mode

### Services
Deze domeinservices zijn beschikbaar:

- `monimoto.refresh`
- `monimoto.start_tracking`
- `monimoto.stop_tracking`
- `monimoto.snooze`
- `monimoto.trigger_alarm`

## Installatie

### Handmatig
Kopieer de map `custom_components/monimoto` naar:

`/config/custom_components/monimoto`

Herstart daarna Home Assistant.

### Via HACS
Voeg deze repository toe als custom repository in HACS en installeer daarna de integratie.

Repository:

`https://github.com/Memphius/monimoto_hassio`

## Configuratie

Ga in Home Assistant naar:

**Instellingen → Apparaten en diensten → Integratie toevoegen**

Zoek op:

**Monimoto**

Daarna:
1. vul je Monimoto e-mailadres in
2. ontvang de code per e-mail
3. voer de code in
4. klaar

## Opties

Na toevoegen kun je via de integratie-opties het poll-interval aanpassen.

## Voorbeeld service-calls

### Tracking starten
```yaml
service: monimoto.start_tracking
data:
  blename: mm.E3CE8EB834B2
