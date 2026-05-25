from sqlalchemy import text


def fetch_albums(db):

    query = text("""
        SELECT album_id,
               title
        FROM album
        LIMIT 10
    """)

    result = db.execute(query)

    albums = []

    for row in result:

        albums.append({
            "id": row.album_id,
            "title": row.title
        })

    return albums