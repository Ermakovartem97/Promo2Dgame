import sys

from pygame import *
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN


# pygame.constants необходим для создания условия выхода из цикла


# далее создаем функцию my_animation, принимающая следующие аргументы w1, h1 - количество спрайтов в строке и столбце
# изображения, k - это общее количество кадров в изображении, fps - количество кадров в секунду, name - название и путь
# к изображению, position - положение анимации на игровом экране.

def my_animation(w1, h1, k, fps, name, position, animation_frames=[]):
    # список для хранения кадров и таймер
    frames = []
    timer = time.Clock()

    # создаем экран и загружаем изображение в переменную sprite, установив методом convert_alpha необходимую прозрачность
    scr = display.set_mode((400, 400), 0, 32)
    sprite = image.load("{0}.png".format(name)).convert_alpha()

    # находим длину, ширину изображения и размеры каждого кадра
    width, height = sprite.get_size()
    w, h = width / w1, height / h1

    # счетчик положения кадра на изображении
    row = 0

    # итерация по строкам
    for j in range(int(height / h)):
        # производим итерацию по элементам строки
        for i in range(int(width / w)):
            # добавляем  в список отдельные кадры
            animation_frames.append(sprite.subsurface(Rect(i * w, row, w, h)))
        # смещаемся на высоту кадра, т.е. переходим на другую строку
        row += int(h)

    # счетчик
    counter = 0

    last_pressed = 0
    while True:
        # условие выхода из цикла - нажатие клавиши ESCAPE
        for evt in event.get():
            if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
                sys.exit()
        # заполняем игровое поле красным цветом и методом blit вырисовываем на поверхности
        # scr, c координатами position, вырезанную часть изображения
        scr.fill((255, 0, 0))

        keys = key.get_pressed()



        if keys[K_DOWN]:
            scr.blit(animation_frames[counter], position)
            counter = (counter + 1) % w1
            position[1] += 3
            last_pressed = counter
        elif keys[K_LEFT]:
            scr.blit(animation_frames[counter], position)
            counter = (counter + 1) % w1 + 12
            position[0] -= 3
            last_pressed = counter
        elif keys[K_RIGHT]:
            scr.blit(animation_frames[counter], position)
            counter = (counter + 1) % w1 + 12 * 2
            position[0] += 3
            last_pressed = counter
        elif keys[K_UP]:
            scr.blit(animation_frames[counter], position)
            counter = (counter + 1) % w1 + 12 * 3
            position[1] -= 3
            last_pressed = counter
        else:
            scr.blit(animation_frames[last_pressed], position)
        # scr.blit(animation_frames[counter], position)

        # счетчик используемый как индекс в списке увеличивается до того как не превысит общее количество кадров,
        # после чего цикл повторяется

        # обновляем экран
        display.update()
        timer.tick(fps)


if __name__ == "__main__":
    # x = float(input("Fps:"))
    x = 30
    my_animation(12, 4, 48, x, "chel", [300, 300])
