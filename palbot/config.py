import os

# Get the bot token directly from Railway environment variables
TOKEN = os.environ.get("DISCORD_TOKEN")

if TOKEN is None:
    # This shows up in Railway logs if the variable is missing
    raise ValueError("❌ DISCORD_TOKEN is not set in Railway Variables!")
