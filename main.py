import pygame
import pygame.freetype
import random
import time

width = 1000
height = 600
pygame.init()
font = pygame.font.SysFont('arial', 32, 1)



display = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption("Snake!!")
pygame_icon = pygame.image.load('3870923.png')
pygame.display.set_icon(pygame_icon)
colors = {
    "snake head": (0, 185, 100),
    "snake tail": (0, 170, 100),
    "apple": (255, 0, 0),
    "enemy": (0, 0, 255)
}
snake_pos = {
    "x": width / 2 - 5,
    "y": height / 2 - 5,
    "change x": 0,
    "change y": 0
}
snake_size = (10, 10)

game_end = False

snake_speed = 5

snake_tails = []

food_pos = {
    "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10
}
enemy_size = (30, 50)
enemy_pos = {
    "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10
}


food_size = (10, 10)
food_eaten = 0
snake_tails.append([snake_pos["x"] + 10, snake_pos["y"]])
snake_tails.append([snake_pos["x"] + 20, snake_pos["y"]])
snake_tails.append([snake_pos["x"] + 30, snake_pos["y"]])
best_score = 0

while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_pos["change x"] == 0:
                snake_pos["change y"] = 0
                snake_pos["change x"] = -snake_speed

            elif event.key == pygame.K_RIGHT and snake_pos["change x"] == 0:
                snake_pos["change y"] = 0
                snake_pos["change x"] = snake_speed

            elif event.key == pygame.K_UP and snake_pos["change y"] == 0:
                snake_pos["change y"] = -snake_speed
                snake_pos["change x"] = 0

            elif event.key == pygame.K_DOWN and snake_pos["change y"] == 0:
                snake_pos["change y"] = snake_speed
                snake_pos["change x"] = 0
    display.fill((0, 230, 255))
    food_eaten = str(food_eaten)
    lenth = len(snake_tails)+1
    lenth = str(lenth)
    text = font.render(f"Score:{food_eaten}", 1, (0, 0, 0), (0, 230, 255))
    text2 = font.render(f"Len:{lenth}", 1, (0, 0, 0), (0, 230, 255))
    display.blit(text, (10, 0))
    display.blit(text2, (130, 0))
    lenth = int(lenth)
    ltx = snake_pos["x"]
    lty = snake_pos["y"]
    for i, v in enumerate(snake_tails):
        _ltx = snake_tails[i][0]
        _lty = snake_tails[i][1]

        snake_tails[i][0] = ltx
        snake_tails[i][1] = lty

        ltx = _ltx
        lty = _lty

    for t in snake_tails:
        pygame.draw.rect(display, colors["snake tail"], [
            t[0],
            t[1],
            snake_size[0],
            snake_size[1]])
    snake_pos["x"] += snake_pos["change x"]
    snake_pos["y"] += snake_pos["change y"]
    pygame.draw.rect(display, colors["snake head"], [
        snake_pos["x"],
        snake_pos["y"],
        snake_size[0],
        snake_size[1]])

    if snake_pos["x"] < - snake_size[0]:
        snake_pos["x"] = width
    elif snake_pos["x"] > width:
        snake_pos["x"] = 0
    elif snake_pos["y"] < - snake_size[1]:
        snake_pos["y"] = height
    elif snake_pos["y"] > height:
        snake_pos["y"] = 0


    pygame.draw.rect(display, colors["apple"], [
        food_pos["x"],
        food_pos["y"],
        food_size[0],
        food_size[1]])

    if (snake_pos["x"] == food_pos["x"]
            and snake_pos["y"] == food_pos["y"]):
        food_eaten = int(food_eaten)
        food_eaten += 1
        food_eaten = str(food_eaten)
        snake_tails.append([food_pos["x"], food_pos["y"]])

        food_pos = {
            "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
            "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10
        }

    for i, v in enumerate(snake_tails):
        # try:
        if (snake_pos["x"] + snake_pos["change x"] == snake_tails[i][0]
                and snake_pos["y"] + snake_pos["change y"] == snake_tails[i][1] and len(snake_tails) > 3):
            snake_tails = snake_tails[:i]
            break
                # quit()
                # snake_tails = []
                # food_eaten = int(food_eaten)
                # best_score = int(best_score)
                # if best_score < food_eaten:
                #    best_score = food_eaten
                # food_eaten = 0
                # best_score = str(best_score)
                # food_eaten = str(food_eaten)
                # snake_tails.append([snake_pos["x"] + 10, snake_pos["y"]])
                # snake_tails.append([snake_pos["x"] + 20, snake_pos["y"]])
                # snake_tails.append([snake_pos["x"] + 30, snake_pos["y"]])
        #except:
        #    pass


    if len(snake_tails) <= 7 and int(food_eaten) > 4:
        quit()
    elif len(snake_tails) <= 6 and int(food_eaten) > 3:
        quit()
    elif len(snake_tails) <= 5 and int(food_eaten) > 2:
        quit()
    elif len(snake_tails) <= 4 and int(food_eaten) > 1:
        quit()
    elif len(snake_tails) <= 8 and int(food_eaten) > 5:
        quit()
    elif len(snake_tails) <= 9 and int(food_eaten) > 6:
        quit()
    elif len(snake_tails) <= 10 and int(food_eaten) > 7:
        quit()
    elif len(snake_tails) <= 11 and int(food_eaten) > 8:
        quit()
    elif len(snake_tails) <= 12 and int(food_eaten) > 9:
        quit()
    elif len(snake_tails) <= 13 and int(food_eaten) > 10:
        quit()

    pygame.display.update()
    time.sleep(0.1)

pygame.quit()
quit()
