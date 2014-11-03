import os, csv


class Config:
    LEVEL_WIDTH = 35
    LEVEL_HEIGHT = 21

    CELL_SIZE = 24
    WINDOW_WIDTH = CELL_SIZE*LEVEL_WIDTH
    WINDOW_HEIGHT = CELL_SIZE*LEVEL_HEIGHT

    hidden_flag = False

    @staticmethod
    def config_level(num):
        with open(os.path.join('levels', 'level{}.csv').format(num), 'rb') as file_data:
            row_num = 0
            for row in csv.reader(file_data):
                Config.LEVEL_WIDTH = len(row)
                row_num += 1
            Config.LEVEL_HEIGHT = row_num

        Config.WINDOW_WIDTH = Config.CELL_SIZE*Config.LEVEL_WIDTH
        Config.WINDOW_HEIGHT = Config.CELL_SIZE*Config.LEVEL_HEIGHT
        Config._hidden_flag = False
