# Monimoto for Home Assistant

Custom Home Assistant integratie voor Monimoto.

## Wat doet deze integratie

Deze integratie haalt trackergegevens op uit de Monimoto cloud en maakt daarvan Home Assistant-entiteiten aan, zoals:

- batterijpercentage
- batterijstatus
- key fob batterij
- tracker temperatuur
- SIM status
- firmware
- device status
- tracking status
- laatste bekende locatie
- laatste rapporttijd
- laatste bericht

## Authenticatie

De integratie gebruikt de Monimoto e-mail loginflow:

1. je vult je e-mailadres in
2. Home Assistant start de login via Monimoto
3. je ontvangt een code per e-mail
4. je voert de code in
5. Home Assistant slaat access- en refresh-token op
6. data wordt periodiek opgehaald

## Installatie

Kopieer deze map naar:

`/config/custom_components/monimoto`

Herstart Home Assistant.

## Configuratie

Ga naar:

Instellingen → Apparaten en diensten → Integratie toevoegen

Zoek op:

`Monimoto`

## Disclaimer

Dit project is niet officieel gelieerd aan Monimoto. Gebruik op eigen risico.
