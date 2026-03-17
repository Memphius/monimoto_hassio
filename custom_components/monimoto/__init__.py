from __future__ import annotations

from dataclasses import dataclass

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import MonimotoApiClient, TokenData
from .const import (
    CONF_API_HOST,
    CONF_EMAIL,
    CONF_VERIFY_SSL,
    DOMAIN,
    PLATFORMS,
    TOKEN_STORAGE_KEY,
)
from .coordinator import MonimotoCoordinator


@dataclass(slots=True)
class RuntimeData:
    client: MonimotoApiClient
    coordinator: MonimotoCoordinator


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    session = async_get_clientsession(hass)

    client = MonimotoApiClient(
        session,
        email=entry.data[CONF_EMAIL],
        api_host=entry.data[CONF_API_HOST],
        verify_ssl=entry.data[CONF_VERIFY_SSL],
    )

    if token_data := entry.data.get(TOKEN_STORAGE_KEY):
        client.set_token(TokenData.from_storage_dict(token_data))

    coordinator = MonimotoCoordinator(hass, entry, client)
    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = RuntimeData(client=client, coordinator=coordinator)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
