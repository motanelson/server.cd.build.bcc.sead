
import pygame
import sys
import random

# Inicializar o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 0)  # Amarelo
ROAD_COLOR = (128,128, 0)  # Cinza escuro
LANE_COLOR = (255, 255, 255)  # Branco
FPS = 500

# Configurações da estrada
ROAD_WIDTH = 400
LANE_WIDTH = 20
ROAD_OFFSET = (SCREEN_WIDTH - ROAD_WIDTH) // 2

# Configurações do carro
CAR_WIDTH = 40
CAR_HEIGHT = 70
CAR_IMAGE_PATH = "car_top_view.png"  # Certifique-se de ter essa imagem no diretório atual

# Inicializar a tela
tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Corrida 2D")

# Carregar imagem do carro
def load_car_image():
    try:
        car_image = pygame.image.load(CAR_IMAGE_PATH)
        return pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))
    except pygame.error:
        print(f"Erro: Imagem '{CAR_IMAGE_PATH}' não encontrada.")
        pygame.quit()
        sys.exit()

car_image = load_car_image()

# Inicializar posição do carro
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 20

# Criar segmentos de estrada
road_segments = []
for y in range(0, SCREEN_HEIGHT, 100):
    curve = random.choice([-20, 0, 20])
    road_segments.append(curve)

def update_road_segments():
    """Atualizar os segmentos da estrada para criar uma ilusão de movimento."""
    road_segments.pop(0)
    curve = random.choice([-20, 0, 20])
    road_segments.append(curve)

def draw_road():
    """Desenhar a estrada na tela."""
    x = ROAD_OFFSET
    for i, curve in enumerate(road_segments):
        y1 = i * 100
        y2 = y1 + 100
        x += curve
        pygame.draw.polygon(tela, ROAD_COLOR, [(x, y1), (x + ROAD_WIDTH, y1), (x + ROAD_WIDTH + curve, y2), (x + curve, y2)])
        for lane in range(1, 4):
            lane_x1 = x + lane * LANE_WIDTH
            lane_x2 = x + lane * LANE_WIDTH + curve
            pygame.draw.line(tela, LANE_COLOR, (lane_x1, y1), (lane_x2, y2), 2)

# Loop principal
def main():
    global car_x, car_y
    clock = pygame.time.Clock()
    running = True

    while running:
        tela.fill(BG_COLOR)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimento do carro
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= 5
        if keys[pygame.K_RIGHT]:
            car_x += 5
        if keys[pygame.K_UP]:
            car_y -= 5
        if keys[pygame.K_DOWN]:
            car_y += 5

        # Constranger o carro dentro da estrada
        car_x = max(ROAD_OFFSET, min(car_x, ROAD_OFFSET + ROAD_WIDTH - CAR_WIDTH))

        # Atualizar estrada
        update_road_segments()

        # Desenhar estrada e carro
        draw_road()
        tela.blit(car_image, (car_x, car_y))

        # Atualizar tela
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
