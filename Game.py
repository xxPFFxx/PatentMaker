class Game():
    def __init__(self, number, uniq, numbers60, numbers180, name, difficulty):
        self.uniq = uniq
        self.numbers60 = numbers60
        self.numbers180 = numbers180
        self.name = name
        self.difficulty = difficulty
        self.number = number
        self.path = 'games/game' + str(number) # Путь к файлам конкретной игры
        # TODO Подумать какие должны быть поля. Например: Дата(Название), виды доп.сырья, правила, сложность и т.д.
