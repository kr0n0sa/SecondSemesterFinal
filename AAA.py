import sqlite3
import random

def recommend_songs_from_db(db_path, num_recommendations=5):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()


    cursor.execute("SELECT artist, track_name, popularity FROM spotify_top_1000_tracks")
    songs = cursor.fetchall()
    conn.close()

    if not songs:
        return []

    artists, titles, popularities = zip(*songs)

    selected_indices = random.choices(range(len(songs)), weights=popularities, k=num_recommendations)

    recommendations = [(artists[i], titles[i]) for i in selected_indices]

    return recommendations

db_path = "Top1KTracks.sqlite3"

recommended = recommend_songs_from_db(db_path)

for artist, song in recommended:
    print(f"{artist} - {song}")