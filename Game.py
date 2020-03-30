class Game():
    def __init__(self, number, name, difficulty, required_level):
        self.name = name
        self.difficulty = difficulty
        self.number = number
        self.path = 'games/game' + str(number) # Путь к файлам конкретной игры
        self.required_level = required_level
        # TODO Подумать какие должны быть поля. Например: Дата(Название), виды доп.сырья, правила, сложность и т.д.
