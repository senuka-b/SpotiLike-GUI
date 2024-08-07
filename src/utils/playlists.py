import os

from urllib.request import urlretrieve
import json
import logging

from pprint import pprint

logging.getLogger(__name__)


def playlists_and_tracks(spotify) -> dict:
    """Returns a dict including tracks like:
    {"Playlist_name": {
        "id": "playlist_id",
        "image_url": "the_url_to_the_icon_of_the_playlist"
        "tracks": [list of track IDs(first 100)]
    }
        }"""

    playlists_and_tracks = {}

    for item in spotify.current_user_playlists()["items"]:
        if item["owner"]["id"] == spotify.me()["id"]:
            playlists_and_tracks[item["name"]] = {
                "id": item["id"],
                "image_url": (
                    item["images"][0]["url"]
                    if not item["images"] == []
                    else "./assets/error.ico"
                ),
                "tracks": [
                    song["track"]["id"]
                    for song in spotify.playlist_tracks(item["id"])["items"]
                ],
            }

    return playlists_and_tracks


def get_playlists(spotify) -> dict:
    """Returns a dict excluding tracks like:
    {"Playlist_name": {
        "id": "playlist_id",
        "image_url": "the_url_to_the_icon_of_the_playlist"
    }
        }"""

    playlists = {}

    data = spotify.current_user_playlists()
    user_id = spotify.me()["id"]

    while True:
        for item in data["items"]:

            if item["owner"]["id"] == user_id:

                playlists[str(item["name"])] = {
                    "id": item["id"],
                    "image_url": (
                        item["images"][0]["url"] if item["images"] else "noIcon"
                    ),
                }

        if data["next"]:
            data = spotify.next(data)
        else:
            break

    return playlists


def save_images(playlists) -> None:
    """Downloads playlist icons returned to './assets/playlists.'"""

    if not os.path.exists("./assets/playlists"):
        os.makedirs("./assets/playlists")

    images = {y["id"]: y["image_url"] for x, y in playlists.items()}

    for id, url in images.items():
        if not os.path.exists(f"./assets/playlists/{id}.ico"):
            if not url == "noIcon":
                urlretrieve(url, f"./assets/playlists/{id}.ico")

            logging.info(f"Downloaded {id}.ico")
    logging.info("Playlist icons downloaded")


def settings() -> dict:
    """Returns a dict containing user settings."""

    with open("./config/settings.json") as f:
        data = json.load(f)
    return data


def main(spotify) -> dict:
    """Main method to return playlist/track data according to user settings"""

    if settings()["fetch_playlists"] and settings()["fetch_songs"]:
        data = playlists_and_tracks(spotify)

    elif settings()["fetch_playlists"]:
        data = get_playlists(spotify)

    else:
        with open("./config/data.json") as f:
            data = json.load(f)
    save_images(data)
    for x in data:
        # Replace image_url value to the path to the file, as we know we have already downloaded them.
        data[x]["image_url"] = f"./assets/playlists/{data[x]['id']}.ico"

    return data
