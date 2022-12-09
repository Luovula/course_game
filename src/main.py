# TEE PELI TÄHÄN
import pygame
import math
import random

class Luolataistelu:
    def __init__(self):
        pygame.init()

        self.lataa_kuvat()

        self.naytto = pygame.display.set_mode((640,480))

        #robotin ja hirvion kohdat
        self.kohdat = [[0,0 + self.seina.get_height()],[640-self.monsu.get_width(), 480-self.monsu.get_height()-self.seina.get_height()]]

        #pelissa kaytettavat napit
        self.napit = []
        self.napit.append((pygame.K_LEFT, -3, 0))
        self.napit.append((pygame.K_RIGHT, 3, 0))
        self.napit.append((pygame.K_UP, 0, -3))
        self.napit.append((pygame.K_DOWN, 0, 3))

        self.kello = pygame.time.Clock()

        self.painettu = {}

        self.fontti = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("luolataistelu")

        self.silmukka()



    def lataa_kuvat(self):
        self.robo = pygame.image.load("images/robo.png")
        self.monsu = pygame.image.load("images/hirvio.png")
        self.seina = pygame.image.load("seina/images.png")

    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()

    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                self.painettu[tapahtuma.key] = True
 
            if tapahtuma.type == pygame.KEYUP:
                del self.painettu[tapahtuma.key]

            if tapahtuma.type == pygame.QUIT:
                exit()
            
        for nappi in self.napit:
            if nappi[0] in self.painettu:
                self.kohdat[0][0] += nappi[1]
                self.kohdat[0][1] += nappi[2]
        
        self.kohdat[0][0] = max(self.kohdat[0][0] , 0)
        self.kohdat[0][0] = min(self.kohdat[0][0] , 640-self.robo.get_width())
        self.kohdat[0][1] = max(self.kohdat[0][1] , 0 + self.seina.get_height())
        self.kohdat[0][1] = min(self.kohdat[0][1] , 480-self.robo.get_height()-self.seina.get_height())

        if self.kohdat[1][0] > self.kohdat[0][0]:
            self.kohdat[1][0] -= 1
        if self.kohdat[1][0] < self.kohdat[0][0]:
            self.kohdat[1][0] += 1
        if self.kohdat[1][1] > self.kohdat[0][1]:
            self.kohdat[1][1] -= 1
        if self.kohdat[1][1] < self.kohdat[0][1]:
            self.kohdat[1][1] += 1

    def piirra_naytto(self):
        self.naytto.fill((150,75,0))
        for i in range(math.ceil(640/self.seina.get_width())):
            self.naytto.blit(self.seina, (0 + i * self.seina.get_width(), 0))
            self.naytto.blit(self.seina, (0 + i * self.seina.get_width(), 480-self.seina.get_height()))
        self.naytto.blit(self.robo,(self.kohdat[0][0], self.kohdat[0][1]))
        self.naytto.blit(self.monsu,(self.kohdat[1][0], self.kohdat[1][1]))
        pygame.display.flip()
        self.kello.tick(60)
if __name__ == "__main__":
    Luolataistelu()

