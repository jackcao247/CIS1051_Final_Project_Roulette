import pygame
from roulette import Wheel, Static
from Settings import * 
from random import randrange

class SpinWheel:
    def __init__(self):
        pygame.init()
        self.game_width, self.game_height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.game_width, self.game_height))
        pygame.display.set_caption(TITLE)
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True

    def new(self, show_menu=True):
        self.all_sprites = pygame.sprite.Group()
        self.wheel = Wheel(self, self.game_width // 2, self.game_height // 2, "C:\\Users\\Bao Cao\\Documents\\py project\\pyGame\\pygame-1.9.6\\Roulette\\Pictures\\main-qimg-4228184a3c2700364fee805dbaa2cced-lq.png", scale=3)
        self.all_sprites.add(self.wheel)
        self.indicator = Static(self, self.game_width - 960, 80, "C:\\Users\\Bao Cao\\Documents\\py project\\pyGame\\pygame-1.9.6\\Roulette\\Pictures\\red-arrow-down-icon-png-30.png", scale=0.2)
        self.all_sprites.add(self.indicator)
        self.player_action = "waiting"
        self.spin_start_time = 0
        if show_menu:
            self.show_start_screen()
        self.run()

    def run(self):
        while self.playing:
            try:
                if self.running:
                    self.clock.tick(FRAME_PER_SEC)
                    self.events()
                    self.update()
                    self.draw()
            except Exception as e:
                print(e)

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if self.wheel.spin_velocity <= 0:
                if event.type == pygame.MOUSEBUTTONDOWN and self.player_action == "waiting":
                    self.player_action = "clicking"
                    self.mouse_down_x, self.mouse_down_y = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP and self.player_action == "clicking":
                    self.mouse_up_x, self.mouse_up_y = pygame.mouse.get_pos()
                    spin_time = (pygame.time.get_ticks() - self.spin_start_time) + 0.5
                    spin_distance = ((self.mouse_up_y - self.mouse_down_y) ** 2 + (self.mouse_up_x - self.mouse_down_x) ** 2) ** 2
                    if spin_distance / spin_time <= 30:
                        self.wheel.spin_velocity = randrange(30, 50)
                    else:
                        self.wheel.spin_velocity = spin_distance / spin_time
                    self.player_action = "waiting"

                if event.type == pygame.MOUSEMOTION and self.player_action == "clicking":
                    self.spin_start_time = pygame.time.get_ticks()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                    self.playing = False

    def draw(self):
        if self.running and self.playing:
            self.screen.fill(WHITE)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def listen_for_key(self, start=True):
        waiting = True
        while waiting:
            self.clock.tick(FRAME_PER_SEC)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if start:
                        self.start_time = pygame.time.get_ticks()
                        waiting = False
                        self.running = True

    def show_start_screen(self):
        self.draw_text("Click to spin the wheel.", 18, WHITE, self.game_width // 2, self.game_height // 3)
        self.draw_text("Press any key to begin.", 18, WHITE, self.game_width // 2, self.game_height // 2)
        pygame.display.flip()
        self.listen_for_key()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(FONT_NAME, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

if __name__ == "__main__":
    g = SpinWheel()
    g.new()
    pygame.quit()
