from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from configurebot import cfg

mainmenunewsupport = KeyboardButton(cfg['button_new_question'])
mainmenuabout = KeyboardButton(cfg['button_about_us'])
mainmenurules = KeyboardButton(cfg['button_rules'])
mainmenucatalog = KeyboardButton(cfg['button_catalog'])
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenunewsupport, mainmenuabout)
mainmenu.row(mainmenurules, mainmenucatalog)

btnreviews = InlineKeyboardButton(text='ОТЗЫВЫ', url='https://t.me/KRIP4IK1/12/13')
reviewsmenu = InlineKeyboardMarkup(row_width=1)
reviewsmenu.insert(btnreviews)

btnUrlChannel = InlineKeyboardButton(text='ПОДПИСАТЬСЯ', url='https://t.me/kripchik5')
btnDoneSub = InlineKeyboardButton(text='ПОДПИСАЛСЯ', callback_data='subchanneldone')

checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.insert(btnUrlChannel)
checkSubMenu.insert(btnDoneSub)
