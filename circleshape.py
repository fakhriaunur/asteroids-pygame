import pygame

class CircleShape(pygame.sprite.Sprite):
    def __main__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
    
    def check_collision(self, other_obj):
        return (
            self.position.distance_to(other_obj.position)
            <= self.radius + other_obj.radius
        )