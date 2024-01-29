from tkinter import messagebox
import pygame

pygame.init()
screen = pygame.display.set_mode((700, 500))
bg1 = pygame.image.load('image/imagem1.jpg')
bg2 = pygame.image.load('image/imagem2.jpg')
bg3 = pygame.image.load('image/imagem4.jpg')
bg4 = pygame.image.load('image/imagem5.jpg')
hit_s = pygame.mixer.Sound('sound/hit_sound.mp3')
pygame.mixer.Sound.set_volume(hit_s, 0.05)
bg_s = pygame.mixer.music.load('sound/m_theme.mp3')
bg = [bg1, bg2,bg3,bg4]
font = pygame.font.SysFont(None, 30)
def message(text, color, x=10, y=10):
    msg = font.render(text, True, color)
    screen.blit(msg, [x,y])
def s_message(score1, score2):
    result = messagebox.askquestion('Достигнут придел', 'Вы хотите продолжить?')
    if result == 'yes':
        score1 = 0
        print(10)
        loop()
        score2 = 0
        return score1, score2
    if result == 'no':
        messagebox.showinfo('Сделан выбор', 'Спасибо за игру!')
        exit(0)
def loop():
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)
    green = (0, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    ph = 75
    pw = 20
    ps = 10
    p1p = [30, 250]
    p2p = [650, 250]
    bp = [350, 250]
    center = (350, 250)
    br = 15
    bs = [6, 10]
    score1 = 0
    score2 = 0
    gameclose = False
    fps = pygame.time.Clock()


    while not gameclose:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameclose = True


        key = pygame.key.get_pressed()
        if key[pygame.K_w] and p1p[1] > 0:
            p1p = [p1p[0], p1p[1] - ps]
        if key[pygame.K_s] and p1p[1] < 500 - ph:
            p1p = [p1p[0], p1p[1] + ps]

        if key[pygame.K_UP] and p2p[1] > 0:
            p2p = [p2p[0], p2p[1] - ps]
        if key[pygame.K_DOWN] and p2p[1] < 500 - ph:
            p2p = [p2p[0], p2p[1] + ps]
        bp[1] += bs[1]
        bp[0] -= bs[0]
        if bp[1]>=500-br or bp[1]<= 0+br:
            bs[1]*=-1
            hit_s.play()

        if (bp[0]<=p1p[0]+pw and bp[1]>=p1p[1] and bp[1]<=p1p[1]+ph) or (bp[0]>=p2p[0]-pw and bp[1]>=p2p[1] and bp[1]<=p2p[1]+ph):
            bs[0]*=-1
            hit_s.play()
        if bp[0]<0:
            score2 += 1
            bp = list(center)
        if bp[0]>700:
            score1 += 1
            bp = list(center)
        if score1==5 or score2==5:
            s_message(score1, score2)

        screen.fill(white)
        screen.blit(bg[score1%4], (0,0))
        message(str(score1), black) # Счет первого игрока
        message(str(score2), black, 680) # Счет второго игрока
        pygame.draw.rect(screen, black, [p1p[0], p1p[1], pw, ph])
        pygame.draw.rect(screen, black, [p2p[0], p2p[1], pw, ph])
        pygame.draw.circle(screen, green, [bp[0], bp[1]], br)
        pygame.display.update()
        fps.tick(30)
    pygame.quit()
    quit()
loop()