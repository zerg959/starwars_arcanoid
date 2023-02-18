import os.path

import pygame

MW_SIZE_X: int = 500  # Main window size (x).
MW_SIZE_Y: int = 500  # Main window size (y).
back: tuple = (200, 255, 255)  # background color.
mw = pygame.display.set_mode((500, 500))  # Main window object.


# class Area from pygame.Rect
class Area:
    """Rectangle sprite background for sprite."""
    def __init__(self, x: int = 0, y: int = 0,
                 width: int = 10, height: int = 10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    # color func
    def color(self, new_color):
        self.fill_color: tuple = new_color

    def fill(self):
        """Fill background area by color."""
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        """Check points of intersections."""
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        """Check if coordinates of two rects intersected."""
        return self.rect.colliderect(rect)


class Picture(Area):
    """Picture rectangle objects class."""
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(os.path.join(
            'sprites', filename)).convert_alpha()

# draw picture in main window
    def draw(self):
        """Draw Picture objects in main window"""
        mw.blit(self.image, (self.rect.x, self.rect.y))
