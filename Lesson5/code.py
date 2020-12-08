#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: December 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage

import constants

def game_scene():
    # this function is the main game game_scene

   # image banks for CircuitPython
   image_bank_bankground = stage.Bank.from_bmp16("space_aliens_background.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, 10,8)
   
   # a sprite that will be updated every frame
   ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

   # create a stage for the background to show up on
   #   and set the frame rate for 60fps
   game = stage.Stage(ugame.display, 60)
   # set layers of all sprites, items show up in order
   game.layers = [ship] + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()

    # repeat forever, game loop
   while True:
       # get user input
       keys = ugame.buttons.get_pressed()
       
       if keys & ugame.K_X:
           print("A")
       if keys & ugame.K_O:
           print("Start")
       if keys & ugame.K_START:
           print("A")
       if keys & ugame.K_SELECT:
           print("Select")
       if keys & ugame.K_RIGHT != 0:
           if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
               ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
           else:
               ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

       if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

       if keys & ugame.K_UP:
           pass
       if keys & ugame.K_DOWN:
           pass 
       # update game logic
       
       # redraw Sprite
       game.render_sprites([ship])
       game.tick() # wait until refresh rate finishes

if __name__ == "__main__":
    game_scene()
