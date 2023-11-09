import pygame
import sys

# Definição das constantes
WIDTH, HEIGHT = 700, 700 # Dimensões da janela
FPS = 60
boardSize = 13  # Tamanho do tabuleiro
lineWidth = 2  # Largura das linhas
lineColor = (65, 37, 0)  # Cor das linhas
backgroundColor = (217, 164, 89)  # Cor de fundo
hoshiRadius = 5  # Raio dos pontos "hoshi"
HoshiColor = (65, 37, 0)  # Cor dos pontos "hoshi"

# Carregamento das imagens
icon = pygame.image.load("./icon.png")
menuBackground = pygame.image.load("./openingScreen.png")

# Inicialização do Pygame
pygame.init()

# Configurações da janela
pygame.display.set_caption('Go!')
pygame.display.set_icon(icon)
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Função para o menu
def menu():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        x, y = pygame.mouse.get_pos()
        window.blit(menuBackground, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x in range(178, 522) and y in range(246, 348):
                    return  # Sai do menu se o botão for pressionado

        if x in range(178, 522) and y in range(246, 348):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

# Função que desenha o tabuleiro
def drawBoard(window):
    # Definir o fundo da tela
    window.fill(backgroundColor)

    # Desenhar linhas horizontais e verticais do tabuleiro
    for i in range(boardSize):
        # Desenhar linhas horizontais
        pygame.draw.line(window, lineColor, (30, 30 + i * (WIDTH - 60) // (boardSize - 1)), (WIDTH - 30, 30 + i * (WIDTH - 60) // (boardSize - 1)), lineWidth)
        # Desenhar linhas verticais
        pygame.draw.line(window, lineColor, (30 + i * (HEIGHT - 60) // (boardSize - 1), 30), (30 + i * (HEIGHT - 60) // (boardSize - 1), HEIGHT - 30), lineWidth)

    # Desenhar os pontos "hoshi"
    if (boardSize == 9):
        hoshi_points = [(2, 2), (6, 2), (2, 6), (6, 6), (4, 4)]
    if (boardSize == 13):
        hoshi_points = [(3, 3), (9, 3), (3, 9), (9, 9), (6, 6)]
    if (boardSize == 19):
        hoshi_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9), (15, 9), (3, 15), (9, 15), (15, 15)]
    for x, y in hoshi_points:
        pygame.draw.circle(window, HoshiColor, (30 + x * (WIDTH - 60) // (boardSize - 1), 30 + y * (HEIGHT - 60) // (boardSize - 1)), hoshiRadius)

# Função que desenha as pedras
def drawStone(x, y, stoneColor):
    if stoneColor == "B":
        pygame.draw.circle(window, (0, 0, 0), (x, y), 26)  # Círculo para a pedra escura
    elif stoneColor == "W":
        pygame.draw.circle(window, (255, 255, 255), (x, y), 26)  # Círculo para a pedra clara

# Função principal do jogo
def main():
    run = True
    clock = pygame.time.Clock()
    stoneColor = "B"
    drawBoard(window)
    pygame.display.flip()

    while run:

        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if stoneColor == "B":
                    drawStone(x, y, stoneColor)
                    stoneColor = "W"
                else:
                    drawStone(x, y, stoneColor)
                    stoneColor = "B"

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    menu()  # Chama o menu antes do início do jogo
    main()  # Inicia o jogo após a seleção no menu
