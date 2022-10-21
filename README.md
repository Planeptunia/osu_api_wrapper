# osu! APIv1 Wrapper
## About it
This is a small wrapper for osu! APIv1 written in Python

## Requirements
Requirements are:  
requests, osu! API key (you can get one [here](https://osu.ppy.sh/p/api))
```python
pip install requests
```

## What it can do
It can do these osu! APIv1 calls:
get_user,
get_user_best,
get_user_recent,
get_match,
get_beatmaps,
get_scores

## Example
##### Getting user information
```python
get_user('Planeptunia', std)
```
First argument is player's nickname, in our case it's Planeptunia.  
It also may be a user id, but we will need to specify what it is an id, and not a nickname. This can be done like this
```python
get_user('12280101', type=user_id)
```
Second argument is player's gamemode, in our case it's std (Standard)  
It also can be: taiko, ctb and mania  


Our output for this API call will be a dict:
```python
[{'user_id': '12280101', 'username': 'Planeptunia', 'join_date': '2018-05-16 16:14:50',
'count300': '9193355', 'count100': '1448308', 'count50': '131484', 'playcount': '41311',
'ranked_score': '11015650003', 'total_score': '49981844484', 'pp_rank': '55119', 'level': '100.231',
'pp_raw': '5052.35', 'accuracy': '98.68647766113281', 'count_rank_ss': '65', 'count_rank_ssh': '2',
'count_rank_s': '756', 'count_rank_sh': '18', 'count_rank_a': '1327', 'country': 'RU',
'total_seconds_played': '2886864', 'pp_country_rank': '4243', 'events': []}]
```
