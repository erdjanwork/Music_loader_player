import pathlib

import psycopg2
import pygame as pg


class Song:
    def __init__(self, singer, song, path):
        self.singer = singer
        self.song = song
        self.path = path


connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='202703erdji',
    database='music_loader',
    port='5433'
)

cur = connection.cursor()

pg.init()

query = 'SELECT * FROM music_table'

cur.execute(query)
data = cur.fetchall()

obj_list = []

for row in data:
    for col in row:
        print(col)
    obj_list.append(Song(row[1], row[2], row[3]))

connection.close()
