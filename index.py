import pygame
import sys

items = [
    "ALPENKRÄHE",
    "DÜNNSCHNABEL-BRACHVOGEL",
    "EINFARBDROSSEL",
    "EINSIEDLERDROSSEL",
    "GRAUORTOLAN",
    "GRAUWANGENDROSSEL",
    "GRÜNWALDSÄNGER",
    "KATZENVOGEL",
    "KRONENLAUBSÄNGER",
    "NODDISEESCHWALBE",
    "PAZIFIKPIEPER",
    "PHARAONENZIEGENMELKER",
    "PRÄRIELÄUFER",
    "ROTKEHLDROSSEL",
    "ROTSCHWANZDROSSEL",
    "SANDFLUGHUHN",
    "SCHMUCKREIHER",
    "STEINSPERLING",
    "STREIFENSCHWIRL",
    "STUMMELLERCHE",
    "TÜRCKENAMMER",
    "WACHOLDERLAUBSÄNGER",
    "WEISSFLÜGELLERCHE",
    "WERMUTREGENPFEIFER",
    "ZWERGDROSSEL"
]

itemLength = len(items)
currentIndex = 13
font = None
text_size = 40
margin = 50

def main():
    global currentIndex

    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    clock = pygame.time.Clock()

    font_name = "synchro.ttf"  # Replace with the actual font filename
    font_size = 80
    font = pygame.font.Font(font_name, font_size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    currentIndex = (currentIndex - 1) % itemLength
                elif event.key == pygame.K_DOWN:
                    currentIndex = (currentIndex + 1) % itemLength
                elif event.key == pygame.K_RETURN:
                    print("Selected Item:", items[currentIndex])

        screen.fill((0, 0, 0))
        pygame.draw.polygon(screen, (255, 54, 252), [(0, 0), (1080, 0), (1080, 720), (0, 720)])
        pygame.draw.rect(screen, (238, 168, 252), (0, 272, 1080, 72))
        #pygame.draw.rect(screen, (255, 255, 255), (10, 292, 500, 60))
        
        render_text = font.render(items[currentIndex], True, (255, 255, 255))
        screen.blit(render_text, (180, 280))

        for s in range(1, 6):

            shown = ""
            if currentIndex - s < 0:
                shown = items[itemLength+(currentIndex-s)]
            else:     
                shown = items[currentIndex-s]

            text_color = (238, 168, 252, 255 - (s * 15))
            font_size_local =  font_size - (s * 10)
            render_text = pygame.font.Font(font_name, font_size_local).render(shown, True, text_color)
            screen.blit(render_text, (150 - s * 30, 280 - s * margin))

        for s in range(1, 6):
            shown = ""
            if currentIndex + s >= itemLength:
                shown = items[(currentIndex+s) - itemLength]
            else:     
                shown = items[currentIndex+s]
            
            font_size_local =  font_size - (s * 10)

            text_color = (238, 168, 252, 255 - (s * 15))
            render_text = pygame.font.Font(font_name, font_size_local).render(shown, True, text_color)
            screen.blit(render_text, (150 - s * 30, 280 + s * margin))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
