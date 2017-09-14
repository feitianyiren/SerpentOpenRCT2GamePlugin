from lib.game import Game

from .api.api import OpenRCT2API

from lib.utilities import Singleton


class SerpentOpenRCT2Game(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "executable"

        kwargs["window_name"] = "OpenRCT2"

        kwargs["executable_path"] = "openrct2"

        super().__init__(**kwargs)

        self.api_class = OpenRCT2API
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "MAIN_MENU_NEW_GAME": (626, 348, 708, 428),
            "MAIN_MENU_LOAD_GAME": (626, 429, 708, 510),
            "MAIN_MENU_MULTIPLAYER": (626, 511, 708, 592),
            "MAIN_MENU_GAME_TOOLS": (626, 593, 708, 674),
            "MAIN_MENU_QUIT": (704, 983, 768, 1023),
            "GAME_PAUSE_BUTTON": (0, 0, 27, 30),
            "GAME_SPEED_BUTTON": (0, 30, 27, 60),
            "GAME_FLOPPY_BUTTON": (0, 60, 27, 90)
        }

        return regions
