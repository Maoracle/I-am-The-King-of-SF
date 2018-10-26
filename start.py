# 游戏开始界面
screen.fill(WHITE)
font = pygame.font.Font(None, 32)
text = '''
In this game you are a SF,
trying to survive a course in
self-defense against enemies, 
click mouse or press any button to 
start the game.'''
lines = text.strip().splitlines()
lines_height = len(lines) * font.get_linesize()
lines_center, lines_top = screen.get_rect().center
lines_top -= lines_height // 2
start_image = pygame.image.load("images/sf0.png").convert()
r = start_image.get_rect()
lines_top += r.height // 2
r.midbottom = lines_center, lines_top - 20
screen.blit(start_image, r)
antialias = 1  # 对文本进行编辑

# 对文本每一行进行编辑
for line in lines:
    text = font.render(line.strip(), antialias, BLACK)
    r = text.get_rect()
    r.midtop = lines_center, lines_top
    screen.blit(text, r)
    lines_top += font.get_linesize()

for event in pygame.event.get():
    if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
        running = True

pygame.display.flip()
clock.tick(60)
