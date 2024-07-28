import requests
import xml.etree.ElementTree as ET

class ColorText:
  COLORS = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[39m'
  }

  BACKGROUNDS = {
    'black': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'magenta': '\033[45m',
    'cyan': '\033[46m',
    'white': '\033[47m',
    'reset': '\033[49m'
  }

  STYLES = {
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reversed': '\033[7m',
    'reset': '\033[0m'
  }

  def colorize(self, text: str, color=None, background=None, style=None):
    if style and style in self.STYLES:
      text = self.STYLES[style] + text

    if color and color in self.COLORS:
      text = self.COLORS[color] + text

    if background and background in self.BACKGROUNDS:
      text = self.BACKGROUNDS[background] + text

    return text + self.STYLES['reset']

color_system = ColorText()

class Pastelib:
  def __init__(self, api_key:str):
    # Set the api key
    self.api_key = api_key

  # This creates a paste you can not edit (API Key needed)
  def create_paste(self, text:str, name:str=None, privacy:str="public", format:str="text", expire="never"):
    # Making the privacy setting translation
    if privacy == "public":
      privacy = 0
    if privacy == "unlisted":
      privacy = 1
    if privacy == "private":
      privacy = 2

    # Make everything for expire lower case
    expire = expire.lower()

    # Translate the expiring crap
    if expire == "never":
      expire = "N"
    elif expire == "10 minutes":
      expire = "10M"
    elif expire == "1 hour":
      expire = "1H"
    elif expire == "1 day":
      expire = "1D"
    elif expire == "1 week":
      expire = "1W"
    elif expire == "2 weeks":
      expire = "2W"
    elif expire == "1 month":
      expire = "1M"
    elif expire == "6 months":
      expire = "6M"
    elif expire == "1 year":
      expire = "1Y"

    # All the paste data
    data = {
      "api_dev_key": self.api_key,
      "api_option": "paste",
      "api_paste_code": text,
      "api_paste_name": name,
      "api_paste_private": privacy,
      "api_paste_format": format,
      "api_paste_expire_date": expire
    }
    # Make a try statement to send a post request
    try:
      # The post request
      res = requests.post("https://pastebin.com/api/api_post.php", data=data)
      # Check if the creation worked
      if res.status_code == 200:
        # Return the paste url
        return res.text
      else:
        # If it fails return false
        return False
    except Exception as e:
      # Another fail message
      return False

  # The gets a paste's info (API Key not needed)
  def get_paste(self, url:str, json:bool=False):
    # Get the paste id
    if url.startswith("https://") or url.startswith("http://"):
      paste_id = self.get_paste_id(url)
    else:
      # Setting the url as the paste id
      paste_id = url

    # Send the get request
    res = requests.get(f"https://pastebin.com/raw/{paste_id}")

    # Check if the request actually worked correctly
    if res.status_code == 200:
      # Check if the request is a json response by the user
      if json == False:
        # Return the paste as text
        return res.text
      else:
        # Return the paste as json
        return res.json()
    else:
      # If it fails return false
      return False

  # This lets you get the paste id from the paste url (API Key not needed)
  def get_paste_id(self, url:str):
    # Get the id from the paste's url
    return url.split("/")[-1]

class User:
  def __init__(self, api_key:str, user_key:str=None, username:str=None, password:str=None):
    # Set the api key
    self.api_key = api_key

    # Check if the user key was set
    if user_key == None:
      # Check if username and password are set
      if username == None or password == None:
        print(color_system.colorize("Can't get user key without the username or password", "red"))
      else:
        # Setting up all the input data
        data = {
          "api_dev_key": api_key,
          "api_user_name": username,
          "api_user_password": password
        }

        # Get the user key
        res = requests.post("https://pastebin.com/api/api_login.php", data=data)

        # Run all the status check
        if res.status_code == 200:
          # Set the user key
          self.user_key = res.text
        elif res.text == "Bad API request, invalid login":
          # Tell the user the lib messed up
          print(color_system.colorize("Incorrect username or password", "red"))
          self.user_key = None
        else:
          # Tell the user the lib messed up

          print(color_system.colorize("Failed to set user key", "red"))
          print(color_system.colorize(res.text, "red"))
          self.user_key = None
    else:
      # Set the user key
      self.user_key = user_key

  def list_pastes(self, limit:int=50):
    # Fix all the limit stuff
    if limit > 1000:
      limit = 1000
    if limit < 1:
      limit = 1

    # Get all the posts in the limits

    # Set all the paste data
    data = {
      "api_dev_key": self.api_key,
      "api_user_key": self.user_key,
      "api_results_limit": limit,
      "api_option": "list"
    }

    # Send post request
    res = requests.post("https://pastebin.com/api/api_post.php", data=data)

    # Request check
    if res.status_code == 200:
      # Parse the XML data
      root = ET.fromstring(res.text)

      # Make a list of the pastes
      pastes = []
      # Get all the xml pastes
      for paste in root.findall('paste'):
        # Set up the dict for paste parser crap
        paste_data = {
          'paste_key': paste.find('paste_key').text,
          'paste_date': paste.find('paste_date').text,
          'paste_title': paste.find('paste_title').text or '',
          'paste_size': paste.find('paste_size').text,
          'paste_expire_date': paste.find('paste_expire_date').text,
          'paste_private': paste.find('paste_private').text,
          'paste_format_long': paste.find('paste_format_long').text or '',
          'paste_format_short': paste.find('paste_format_short').text,
          'paste_url': paste.find('paste_url').text,
          'paste_hits': paste.find('paste_hits').text
        }
        # Append it to pastes list
        pastes.append(paste_data)

      return pastes
    else:
      return False

  # This lets you delete a paste (API Key needed)
  def delete_paste(self, url:str):
    # Check if the url is url or an id
    if url.startswith("https://") or url.startswith("http://"):
      # Get paste id from url
      paste_id = Pastelib(self.api_key).get_paste_id(url)
    else:
      # Set the url as the paste_id
      paste_id = url
    # All the paste data
    data = {
      "api_dev_key": self.api_key,
      "api_user_key": self.user_key,
      "api_option": "delete",
      "api_paste_key": paste_id
    }
    # Send the post request to the api
    res = requests.post("https://pastebin.com/api/api_post.php", data=data)
    # All the checks
    try:
      # Check if work
      if res.status_code == 200:
        return True
      else:
        return False
    # Big fail
    except Exception:
      return False

  def get_user_info(self):
    # Set all the paste data
    data = {
      "api_dev_key": self.api_key,
      "api_user_key": self.user_key,
      "api_option": "userdetails"
    }

    # Send post request
    res = requests.post("https://pastebin.com/api/api_post.php", data=data)
    # Request check
    if res.status_code == 200:
      # Parse the XML data
      root = ET.fromstring(res.text)

      # Extract the user data into a dict
      user_data = {
        'user_name': root.find('user_name').text,
        'user_format_short': root.find('user_format_short').text,
        'user_expiration': root.find('user_expiration').text,
        'user_avatar_url': root.find('user_avatar_url').text,
        'user_private': root.find('user_private').text,
        'user_website': root.find('user_website').text or '',
        'user_email': root.find('user_email').text,
        'user_location': root.find('user_location').text or '',
        'user_account_type': root.find('user_account_type').text
      }

      # Return the data
      return user_data
    else:
      return False

  def get_private_paste(self, url:str, json:bool=False):
    # Get the paste id
    if url.startswith("https://") or url.startswith("http://"):
      paste_id = Pastelib(self.api_key).get_paste_id(url)
    else:
      # Setting the url as the paste id
      paste_id = url

    # Set all the paste data
    data = {
      "api_dev_key": self.api_key,
      "api_user_key": self.user_key,
      "api_paste_key": paste_id,
      "api_option": "show_paste"
    }

    # Send the get request
    res = requests.post(f"https://pastebin.com/api/api_raw.php", data=data)

    # Check if the request actually worked correctly
    if res.status_code == 200:
      # Check if the request is a json response by the user
      if json == False:
        # Return the paste as text
        return res.text
      else:
        # Return the paste as json
        return res.json()
    else:
      # If it fails return false
      return False