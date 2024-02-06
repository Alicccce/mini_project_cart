import pygame
import sys
import os
import requests

x1, x2 = int(input()), int(input())
map_request = f'http://static-maps.yandex.ru/1.x/?ll={x1}%2C{x2}&spn=3,5&l=map'
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
zoom = 2

pr1, pr2 = False, False
screen = pygame.display.set_mode((600, 450))
mappp = pygame.image.load(map_file)


mapr = mappp.get_rect()
mapsurf = pygame.Surface((600, 450))
mapsurf.blit(pygame.transform.scale(mappp,(600, 450)),(0,0))
screen.blit(mapsurf,(0,0))
scale = 1

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_PAGEDOWN:
            zoom = 2
            zoom_size = (int(600 / zoom), int(450 / zoom))
            zoom_surf = .
            screen.blit(zoom_surf, (0, 0))
        if event.type == pygame.K_PAGEUP:
            zoom = 0.5
            zoom_size = (int(600 / zoom), int(450 / zoom))
            zoom_surf = pygame.Surface(zoom_size)
            zoom_surf.blit(screen, (0, 0), zoom_size)
            zoom_surf = pygame.transform.smoothscale(zoom_surf, (600, 450))
            screen.blit(zoom_surf, (0, 0))
        pygame.display.flip()
    #map_request = f'http://static-maps.yandex.ru/1.x/?ll={x1}%2C{x2}&spn={3/zoom},{5/zoom}&l=map'
    #screen.blit(pygame.transform.scale(screen, (600, 450)), (0, 0))
pygame.display.update()
pygame.quit()
os.remove(map_file)