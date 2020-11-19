# tweepy-bot

[1] install package
```
pip install -r requirements.txt
```
or
```
pip install tweepy
```

[2] Copy env-sample.py to create env.py

[3] Update the values of "CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_TOKEN" and "ACCESS_TOKEN_SECRET" in the created env.py.
```
def set_env():
  os.environ["CONSUMER_KEY"] = "CONSUMER_KEY"
  os.environ["CONSUMER_SECRET"] = "CONSUMER_SECRET"
  os.environ["ACCESS_TOKEN"] = "ACCESS_TOKEN"
  os.environ["ACCESS_TOKEN_SECRET"] = "ACCESS_TOKEN_SECRET"
```

[4] Run a bot with the following command
```
python index.py
```
