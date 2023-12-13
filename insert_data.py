import pathlib
import psycopg2

files = pathlib.Path('/Users/terzi/PycharmProjects/music_loader_player/Music')
filtered_data = list(files.rglob('*.mp3'))



connection = psycopg2.connect(
    host='localhost',
    port='5433',
    user='postgres',
    password='password',
    database='music_loader'
)

cur = connection.cursor()

for i in filtered_data:
    singer = i.parts[6].split('-')[0]
    song = i.parts[6].split('-')[1]
    file_path = str(i)

    query = '''INSERT INTO music_table (singer, song, file_path)
    VALUES (%s, %s, %s)'''

    cur.execute(query, (singer, song, file_path))

connection.commit()
