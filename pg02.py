from typing import Tuple

import math

import pygame
from pygame.locals import *


class PGTutorial02(object):

    def __init__(self) -> None:   

        # to be set to True by code making changes requiring redraw
        self.redraw = False

        self.winsize = (560,400)

        self.circle_coords = None

        pygame.init()        
        self.font = pygame.font.SysFont('freesans', 26)
        pygame.display.set_caption("PyGame Tutorial 2")
        self.win = pygame.display.set_mode(self.winsize)

        self.run = True
        self.clock = pygame.time.Clock()
        self.interval_ms = 60

        self.__draw_window()

        self.__event_loop()


    def __draw_window(self) -> None:

        '''
        Called once in __init__ 
        and by __event_loop when needed
        '''

        # this is just to demonstrate that __draw_window 
        # is only called when the game starts or when 
        # redraw is True, not on every iteration of the event loop
        print("__draw_window")

        # colour is tuple of RGB decimal values 0-255
        # note: NOT hexadecimal
        self.win.fill((0,0,32))

        # TEXT
        text = self.font.render("PyGame Tutorial 2", True, (255,128,0))
        print(text)
        text_size = self.font.size("PyGame Tutorial 2")
        print(text_size)
        self.win.blit(text, ((self.winsize[0]/2)-(text_size[0]/2), 5))

        # RECT
        # rect argument is (top, left, width, height)
        # outline only if width > 0
        pygame.draw.rect(self.win, "yellow", rect=(10,50,100,25), width=0)

        # POLYGON
        # points argument is 3 or more tuples of (x,y) coordinates
        # filled if width=0
        pygame.draw.polygon(self.win, "yellow", points=((120,50),(220,50),(170,75)), width=1)

        # ELLIPSE
        # rect argument is (top, left, width, height)
        # outline only if width > 0
        pygame.draw.ellipse(self.win, "yellow", rect=(230,50,100,25), width=0)

        # ARC
        # rect argument is (top, left, width, height)
        # angles in radians, anticlockwise from 3 o'clock
        pygame.draw.arc(self.win, "yellow", rect=(340,50,100,25), start_angle=0, stop_angle=math.pi, width=1)

        # LINE
        pygame.draw.line(self.win, "yellow", start_pos=(450,50), end_pos=(550, 75), width=1)

        # circle_coords is set only when user left-clicks
        if self.circle_coords != None:
            
            pygame.draw.circle(self.win, "steelblue1", self.circle_coords, 32)
            self.circle_coords = None

        pygame.display.update()

        # must reset redraw to prevent unnecessary calls
        # to this function every time event loop loops
        self.redraw = False


    # EVENT HANDLER FUNCTIONS

    def __handle_left_mousebuttondown(self, pos:Tuple) -> None:

        self.circle_coords = pos
        # this causes the event loop to call __draw_window
        self.redraw = True        

    def __handle_right_mousebuttondown(self, pos:Tuple) -> None:

        print(f"Right mouse clicked at {pos}")

    def __handle_middle_mousebuttondown(self, pos:Tuple) -> None:

        print(f"Middle mouse clicked at {pos}")

    def __handle_mouse_wheel(self, event) -> None:

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
        on value of self.interval_ms
        """

        while self.run:

            for event in pygame.event.get():

                match event.type:

                    case pygame.locals.QUIT:

                        self.run = False
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

            # only call __draw_window if any of the event 
            # handlers have set redraw to True
            if self.redraw == True:
                self.__draw_window()

            self.clock.tick(self.interval_ms)


game = PGTutorial02()