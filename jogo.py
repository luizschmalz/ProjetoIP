

import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint

pg.init()
largura = 800
altura = 600
tela = pg.display.set_mode((largura, altura))
fundo = pg.image.load("fundo.jpg")
relogio = pg.time.Clock()
z = 0
w = 0
fonte = pg.font.SysFont('arial', 30, False, False)
pronto = False
crachas = 3
debuff = 0
rodando = True
musica_fundo = pg.mixer.music.load("musicafundo.mp3.mp3")
pg.mixer.music.play(-1)


class Cracha(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load("cracha.png"))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.y = randint(50, 550)
        self.rect.x = randint(50, 750)
        self.image = pg.transform.scale(self.image, (64*0.8, 64*0.8))
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.y = randint(50, 550)
        self.rect.x = randint(50, 750)



class Gota(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load("gotinha-1.png.png"))
        self.sprites.append(pg.image.load("gotinha-2.png.png"))
        self.sprites.append(pg.image.load("gotinha-3.png.png"))
        self.sprites.append(pg.image.load("gotinha-4.png.png"))
        self.sprites.append(pg.image.load("gotinha-5.png.png"))
        self.sprites.append(pg.image.load("gotinha-6.png.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.y = w
        self.rect.x = z
        self.image = pg.transform.scale(self.image, (64 * 2, 64 * 2))
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        self.atual += 1
        if self.atual >= 6:
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (64 * 2, 64 * 2))
        self.rect.y = w
        self.rect.x = z


class Reidograd(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load("reidograd-1.png.png"))
        self.sprites.append(pg.image.load("reidograd-2.png.png"))
        self.sprites.append(pg.image.load("reidograd-3.png.png"))
        self.sprites.append(pg.image.load("reidograd-4.png.png"))
        self.sprites.append(pg.image.load("reidograd-5.png.png"))
        self.sprites.append(pg.image.load("reidograd-6.png.png"))
        self.sprites.append(pg.image.load("reidograd-7.png.png"))
        self.sprites.append(pg.image.load("reidograd-8.png.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (64*1.5, 64*1.5))
        self.mask = pg.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = 400, 300

    def update(self):
        self.atual += 1
        if self.atual >= 8:
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (64 * 1.5, 64 * 1.5))
        if self.rect.topright[0] <= largura+30:
            self.rect.x += 10
        else:
            self.rect.x = 0
            self.rect.y = randint(50,600)

class Marmita(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load('almirante.png'))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = randint(50,750)
        self.rect.y = randint(50,600)
        self.mask = pg.mask.from_surface(self.image)



cracha = Cracha()
rei = Reidograd()
gota = Gota()
marmita = Marmita()
sprites = pg.sprite.Group()
sprites.add(rei)
sprites.add(cracha)
sprites.add(gota)
sprites.add(marmita)
coletaveis = pg.sprite.Group()
coletaveis.add(cracha)
inimigos = pg.sprite.Group()
inimigos.add(rei)
vencedor = pg.sprite.Group()
vencedor.add(gota)
comida = pg.sprite.Group()
comida.add(marmita)



while True:
    tela.blit(fundo, (0, 0))
    relogio.tick(30)
    mensagem4 = f"Crachas Restantes: {crachas}"
    texto4 = fonte.render(mensagem4, False, (0, 0, 0))
    tela.blit(texto4, (450, 50))
    sprites.draw(tela)
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
    if rodando:
        if debuff == 0:
            if pg.key.get_pressed()[K_a]:
                z = z - 10
            if pg.key.get_pressed()[K_d]:
                z = z + 10
            if pg.key.get_pressed()[K_w]:
                w = w - 10
            if pg.key.get_pressed()[K_s]:
                w = w + 10
        elif debuff == 1:
            if pg.key.get_pressed()[K_a]:
                z = z - 7
            if pg.key.get_pressed()[K_d]:
                z = z + 7
            if pg.key.get_pressed()[K_w]:
                w = w - 7
            if pg.key.get_pressed()[K_s]:
                w = w + 7
        elif debuff == 2:
            if pg.key.get_pressed()[K_a]:
                z = z - 5
            if pg.key.get_pressed()[K_d]:
                z = z + 5
            if pg.key.get_pressed()[K_w]:
                w = w - 5
            if pg.key.get_pressed()[K_s]:
                w = w + 5
        elif debuff == 3:
            if pg.key.get_pressed()[K_a]:
                z = z - 2
            if pg.key.get_pressed()[K_d]:
                z = z + 2
            if pg.key.get_pressed()[K_w]:
                w = w - 2
            if pg.key.get_pressed()[K_s]:
                w = w + 2
    else:
        pass

    colisao_cracha = pg.sprite.spritecollide(gota, coletaveis, False, pg.sprite.collide_mask)
    if colisao_cracha:
        crachas -= 1
        debuff += 1
        if crachas == 0:
            colisao_cracha = pg.sprite.spritecollide(gota, coletaveis, True, pg.sprite.collide_mask)
            pronto = True
        else:
            coletaveis.draw(tela)
            coletaveis.update()
    else:
        pass

    colisao_comida = pg.sprite.spritecollide(gota, comida, True, pg.sprite.collide_mask)
    if colisao_comida:
        if debuff > 0:
            debuff -=1
        else:
            pass
    else:
        pass


    colisao_inimigo = pg.sprite.spritecollide(gota, inimigos, False, pg.sprite.collide_mask)
    if colisao_inimigo and not pronto:
        mensagem1 = "Você Perdeu!"
        rodando = False
        texto1 = fonte.render(mensagem1, True, (0, 0, 0))
        tela.blit(fundo, (0, 0))
        sprites.draw(tela)
        tela.blit(texto1, (280,200))
    if colisao_inimigo and pronto:
        mensagem2 = "Parabéns, agora você se tornou o novo Rei do Grad"
        rodando = False
        texto2 = fonte.render(mensagem2, True, (0, 0, 0))
        tela.blit(fundo, (0, 0))
        tela.blit(texto2, (50, 200))
        vencedor.draw(tela)
        vencedor.update()

    elif not colisao_inimigo:
        vencedor.update()
        inimigos.update()






    pg.display.flip()
