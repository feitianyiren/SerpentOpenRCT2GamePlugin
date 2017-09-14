from lib.game_api import GameAPI


class OpenRCT2API(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)

    class MainMenu:
        @classmethod
        def click_new_game(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_NEW_GAME",
                game=OpenRCT2API.instance.game
            )

        @classmethod
        def click_load_game(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_LOAD_GAME",
                game=OpenRCT2API.instance.game
            )

        @classmethod
        def click_multiplayer(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_MULTIPLAYER",
                game=OpenRCT2API.instance.game
            )

        @classmethod
        def click_game_tools(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_GAME_TOOLS",
                game=OpenRCT2API.instance.game
            )

        @classmethod
        def click_quit(cls):
            OpenRCT2API.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_QUIT",
                game=OpenRCT2API.instance.game
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