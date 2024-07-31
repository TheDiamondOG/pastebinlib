# Pastebinlib
By TheDiamondOG
Source Code: https://github.com/thediamondog/pastebinlib

A small python library made for interacting with Pastebin

## Story
This was one of those small projects I would just make while I am in class, normally I would just make a multi tool, but this time I wanted to add in Pastebin support which is why I made Pastebinlib. It was meant to be for that small project on Replit, but I thought this is a pretty useful tool, so I wanted to make it public on GitHub.

This was originally made on November 13, 2023. The thing is that I forgot to upload it for 4 days so the whole thing released on GitHub on November 13, 2023.

8 months later I got bored and wanted to upgrade the project, so after releasing fake terminal I worked on this. So now Pastebinlib is now better, and I actually know how to get something on PyPi.
______________________________________________________
# Install

## Source
This is only if you want to run it straight from source
```shell
git clone https://github.com/TheDiamondOG/pastebinlib
python setup.py install
```
## PyPi
This is from PyPi the best way to get it 
```shell
pip install pastebinlib
```
______________________________________________________
# Documentation
## Normal Pastebin API
Requirements \
- API Key: https://pastebin.com/doc_api

Setting up the library to use the API wrapper

```python
import pastebinlib

pastebin = pastebinlib.Pastebinlib(api_key)
```

This is how you create a paste in Pastebinlib

Requirements
- Text
- Paste Name
- Privacy
- Paste Format
- Expiring Time

Privacy Option
- public
- unlisted
- private

Expire options
- never
- 10 minutes
- 1 hour
- 1 day
- 1 week
- 2 weeks
- 1 month
- 6 months
- 1 year

```python
import pastebinlib

pastebin = pastebinlib.Pastebinlib(api_key)

"""
First is the text
Second is the name
Third is the privacy
Fourth is the paste format
Last is the expiring time
"""

pastebin.create_paste("Your Text", "Your Paste Name", "public", "text", "never")
```

This is how to get the data from a paste

Requirements
- URL/Paste ID
- JSON <True/False>

```python
import pastebinlib

pastebin = pastebinlib.Pastebinlib(api_key)

"""
First is the URL/Paste ID
Second is using to say if the paste is in the json format <True/False>
"""

pastebin.get_paste("https://pastebin.com/raw/Fj8dsgCR", False)
```

This is how to get the id of a paste for some reason

All you need is the URL

```python
import pastebinlib

pastebin = pastebinlib.Pastebinlib(api_key)

"""
Input the url
"""

pastebin.get_paste_id("https://pastebin.com/raw/Fj8dsgCR")
```

## User Pastebin API
Setting up the the class for the User Pastebinlib

Requirements for this one
- API Key: https://pastebin.com/doc_api
- User Key (Not a function specific)
	- Pastebin Account
		- Username
		- Password

```python
import pastebinlib

userbin = pastebinlib.User(api_key, user_key, username, password)
```

This is how to list pastes under the account returns a list
Optional
- Limits (50 is default)

```python
import pastebinlib

userbin = pastebinlib.User(api_key, user_key, username, password)

pastes = userbin.list_pastes(limit=50)
```

This is how you delete a paste

Requirements
- URL/Paste

```python
import pastebinlib

userbin = pastebinlib.User(api_key, user_key, username, password)

userbin.delete_paste(url)
```

Get the user info return your user info in a JSON format

```python
import pastebinlib

userbin = pastebinlib.User(api_key, user_key, username, password)

userbin.get_user_info()
```

This is how to get the data from a private paste

Requirements
- URL/Paste ID
- JSON <True/False>

```python
import pastebinlib

pastebin = pastebinlib.Pastebinlib(api_key)

"""
First is the URL/Paste ID
Second is using to say if the paste is in the json format <True/False>
"""

pastebin.get_paste("https://pastebin.com/raw/Fj8dsgCR", False)
```
