# Нижутин Олег 2415 (lvl_3)
import pygame

# Создание окна 800*800
pygame.init()
screen = pygame.display.set_mode((800, 800))

# Указание координат и состояния букв (по умолчанию буквы невидимы - false)
letters = {
    'О': {'x': 100, 'y': 100, 'visible': False},
    'Л': {'x': 700, 'y': 100, 'visible': False},
    'Е': {'x': 700, 'y': 700, 'visible': False},
    'Г': {'x': 100, 'y': 700, 'visible': False}
}

# Загрузка шрифта (по умолчанию - чёрный, 100 р-р)
font = pygame.font.Font(None, 100)

running = True
while running: # Пока true - код выполняется
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Нажата кнопка закрытия окна - программа завершила работу
            running = False
        elif event.type == pygame.KEYDOWN: # Проверка нажатиия клавиш (и каких)
            if event.key == pygame.K_j:
                letters['О']['visible'] = not letters['О']['visible']
            elif event.key == pygame.K_k:
                letters['Л']['visible'] = not letters['Л']['visible']
            elif event.key == pygame.K_t:
                letters['Е']['visible'] = not letters['Е']['visible']
            elif event.key == pygame.K_u:
                letters['Г']['visible'] = not letters['Г']['visible']
    
    screen.fill((255, 255, 255))  # Очищаем экран (делаем белым)
    
    # Отрисовка букв
    for letter, data in letters.items():
        if data['visible']: # Является ли буква видимой
            text = font.render(letter, True, (0, 0, 0)) # Если да - создаем букву шрифтом черного цвета (true тут - сглаживание)
            rect = text.get_rect(center=(data['x'], data['y'])) # Получение прямоугольника для буквы
            screen.blit(text, rect) # Текст отрисовывается в окне
    
    pygame.display.flip() # Обновляем экран 

pygame.quit() # Завершаем работу