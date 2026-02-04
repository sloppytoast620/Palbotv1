import os

# Railway provides this variable directly to the OS
TOKEN = os.environ.get("DISCORD_TOKEN")

if TOKEN is None:
    # This helps catch the TypeError before it happens
    raise ValueError("MY_TOKEN is not set in Railway variables!")
