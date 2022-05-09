

import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint

pg.init()
largura = 800
altura = 600
tela = pg.display.set_mode((largura, altura))
fundo = pg.image.load("fundo.png")
start = False
fundo_start = pg.image.load("tela inicio.png")
relogio = pg.time.Clock()
z = 0
w = 0
fonte = pg.font.SysFont('arial', 30, False, False)
pronto = False
crachas = 3
debuff = 0
rodando = True
musica_fundo = pg.mixer.music.load("musicafundo.mp3")
pg.mixer.music.play(-1)
tela_end = pg.image.load("tela end.png")
tomadas_aparecer = False

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
        self.image = pg.transform.scale(self.image, (int(64 * 1.5), int(64 * 1.5)))

        if crachas == 0:
            self.rect.x = 700
            self.rect.y = 50
        else:
            if self.rect.x > z:
                self.rect.x -= 4
            elif self.rect.x < z:
                self.rect.x += 4

            if self.rect.y > w:
                self.rect.y -= 4
            elif self.rect.y < w:
                self.rect.y += 4

class Marmita(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load('almirante.png'))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 600)
        self.rect.y = randint(100, 400)
        self.mask = pg.mask.from_surface(self.image)

class Tomadas(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load("tomada1.png"))
        self.sprites.append(pg.image.load("tomada2.png"))
        self.sprites.append(pg.image.load("tomada3.png"))
        self.sprites.append(pg.image.load("tomada4.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.y = randint(50, 550)
        self.image = pg.transform.scale(self.image, (int(64 * 2), int(64 * 2)))

    def update(self):
        self.atual += 1
        if self.atual >= 4:
            self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (int(64 * 2), int(64 * 2)))
        self.rect.x += randint(8, 15)


cracha = Cracha()
rei = Reidograd()
gota = Gota()
marmita = Marmita()
tomada = Tomadas()
sprites = pg.sprite.Group()
sprites.add(rei)
sprites.add(cracha)
sprites.add(gota)
sprites.add(marmita)
coletaveis = pg.sprite.Group()
coletaveis.add(cracha)
inimigos = pg.sprite.Group()
inimigos.add(rei)
comida = pg.sprite.Group()
comida.add(marmita)
tomadas = pg.sprite.Group()
tomadas.add(tomada)
vencedor = pg.sprite.Group()
vencedor.add(gota)



while True:
    if start:
        tela.blit(fundo, (0, 0))
        relogio.tick(30)
        mensagem4 = f"Crachas Restantes: {crachas}"
        texto4 = fonte.render(mensagem4, False, (255, 255, 255))
        tela.blit(texto4, (480, 50))
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
                    z = z - 3
                if pg.key.get_pressed()[K_d]:
                    z = z + 3
                if pg.key.get_pressed()[K_w]:
                    w = w - 3
                if pg.key.get_pressed()[K_s]:
                    w = w + 3
        else:
            pass

        colisao_cracha = pg.sprite.spritecollide(gota, coletaveis, False, pg.sprite.collide_mask)
        if colisao_cracha:
            crachas -= 1
            debuff += 1
            if crachas == 0:
                colisao_cracha = pg.sprite.spritecollide(gota, coletaveis, True, pg.sprite.collide_mask)
                pronto = True
                tomadas_aparecer = True
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
            rodando = False
            tela.blit(tela_end, (0, 0))
        if colisao_inimigo and pronto:
            mensagem2 = "Parabéns, agora você se tornou o novo Rei do Grad"
            rodando = False
            texto2 = fonte.render(mensagem2, True, (0, 0, 0))
            tela.blit(fundo, (0, 0))
            tela.blit(texto2, (50, 200))

        elif not colisao_inimigo:
            vencedor.update()
            inimigos.update()

        if tomadas_aparecer:
            colisao_tomadas = pg.sprite.spritecollide(gota, tomadas, False, pg.sprite.collide_mask)
            if colisao_tomadas:
                rodando = False
                tela.blit(tela_end, (0, 0))
            else:
                tomadas.draw(tela)
                tomadas.update()
        else:
            pass


    else:
        relogio.tick(30)
        tela.blit(fundo_start, (0,0))
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                start = True
            else:
                pass
            if event.type == QUIT:
                pg.quit()
                exit()




    pg.display.flip()
