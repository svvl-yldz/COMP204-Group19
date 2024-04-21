import lib.stddraw as stddraw  # stddraw is used as a basic graphics library
from lib.color import Color  # used for coloring the tile and the number on it
import random as rd
# Class used for modeling numbered tiles as in 2048
class Tile: 
   # Class attributes shared among all Tile objects
   # ---------------------------------------------------------------------------
   # the value of the boundary thickness (for the boxes around the tiles)
   boundary_thickness = 0.004
   # font family and size used for displaying the tile number
   font_family, font_size = "Arial", 14

   # Constructor that creates a tile with 2 as the number on it
   def __init__(self):
      # set the number on the tile
      if(rd.random() < 0.5 ):
         self.number = 2
      else:
         self.number = 4
      if(self.number == 2):
         self.background_color = Color(151, 178, 199)  # background (tile) color
         self.foreground_color = Color(0, 100, 200)  # foreground (number) color
      elif(self.number == 4):
         self.background_color = Color(77,78,19)
         self.foreground_color = Color(207,122,122)
      elif(self.number == 8):
         self.background_color = Color(53,28,117)
         self.foreground_color = Color(207,122,122)

      else:
         self.background_color = Color(53,28,117)
         self.foreground_color = Color(207,122,122)
      # set the colors of the tile

      self.box_color = Color(78,240,7) # box (boundary) color
   def draw(self, position, length = 1):
      # draw the tile as a filled square
      stddraw.setPenColor(self.background_color)
      stddraw.filledSquare(position.x, position.y, length / 2)
      # draw the bounding box around the tile as a square
      stddraw.setPenColor(self.box_color)
      stddraw.setPenRadius(Tile.boundary_thickness)
      stddraw.square(position.x, position.y, length / 2)
      stddraw.setPenRadius()  # reset the pen radius to its default value
      # draw the number on the tile
      stddraw.setPenColor(self.foreground_color)
      stddraw.setFontFamily(Tile.font_family)
      stddraw.setFontSize(Tile.font_size)
      stddraw.text(position.x, position.y, str(self.number))
   def merge_matches(self, tile):
      if self.number == tile.number and self.number < 2048:
         self.number *= 2  # Double the number on the current tile
         tile.number = None  # Remove the other tile
         return self.number  # Return the merged number
      else:
         return 0  # Return 0 if no merge occurred

   def merge_tiles(tile_matrix, score):
      rows, cols = len(tile_matrix), len(tile_matrix[0])

      for col in range(cols):
         for row in range(rows - 1):
            current_tile = tile_matrix[row][col]

            if current_tile:
               next_tile = tile_matrix[row + 1][col]

               if next_tile and current_tile.number == next_tile.number:
                  score += current_tile.merge_matches(next_tile)
                  tile_matrix[row + 1][col] = None

         # Shift tiles downwards after merging
         shifted_tiles = [tile for tile in tile_matrix[:, col] if tile is not None]
         tile_matrix[:, col] = shifted_tiles + [None] * (rows - len(shifted_tiles))

      return score