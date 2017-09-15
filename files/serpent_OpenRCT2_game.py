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
            "MAIN_MENU_SCENARIO_TAB_RCT": (234, 148, 267, 239),
            "MAIN_MENU_SCENARIO_TAB_RCT_CF": (234, 239, 267, 330),
            "MAIN_MENU_SCENARIO_TAB_RCT_LL": (234, 330, 267, 421),
            "MAIN_MENU_SCENARIO_TAB_RCT2": (234, 421, 267, 512),
            "MAIN_MENU_SCENARIO_TAB_RCT2_WW": (234, 512, 267, 603),
            "MAIN_MENU_SCENARIO_TAB_RCT2_TT": (234, 603, 267, 694),
            "MAIN_MENU_SCENARIO_TAB_RCT_RP": (234, 694, 267, 785),
            "MAIN_MENU_SCENARIO_TAB_RCT_OP": (234, 785, 267, 876),
            "GAME_PAUSE_BUTTON": (0, 0, 27, 30),
            "GAME_SPEED_BUTTON": (0, 30, 27, 60),
            "GAME_FLOPPY_BUTTON": (0, 60, 27, 90)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SCENARIO_TEXT": {
                "extract": {
                    "gradient_size": 3,
                    "closing_size": 10
                },
                "perform": {
                    "scale": 16,
                    "order": 3,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
