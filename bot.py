from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import configurebot
import aiohttp

proxy_url = 'http://proxy.server:3128'

storage = MemoryStorage()
bot = Bot(token=configurebot.cfg['token'], proxy=proxy_url)
dp = Dispatcher(bot, storage=storage)
