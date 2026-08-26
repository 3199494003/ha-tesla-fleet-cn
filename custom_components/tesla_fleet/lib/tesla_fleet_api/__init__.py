"""Tesla Fleet API (vendored, China-region fork).

Trimmed top-level exports: only what the HA tesla_fleet integration needs is
imported eagerly, avoiding pulling in Teslemetry/Tessie/Bluetooth classes.
The token-exchange endpoints in tesla/fleet.py and tesla/oauth.py are patched
to use auth.tesla.cn for the cn region.
"""

__author__ = "hello@teslemetry.com"
__version__ = "1.5.0-cn"

from tesla_fleet_api.const import Region, Scope, is_valid_region
from tesla_fleet_api.tesla.fleet import TeslaFleetApi

__all__ = [
    "TeslaFleetApi",
    "Region",
    "Scope",
    "is_valid_region",
]
