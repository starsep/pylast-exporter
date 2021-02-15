import json
import sys
from dataclasses import asdict, dataclass
from os import environ

import pylast
from tqdm import tqdm

API_KEY = environ.get("PYLAST_EXPORTER_API_KEY")
API_SECRET = environ.get("PYLAST_EXPORTER_API_SECRET")
USERNAME = environ.get("PYLAST_EXPORTER_USERNAME")


@dataclass
class Scrobble:
    album: str
    artistName: str
    date: str
    timestamp: int
    title: str


def main():
    lastFMNetwork = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
    user = lastFMNetwork.get_user(username=environ.get(USERNAME))

    with tqdm(file=sys.stderr, total=user.get_playcount()) as bar:
        bar.set_description("Fetching scrobbles from Last.fm")
        scrobbles = list()
        for playedTrack in user.get_recent_tracks(limit=None, stream=True):
            scrobble = Scrobble(
                album=playedTrack.album,
                artistName=playedTrack.track.artist.name,
                date=playedTrack.playback_date,
                timestamp=int(playedTrack.timestamp),
                title=playedTrack.track.title,
            )
            scrobbles.append(scrobble)
            bar.update(1)

    scrobbles = list(map(asdict, scrobbles))
    print(json.dumps(scrobbles, ensure_ascii=False))


if __name__ == "__main__":
    main()
