from typing import Dict

import pygame
from pygame.locals import *


class PGTutorial03(object):

    def __init__(self):

        self.winsize = (1440,810)

        self.background_drawn = False

        pygame.init()
        pygame.display.set_caption("PyGame Tutorial 3")
        self.win = pygame.display.set_mode(self.winsize)

        self.graphics = self.__init_graphics()

        self.spaceship_width = self.graphics["spaceship"].get_width()

        # start the spaceship just off the left edge
        self.starting_point_x = 0 - self.spaceship_width
        self.starting_point_y = (self.winsize[1]/2) - (self.graphics["spaceship"].get_height()/2)
        
        # initialise spaceship coordinates
        self.spaceship_pos = [self.starting_point_x, self.starting_point_y]

        # speeds are pixels per event loop interval
        self.h_speed_ppms = 0.1
        self.v_speed_ppms = 0.2

        self.prev_ss_rect = None
        
        self.run = True
        self.clock = pygame.time.Clock()
        self.max_fps = 60
        self.ellapsed_ms = 0

        # this causes the key event to be fired at stated
        # intervals if user holds key down
        pygame.key.set_repeat(1000 / self.max_fps)            

        self.__event_loop()


    def __init_graphics(self) -> Dict:

        '''
        Creates a dictionary of all the 
        images used by the game.
        '''

        # convert_alpha is needed for graphics with transparency
        graphics = {"background": pygame.Surface.convert(pygame.image.load('background2.jpg')),
                    "spaceship": pygame.Surface.convert_alpha(pygame.image.load('spaceshipsmall.png')),
                    "flyingsaucer": pygame.Surface.convert_alpha(pygame.image.load('flyingsaucersmall.png'))}

        return graphics
    

    def __draw_window(self) -> None:

        """
        Blits the graphics
        Adds rects from blits to list
        Redraws updated rects
        """

        # list for areas affected by this draw
        rects = []
            
        # if the spaceship has already been drawn
        # add its previous position rectangle
        # to the list so it is overdrawn
        if self.prev_ss_rect != None:
            rects.append(self.prev_ss_rect)

        # blit the background and retrieve its rect
        # which will be the whole window
        bgrect = self.win.blit(self.graphics["background"], (0,0))

        # If the background hasn't yet been drawn add
        # its rect to the list and update the drawn flag.
        # If we don't do this only the rects from other blits will be drawn.
        if self.background_drawn == False:
            
            rects.append(bgrect)
            self.background_drawn = True

        # blit the spaceship, pick up the rect it is drawn in
        # and add it to the list
        ss_rect = self.win.blit(self.graphics["spaceship"], (self.spaceship_pos[0], self.spaceship_pos[1]))
        rects.append(ss_rect)
        
        # blit the flying saucer and add its rect to the list
        rects.append(self.win.blit(self.graphics["flyingsaucer"], (1200,394)))

        # without this nothing will happen!
        # rects argument ensures only necessary areas are redrawn
        pygame.display.update(rects)

        # update the previous rect to the current 
        # for use on next loop
        self.prev_ss_rect = ss_rect


    def __handle_keydown(self, key) -> None:

        """
        Move spaceship vertical position when arrow keys pressed
        """

        match key:
            case pygame.locals.K_UP:
                pixels_to_move = self.__pixels_to_move(self.ellapsed_ms, 
                                                       self.v_speed_ppms)
                self.spaceship_pos[1] -= pixels_to_move

            case pygame.locals.K_DOWN:
                pixels_to_move = self.__pixels_to_move(self.ellapsed_ms, 
                                                       self.v_speed_ppms)
                self.spaceship_pos[1] += pixels_to_move

            case pygame.locals.K_SPACE:

                # for future use
                
                ...


    def __pixels_to_move(self, ms:int, ppms:int) -> int:

        return round(ms * ppms)


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

                        if event.key in(K_UP, K_DOWN):
                            self.__handle_keydown(event.key)
                           
            # move spaceship horizontally
            pixels_to_move = self.__pixels_to_move(self.ellapsed_ms, 
                                                   self.h_speed_ppms)
            self.spaceship_pos[0] += pixels_to_move

            self.__draw_window()

            self.ellapsed_ms = self.clock.tick(self.max_fps)


game = PGTutorial03()