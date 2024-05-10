from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from configurebot import cfg

mainmenunewsupport = KeyboardButton(cfg['button_new_question'])
mainmenuabout = KeyboardButton(cfg['button_about_us'])
mainmenurules = KeyboardButton(cfg['button_rules'])
mainmenucatalog = KeyboardButton(cfg['button_catalog'])
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenunewsupport, mainmenuabout)
mainmenu.row(mainmenurules, mainmenucatalog)