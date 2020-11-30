#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: November 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage


def game_scene():
    # this function is the main game game_scene

   # image banks for CirucuitPython
   image_bank_bankground = stage.Bank.from_bmp16("space_aliens_background.bmp")
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, 10,8)

   # create a stage for the background to show up on
   #   and set the frame rate for 60fps
   game = stage.Stage(ugame.display, 60)
   # set layers of all sprites, items show up in order
   game.layers = [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()

    # repeat forever, game loop
   while True:
       pass # just a placeholder for now

if __name__ == "__main__":
    game_scene()
