# config.py
def load_config():
    config = {}
    with open('config.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            config[key] = value
    return config

config = load_config()
API_TOKEN = config['API_TOKEN']
CHANNEL_ID = config['CHANNEL_ID']
