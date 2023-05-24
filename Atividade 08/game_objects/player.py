import pygame

class Player:
  def __init__(self, x: int, y: int) -> None:
    self.__x = x
    self.__y = y

  __x, __y = 0, 0
  __speed = 10
  __is_facing_right = True
  is_on_the_ground = True

  __sprite_sheet = pygame.image.load("assets/player.png")
  __animation_frame = 0
  __animation_time = 0

  def update(self, dt: int, pressed_keys):
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
      self.__is_facing_right = False
      self.__x -= self.__speed * dt/60
      self.__walking_animation(dt)

    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
      self.__is_facing_right = True
      self.__x += self.__speed * dt/60
      self.__walking_animation(dt)

    else:
      if self.is_on_the_ground:
        self.__animation_frame = 0
      else:
        self.__animation_frame = 3

  def __walking_animation(self, dt: int):
    self.__animation_time += dt
    if self.__animation_time > 2 * 60:
      self.__animation_time = 0
      self.__animation_frame += 1
      if self.__animation_frame > 2:
        self.__animation_frame = 1

  def draw(self, screen: pygame.Surface):
    screen.blit(
      source = self.__sprite_sheet,
      dest = (self.__x, self.__y),
      area = (
        16 * self.__animation_frame,
        0 if self.__is_facing_right else 16,
        16,
        16
      )
    )
