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

btnclashroyale = InlineKeyboardButton(text='Clash Royale', callback_data='clash_royale_action')
btnsupersus = InlineKeyboardButton(text='Super Sus', callback_data='super_sus_action')
btnpbgmb = InlineKeyboardButton(text='Pubg Mobile', callback_data='pubg_mobile_action')
btnclashofclans = InlineKeyboardButton(text='Clash of Clans', callback_data='clash_of_clans_action')
btnbrawlstars = InlineKeyboardButton(text='Brawl Stars', callback_data='brawl_stars_action')
catalogmenu = InlineKeyboardMarkup(row_width=1)
catalogmenu.row(btnclashroyale, btnsupersus)
catalogmenu.row(btnpbgmb, btnclashofclans)
catalogmenu.insert(btnbrawlstars)

clashroyale_products = InlineKeyboardMarkup(row_width=1)
clashroyale_product1 = InlineKeyboardButton(text='80 гемов', callback_data='clashroyale_product1_action')
clashroyale_product2 = InlineKeyboardButton(text='500 гемов', callback_data='clashroyale_product2_action')
clashroyale_product3 = InlineKeyboardButton(text='1200 гемов', callback_data='clashroyale_product3_action')
clashroyale_product4 = InlineKeyboardButton(text='2500 гемов', callback_data='clashroyale_product4_action')
clashroyale_product5 = InlineKeyboardButton(text='6500 гемов', callback_data='clashroyale_product5_action')
clashroyale_product6 = InlineKeyboardButton(text='14000 гемов', callback_data='clashroyale_product6_action')
clashroyale_product7 = InlineKeyboardButton(text='Diamond pass', callback_data='clashroyale_product7_action')
clashroyale_product8 = InlineKeyboardButton(text='Gold pass', callback_data='clashroyale_product8_action')
clashroyale_products.row(clashroyale_product1, clashroyale_product2, clashroyale_product3)
clashroyale_products.row(clashroyale_product4, clashroyale_product5, clashroyale_product6)
clashroyale_products.row(clashroyale_product7, clashroyale_product8)
