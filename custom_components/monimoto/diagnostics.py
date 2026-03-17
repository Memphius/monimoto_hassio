from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import TOKEN_STORAGE_KEY

TO_REDACT = {
    "access_token",
    "refresh_token",
    "bt_aes_key",
    "imei",
    "iccid",
    "uid",
    "phone",
    "email",
    "firebase_user_id",
    "phone_number",
}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    runtime = entry.runtime_data

    data = {
        "entry": dict(entry.data),
        "options": dict(entry.options),
        "coordinator_data": {},
    }

    if TOKEN_STORAGE_KEY in data["entry"]:
        data["entry"][TOKEN_STORAGE_KEY] = {
            "present": True,
            "expires_at": data["entry"][TOKEN_STORAGE_KEY].get("expires_at"),
        }

    coordinator_data = runtime.coordinator.data
    for device_id, device in coordinator_data.items():
        data["coordinator_data"][device_id] = device.raw

    return async_redact_data(data, TO_REDACT)
