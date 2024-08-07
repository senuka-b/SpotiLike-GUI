from string import ascii_lowercase as english
from fuzzywuzzy import process

HOTKEY_PREFIXES = [
    "alt",
    "backspace",
    "caps_lock",
    "ctrl",
    "cmd",
    "delete",
    "down",
    "end",
    "enter",
    "esc",
    "f1",
    "f10",
    "f11",
    "f12",
    "f13",
    "f14",
    "f15",
    "f16",
    "f17",
    "f18",
    "f19",
    "f2",
    "f20",
    "f3",
    "f4",
    "f5",
    "f6",
    "f7",
    "f8",
    "f9",
    "home",
    "insert",
    "left",
    "media_next",
    "media_play_pause",
    "media_previous",
    "media_volume_down" "media_volume_mute",
    "media_volume_up",
    "menu",
    "num_lock",
    "page_down",
    "page_up",
    "pause",
    "print_screen",
    "right",
    "scroll_lock",
    "shift",
    "space",
    "tab",
    "up",
]


def format(key: str) -> str:
    """Formats a hotkey-string in the format to pass in keyboard.GlobalHotkeys class"""

    if not key:
        return

    if key.endswith("+"):
        key[:-1]

    result = [
        i
        for i in [
            (
                f"<{thing}>"
                if any(map(key.__contains__, HOTKEY_PREFIXES))
                and thing in HOTKEY_PREFIXES
                else thing
            )
            for thing in key.split("+")
        ]
        if i
    ]

    return "+".join(result)


def match(keys: str) -> str:
    """Matches the string to the nearest possible value in HOTKEY_PREFIXES"""

    if keys:
        if keys.strip().lower() == "none":
            return None
    else:
        return None

    result = list(
        dict.fromkeys(
            [
                process.extractOne(key, HOTKEY_PREFIXES)[0]
                for key in keys.split("+")
                if not key in english and not key in [str(no) for no in range(10)]
            ]
            + [
                keys
                for keys in keys.split("+")
                if keys in english or keys in [str(x) for x in range(10)]
            ]
        )
    )

    return "+".join(result)


def unformat(combination: str) -> str:
    """Unformats a formatted string to it's original state"""

    return str(combination).replace("<", "").replace(">", "")
