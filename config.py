import os
from discord import Intents  # type: ignore

CONFIG_DICT = {
    "prefix": ".",
    "intents": Intents.all(),
    "owners": {
        977036206179233862,
        352190010998390796,
        978402974667800666,
        744806691396124673,
        863914425445908490,
        915350867438338058,
    },
    "token": os.environ.get("DISCORD_TOKEN", ""),
    "rival_api": os.environ.get("RIVAL_API_KEY", ""),
    "domain": "https://greed.wtf",
}


CHANCES = {
    "roll": {"percentage": 50.0, "total": 100.0},
    "coinflip": {"percentage": 60.0, "total": 100.0},
    "gamble": {"percentage": 20.0, "total": 100.0},
    "supergamble": {"percentage": 21.0, "total": 1000.0},
}


class Authorization:
    class Instagram:
        session_id = ""
        csrf_token = ""

    class LastFM:
        api_key = os.environ.get("LASTFM_API_KEY", "ac82ef7e341d3e9dd71c2e7f5625b6a8")
        api_secret = os.environ.get("LASTFM_API_SECRET", "1008d94193db951eae45e3ebf9a9a034")
        pending_auth = {}
        cb_url = "https://api.greed.rocks/callback"

    class Outages:
        api_key = os.environ.get("OUTAGES_API_KEY", "greed_outages_api_key_2024_because_im_a_boss_85_2007_noscopes")
