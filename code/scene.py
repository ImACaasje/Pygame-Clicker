from globals import *
from sprites import Sprite, Clickable_Sprite
from data import texture_data


class Scene:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.textures = self.gen_textures()
        # groups
        self.all_sprites = pygame.sprite.Group()
        self.setup()

    @staticmethod
    def gen_textures() -> dict:
        textures = {}
        for name, data in texture_data.items():
            textures[name] = pygame.transform.scale(pygame.image.load(data['filepath']).convert_alpha(), (data['size']))
        return textures

    def setup(self):
        Clickable_Sprite((200, SCREENHEIGHT / 2), self.textures['cookie'], self.all_sprites)

    def run(self, dt):
        self.all_sprites.update()
        self.display.fill('lightblue')
        self.all_sprites.draw(self.display)
