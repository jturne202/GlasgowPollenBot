import urllib.request, json, tweepy

tweet = ""

# Retrieve pollon data
with urllib.request.urlopen("https://api.breezometer.com/pollen/v2/forecast/daily?lat=55.861474&lon=-4.253737&key=YOUR_KEY_HERE&days=1") as url:
    data = json.loads(url.read().decode())
    
    # Parse data and create tweet content
    for t, v in data["data"][0]["types"].items():
        if v["data_available"]:
            line = v["display_name"] + ": " + v["index"]["category"] + "\n"
            tweet += line
        else:
            line = v["display_name"] + ": Assumed none"
            tweet += line

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Tweet the pollon count
api.update_status(tweet)
