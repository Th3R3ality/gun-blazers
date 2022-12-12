import math, pygame

def atan2d(a, b) -> float:
    return math.degrees(math.atan2(b[0] - a[0], b[1] - a[1]))

def dist2d(a, b):
    return math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))

def point_in_circle(a, b, br):
        if dist2d(a, b) < br:
            return True
        return False

class debug_text():
    def __init__(self) -> None:
        self.strings = []
        self.permas = []
        self.font = pygame.font.SysFont("Arial", 18)
    
    def add(self, string, color, pos = (0,0)):
        self.strings.append((self.font.render(str(string), 1, color), pos))
    
    def add_perma(self, string, color, pos = (0,0)):
        self.permas.append((self.font.render(str(string), 1, color), pos))

    def draw_flush(self, surface):
        count = 0
        for s in self.permas:
            pos = (10, 18 * count)
            if s[1] != (0,0):
                pos = s[1]
            surface.blit(s[0], pos)
            count += 1
        for s in self.strings:
            pos = (10, 18 * count)
            if s[1] != (0,0):
                pos = s[1]
                count -= 1
            surface.blit(s[0], pos)
            count += 1
        
        self.strings = []