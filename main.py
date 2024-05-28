import pygame

WIDTH, HEIGHT = 500, 500
FPS = 60


class Button:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled

    def draw(self):
        btn_text = mid_font.render(self.text, True, 'black')
        btn_rct = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))
        if self.enabled:
            if self.check_click():
                pygame.draw.rect(screen, 'dark gray', btn_rct, 0, 5)
            else:
                pygame.draw.rect(screen, 'light gray', btn_rct, 0, 5)
        else:
            pygame.draw.rect(screen, 'black', btn_rct, 0, 5)

        pygame.draw.rect(screen, 'black', btn_rct, 2, 5)

        screen.blit(btn_text, (self.x_pos + 5, self.y_pos + 5))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_clicked = pygame.mouse.get_pressed()[0]
        btn_rct = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))
        if left_clicked and btn_rct.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
mid_font = pygame.font.Font('calibri-regular.ttf', 16)
pygame.display.set_caption('Buttons')
button1_enabled = True
new_pressed = True

button1 = Button('click me!', 10, 10, button1_enabled)
button2 = Button('click me too!', 10, 40, True)
button3 = Button('click me three!', 10, 70, True)

running = True
while running:
    screen.fill('white')
    clock.tick(60)

    button1.draw()
    button2.draw()
    button3.draw()

    if pygame.mouse.get_pressed()[0] and new_pressed:
        new_pressed = False
        if button3.check_click():
            if button1.enabled:
                button1.enabled = False
            else:
                button1.enabled = True

    if not pygame.mouse.get_pressed()[0] and not new_pressed:
        new_pressed = True

    if button2.check_click():
        button_text = mid_font.render('Clicked Button Two!', True, 'black')
        screen.blit(button_text, (200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
