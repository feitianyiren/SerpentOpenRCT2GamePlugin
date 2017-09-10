from lib.game import Game

from .api import api


class SerpentOpenRCT2Game(Game):

    def __init__(self, **kwargs):
        kwargs["platform"] = "executable"

        kwargs["window_name"] = "OpenRCT2"
        
        kwargs["executable_path"] = "openrct2"

        super().__init__(**kwargs)

        self.api = api

    @property
    def screen_regions(self):
        regions = {
            "MAIN_MENU_NEW_GAME": (626, 348, 708, 428),
            "MAIN_MENU_LOAD_GAME": (626, 429, 708, 510),
            "MAIN_MENU_MULTIPLAYER": (626, 511, 708, 592),
            "MAIN_MENU_GAME_TOOLS": (626, 593, 708, 674),
            "MAIN_MENU_QUIT": (704, 983, 768, 1023)
        }

        return regions
