import json
from dataclasses import asdict, dataclass
from os import environ

import pylast
from alive_progress import alive_bar

API_KEY = environ.get("PYLAST_EXPORTER_API_KEY")
API_SECRET = environ.get("PYLAST_EXPORTER_API_SECRET")
OUTPUT_FILENAME = environ.get("PYLAST_EXPORTER_OUTPUT_FILENAME")
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

    with alive_bar(user.get_playcount()) as bar:
        bar.text("Fetching scrobbles from Last.fm")
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
            bar()

    with open(OUTPUT_FILENAME, "w", encoding="utf8") as f:
        scrobbles = list(map(asdict, scrobbles))
        json.dump(scrobbles, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
