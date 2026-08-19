# ============================================================
# Exercises 07: Album (make_album)
# 'tracks' is OPTIONAL with default None ("no value given").
# The key is only added to the dictionary when a real number
# is passed. The function RETURNS a dictionary.
# ============================================================


def make_album(artist, title, tracks=None):
    """Build a dictionary describing a music album."""
    album = {"artist": artist.title(), "title": title.title()}
    if tracks is not None:
        album["tracks"] = tracks
    return album


album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Ed Sheeran", "Divide")
album3 = make_album("Pink Floyd", "The Dark Side of the Moon", tracks=10)

print(album1)
print(album2)
print(album3)