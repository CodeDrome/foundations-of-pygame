from typing import Tuple

import pygame
from pygame.locals import *


class PGTutorial01(object):

    def __init__(self):

        # initialise PyGame modules
        # pygame.init()
        pygame.display.set_caption("PyGame Tutorial 1")
        # create pygame.Surface object with specified properties
        self._win = pygame.display.set_mode(size=(600,400))

        # used to keep the event loop looping
        self._run = True
        # used to wait between event loop iterations
        self._clock = pygame.time.Clock()
        # length of time between event loop iterations
        self._interval_ms = 60

        # start the event loop
        self.__event_loop()


    # EVENT HANDLER FUNCTIONS
    # to be called within the event loop

    def __handle_left_mousebuttondown(self, pos:Tuple) -> None:

        print(f"Left mouse clicked at {pos}")


    def __handle_right_mousebuttondown(self, pos:Tuple) -> None:

        print(f"Right mouse clicked at {pos}")


    def __handle_middle_mousebuttondown(self, pos:Tuple) -> None:

        print(f"Middle mouse clicked at {pos}")


    def __handle_mouse_wheel(self, event) -> None:

        # event.y = 1 for scroll up
        # event.y = -1 for scroll down
        print(f"Mouse wheel turned {event.y}")


    def __handle_arrow_key(self, key) -> None:

        dir = ""

        match key:
            case pygame.locals.K_LEFT:
                dir = "left"
            case pygame.locals.K_RIGHT:
                dir = "right"
            case pygame.locals.K_UP:
                dir = "up"
            case pygame.locals.K_DOWN:
                dir = "down"

        print(f"{dir} arrow key pressed ")


    # EVENT LOOP

    def __event_loop(self) -> None:

        """
        Checks event queue periodically based
        on value of self.interval_ms.
        Calls relevant event handler functions
        """

        while self._run:

            for event in pygame.event.get():

                match event.type:

                    case pygame.locals.QUIT:

                        self._run = False
                        pygame.quit()
                        return

                    case pygame.locals.KEYDOWN:

                        if event.key in(K_LEFT,K_RIGHT,K_UP,K_DOWN):
                            self.__handle_arrow_key(event.key)
                                                    
                    case pygame.locals.MOUSEBUTTONDOWN:

                        match event.button:
                            case 1:
                                self.__handle_left_mousebuttondown(event.pos)
                            case 3:
                                self.__handle_right_mousebuttondown(event.pos)
                            case 2:
                                self.__handle_middle_mousebuttondown(event.pos)
                
                    case pygame.locals.MOUSEWHEEL:
                
                        self.__handle_mouse_wheel(event)

            self._clock.tick(self._interval_ms)


game = PGTutorial01()