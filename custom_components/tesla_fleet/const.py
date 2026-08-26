"""Constants used by Tesla Fleet integration."""

from enum import StrEnum
import logging

from tesla_fleet_api.const import SERVERS, Scope

DOMAIN = "tesla_fleet"

CONF_REFRESH_TOKEN = "refresh_token"

# Regions the user can register in. China uses separate infrastructure
# (fleet-api.prd.cn.vn.cloud.tesla.cn) and is fully supported by the
# underlying tesla-fleet-api library — the official integration filtered it
# out, this fork re-enables it.
REGION_SERVERS: dict[str, str] = dict(SERVERS)
REGIONS = list(REGION_SERVERS)

LOGGER = logging.getLogger(__package__)

# China-region OAuth endpoints. Mainland China accounts must authenticate
# against auth.tesla.cn (the international fleet-auth.prd.vn.cloud.tesla.com
# does not recognize China-registered client_ids -> "Client authentication
# failed"). Verified via auth.tesla.cn/oauth2/v3/thirdparty/.well-known/
# openid-configuration.
AUTHORIZE_URL = "https://auth.tesla.cn/oauth2/v3/authorize"
TOKEN_URL = "https://auth.tesla.cn/oauth2/v3/token"

SCOPES = [
    Scope.OPENID,
    Scope.OFFLINE_ACCESS,
    Scope.VEHICLE_DEVICE_DATA,
    Scope.VEHICLE_LOCATION,
    Scope.VEHICLE_CMDS,
    Scope.VEHICLE_CHARGING_CMDS,
    Scope.ENERGY_DEVICE_DATA,
    Scope.ENERGY_CMDS,
]

ENERGY_HISTORY_FIELDS = [
    "solar_energy_exported",
    "generator_energy_exported",
    "grid_energy_imported",
    "grid_services_energy_imported",
    "grid_services_energy_exported",
    "grid_energy_exported_from_solar",
    "grid_energy_exported_from_generator",
    "grid_energy_exported_from_battery",
    "battery_energy_exported",
    "battery_energy_imported_from_grid",
    "battery_energy_imported_from_solar",
    "battery_energy_imported_from_generator",
    "consumer_energy_imported_from_grid",
    "consumer_energy_imported_from_solar",
    "consumer_energy_imported_from_battery",
    "consumer_energy_imported_from_generator",
    "total_home_usage",
    "total_battery_charge",
    "total_battery_discharge",
    "total_solar_generation",
    "total_grid_energy_exported",
]


class TeslaFleetState(StrEnum):
    """Teslemetry Vehicle States."""

    ONLINE = "online"
    ASLEEP = "asleep"
    OFFLINE = "offline"


class TeslaFleetClimateSide(StrEnum):
    """Tesla Fleet Climate Keeper Modes."""

    DRIVER = "driver_temp"
    PASSENGER = "passenger_temp"
