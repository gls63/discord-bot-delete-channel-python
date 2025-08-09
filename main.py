import disnake
from disnake.ext import commands
import logging
import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s — %(levelname)s — %(message)s")

bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all())

@bot.event
async def on_ready():
    logging.info(f"Logging in as Bot {bot.user} (ID: {bot.user.id})")
    await bot.load_extension("cogs.dora")
    logging.info("Cog dora loaded.")

bot.run(config.token)
