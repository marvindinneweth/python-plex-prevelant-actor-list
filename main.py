from collections import Counter
from plexapi.server import PlexServer

# How to get token:
# https://www.plexopedia.com/plex-media-server/general/plex-token/

PLEX_URL = "http://localhost:32400"
PLEX_TOKEN = "xxxx"
MOVIE_LIBRARY_NAME = "Movies"

plex = PlexServer(PLEX_URL, PLEX_TOKEN)

actors = Counter([role.tag for movie in plex.library.section(MOVIE_LIBRARY_NAME).all() for role in movie.reload().roles])

with open('actors.txt', 'w') as f:
    for actor in sorted(actors.items(), key=lambda x: x[1], reverse=True):
        print("{}\t{}".format(actor[1], actor[0]))
        f.write("{}\t{}\n".format(actor[1], actor[0]))