# osu! APIv1 Python Wrapper
# by Planeptunia

from datetime import date
import requests
# Link to API = https://osu.ppy.sh/api/

api_key = 'PLACE_YOUR_OSU_API_KEY_HERE'

# Shortcuts
# Modes
std = 0
taiko = 1
ctb = 2
mania = 3

# Type
username = 'string'
user_id = 'id'

# Mods
NoMod = 0
NoFail = 1
Easy = 2
TouchDevice = 4
Hidden = 8
HardRock = 16
SuddenDeath = 32
DoubleTime = 64
Relax = 128
HalfTime = 256
Nightcore = 512 + DoubleTime
Flashlight = 1024
Autoplay = 2048
SpunOut = 4096
Autopilot = 8192
Perfect = 16384 + SuddenDeath
Key4 = 32768
Key5 = 65536
Key6 = 131072
Key7 = 262144
Key8 = 524288
FadeIn = 1048576
Random = 2097152
Cinema = 4194304
Target = 8388608
Key9 = 16777216
KeyCoop = 33554432
Key1 = 67108864
Key3 = 134217728
Key2 = 268435456
ScoreV2 = 536870912
Mirror = 1073741824

# User information functions
def get_user(user, mode:int=std, type:str=username, event_days:int='1') -> dict:
    """Get info of certain user"""
    par = {'k': api_key, 'u': user, 'm': mode, 'type': type, 'event_days': event_days}
    req = requests.get('https://osu.ppy.sh/api/get_user', params=par).json()
    return req

def get_user_best(user, mode:int=std, limit:int='10', type:str=username) -> dict:
    """Get best scores of certain user"""
    par = {'k': api_key, 'u': user, 'm': mode, 'limit': limit, 'type': type}
    req = requests.get('https://osu.ppy.sh/api/get_user_best', params=par).json()
    return req

def get_user_recent(user, mode:int=std, limit:int='10', type:str=username) -> dict:
    """Get recent scores of certain user"""
    par = {'k': api_key, 'u': user, 'm': mode, 'limit': limit, 'type': type}
    req = requests.get('https://osu.ppy.sh/api/get_user_recent', params=par).json()
    return req

# Multiplayer
def get_match(match_id:int) -> dict:
    """Get multiplayer match information"""
    par = {'k': api_key, 'mp': match_id}
    req = requests.get('https://osu.ppy.sh/api/get_match', params=par).json()
    return req

# Beatmap
def get_beatmaps(user, hash:str, since:date='2007-10-6 17:46:31', set_id:int='1', map_id:int='75', type:str=username, mode:int=std, limit:int='10', mods:int=NoMod, converts:int='0') -> dict:
    """Get general beatmap info"""
    par = {'k': api_key, 'since': since, 's': set_id, 'b': map_id, 'u': user, 'type': type, 'm': mode, 'a': converts, 'h': hash, 'limit': limit, 'mods': mods}
    req = requests.get('https://osu.ppy.sh/api/get_beatmaps', params=par).json()
    return req

def get_scores(user, mods:int='0', map_id:int='75', mode:int=std, type:str=username, limit:int='10') -> dict:
    """Retrieve information about the top 100 scores of specified beatmap"""
    par = {'k': api_key, 'b': map_id, 'u': user, 'm': mode, 'mods': mods, 'type': type, 'limit': limit}
    req = requests.get('https://osu.ppy.sh/api/get_scores', params=par).json()
    return req