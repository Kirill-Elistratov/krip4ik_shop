from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import bot, dp
from configurebot import cfg

tehchatid = cfg['teh_chat_id']
message_seneded = cfg['question_ur_question_sended_message']
sleep_mod = cfg['sleep']