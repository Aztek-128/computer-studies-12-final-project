import pygame as pygame
import time
import sqlite3

class main(): #This is a shooter game like survivor.io

    def __init__(self) -> None:
        file = 'dbase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        create table if not exists score (
            id integer primary key autoincrement,
            killscore int,
            time_spent_alive int);
        """
        self.cursor.execute(query)
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        self.pygametime = pygame.time.Clock()
        self.running = True
        self.stats = {"hp": 5,"dp": 1,"movement": 1}
        self.start
    def start(self):
        timestart = time.time()
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        


    
    
