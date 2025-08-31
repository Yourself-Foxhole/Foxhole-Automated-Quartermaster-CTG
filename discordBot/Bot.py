import disnake, logging

logger = logging.getLogger("Bot")

class DiscordBot(disnake.Client):
	intents = disnake.Intents.default()
	intents.message_content = True
	async def on_ready(self):
		logger.info(f"Logged as : {self.user}")
	async def on_message(self, message):
		logger.info(f"Message from {message.author} : {message.content}")

