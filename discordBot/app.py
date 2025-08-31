import os, sys, traceback
import logging, logging.config
from Bot import DiscordBot
from dotenv import load_dotenv
logging.config.fileConfig("./loggerConf.ini")
load_dotenv()
def main():
	try:
		logger.info("starting...")
		bot = DiscordBot(intents=DiscordBot.intents)
		bot.run(os.getenv("BOT_TOKEN"))
		return_val = os.X_OK

	except KeyboardInterrupt:
		logger.info("Quit...")
	except Exception as e:
		logger.error(f"[{OSError}] - {traceback.format_exc()}")
		if os.name == 'nt':
			return_val = 70
		else:
			return_val = os.EX_SOFTWARE
	finally:
		if return_val != os.X_OK:
			logger.info(f"exit with : {return_val} > {os.strerror(return_val)}")
		else:
			logger.info(f"exit with : {return_val} > Program end successfully")
		logger.info("===================   END   ===================")
		return return_val

if __name__ == "__main__":
	logger = logging.getLogger("main")
	logger.info("=================== CTG  BOT ===================")
	logger.info("===================  v0.0.0  ===================")
	sys.exit(main())