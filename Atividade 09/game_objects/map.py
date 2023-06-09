import pygame
from game_objects.tileset import Tileset
from game_objects.camera import Camera

class Map:
  def __init__(self, map_layers: list, width: int, tileset: Tileset) -> None:
    self.__map_layers = map_layers
    self.__width = width
    self.__tileset = tileset

    for layer in self.__map_layers:
      for tile_number, tile in enumerate(layer):
        if self.__tileset.is_tile_collisionable(tile):
          rect = pygame.Rect(
            (tile_number % self.__width) * self.__tileset.tile_size,
            (tile_number // self.__width) * self.__tileset.tile_size,
            self.__tileset.tile_size,
            self.__tileset.tile_size,
          )
          if rect not in self.colliders:
            self.colliders.append(rect)

  __map_layers = []
  __tileset = Tileset
  __width = 0
  colliders = []

  def draw(self, screen: pygame.Surface, camera: Camera):
    for layer in self.__map_layers:
      for tile_number, tile in enumerate(layer):
        if tile == -1: continue

        screen.blit(
          source = self.__tileset.image,
          dest = (
            (tile_number % self.__width) * self.__tileset.tile_size - camera.x_offset,
            (tile_number // self.__width) * self.__tileset.tile_size - camera.y_offset,
          ),
          area = (
            (tile % self.__tileset.tiles_in_a_row) * self.__tileset.tile_size,
            (tile // self.__tileset.tiles_in_a_row) * self.__tileset.tile_size,
            self.__tileset.tile_size,
            self.__tileset.tile_size,
          ),
        )
