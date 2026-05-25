from sqlalchemy import text


def fetch_tracks(db):

    query = text("""
        SELECT track_id,
               name,
               milliseconds
        FROM track
        LIMIT 20
    """)

    result = db.execute(query)

    tracks = []

    for row in result:

        tracks.append({
            "id": row.track_id,
            "name": row.name,
            "duration": row.milliseconds
        })

    return tracks