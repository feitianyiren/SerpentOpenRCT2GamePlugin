from lib.game_api import GameAPI

from lib.game_frame import GameFrame

import time


class OpenRCT2API(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)

    class MainMenu:
        scenario_tab_name_mapping = {
            "RollerCoaster Tycoon": "MAIN_MENU_SCENARIO_TAB_RCT",
            "Corkscrew Follies": "MAIN_MENU_SCENARIO_TAB_RCT_CF",
            "Loopy Landscapes": "MAIN_MENU_SCENARIO_TAB_RCT_LL",
            "RollerCoaster Tycoon 2": "MAIN_MENU_SCENARIO_TAB_RCT2",
            "Wacky Worlds": "MAIN_MENU_SCENARIO_TAB_RCT2_WW",
            "Time Twister": "MAIN_MENU_SCENARIO_TAB_RCT2_TT",
            "Real Parks": "MAIN_MENU_SCENARIO_TAB_RCT_RP",
            "Other Parks": "MAIN_MENU_SCENARIO_TAB_RCT_OP"
        }

        @classmethod
        def open_scenario(cls, game_frame, scenario_tab_name="RollerCoaster Tycoon", scenario_name="Forest Frontiers", lastest_frame_func=None):
            cls.click_new_game()
            time.sleep(0.5)
            cls.click_scenario_tab(scenario_tab_name)
            time.sleep(0.5)

            latest_game_frame = lastest_frame_func()

            offset_x = game_frame.offset_x
            offset_y = game_frame.offset_y

            game_frame = GameFrame(latest_game_frame.frame[
                offset_y:offset_y + game_frame.frame.shape[0],
                offset_x:offset_x + game_frame.frame.shape[1],
            ], offset_x=offset_x, offset_y=offset_y)

            cls.click_scenario(scenario_name, game_frame)

        @classmethod
        def click_new_game(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_NEW_GAME"
            )

        @classmethod
        def click_load_game(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_LOAD_GAME"
            )

        @classmethod
        def click_multiplayer(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_MULTIPLAYER"
            )

        @classmethod
        def click_game_tools(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_GAME_TOOLS"
            )

        @classmethod
        def click_quit(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_QUIT"
            )

        @classmethod
        def click_scenario_tab(cls, scenario_tab_name):
            screen_region_name = cls.scenario_tab_name_mapping.get(scenario_tab_name)

            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region=screen_region_name
            )

        @classmethod
        def click_scenario(cls, scenario_name, game_frame):
            clicked = OpenRCT2API.instance.input_controller.click_string(
                scenario_name,
                game_frame,
                fuzziness=2,
                ocr_preset=OpenRCT2API.instance.game.ocr_presets.get("SCENARIO_TEXT")
            )

    class Game:
        @classmethod
        def click_pause(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="GAME_PAUSE_BUTTON",
                game=OpenRCT2API.instance.game
            )

        @classmethod
        def click_speed(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="GAME_SPEED_BUTTON",
                game=OpenRCT2API.instance.game
            )

        @classmethod
        def click_floppy(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="GAME_FLOPPY_BUTTON",
                game=OpenRCT2API.instance.game
            )