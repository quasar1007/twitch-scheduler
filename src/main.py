"""Script to auto open twitch streams"""
import asyncio
import os

import yaml
import webbrowser

from twitchAPI.helper import first
from twitchAPI.twitch import Twitch

with open('config.yaml', 'r') as f:
    config = yaml.load(f, yaml.SafeLoader)

active_streams = set()


async def get_twitch_client() -> Twitch:
    """
    Gets the twitch client

    Returns:
        Twitch: the twitch client
    """
    return await Twitch(os.getenv("TwitchClientId"), os.getenv("TwitchSecret"))


async def main():
    """
    Main driver for the application

    Returns:
        None
    """
    while True:
        twitch = await get_twitch_client()
        for streamer in config["streamers"]:
            stream = await first(twitch.get_streams(user_login=[streamer]))
            if stream is not None:
                if streamer not in active_streams:
                    webbrowser.open(f"https://twitch.tv/{streamer}")
                    active_streams.add(streamer)
            elif streamer in active_streams:
                active_streams.remove(streamer)

        await asyncio.sleep(30)


asyncio.run(main())
