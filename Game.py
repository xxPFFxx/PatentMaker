class Game():
    def __init__(self, number, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.number = number
        self.path = 'games/game' + str(number) # Путь к файлам конкретной игры
        # TODO Подумать какие должны быть поля. Например: Дата(Название), виды доп.сырья, правила, сложность и т.д.
