import kb
from handlers.client import *


async def handle_game_actions(callback_query: types.CallbackQuery):
    action = callback_query.data
    if action == 'clash_royale_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id, f'👇Выберите товар👇', reply_markup=kb.clashroyale_products)

    elif action == 'super_sus_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id, '👇Выберите товар👇')

    elif action == 'pubg_mobile_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id, '👇Выберите товар👇')

    elif action == 'clash_of_clans_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id, '👇Выберите товар👇')

    elif action == 'brawl_stars_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id, '👇Выберите товар👇')


async def handle_product_actions(callback_query: types.CallbackQuery):
    action = callback_query.data
    if action == 'clashroyale_product1_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id, '🛍Ваш товар: 80 гемов\n💰Цена: 10₽\n\n✅Вы выбрали товар👆')
    elif action == 'clashroyale_product2_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id,
                               '🛍Ваш товар: 500 гемов\n💰Цена: 20₽\n\n✅Вы выбрали товар👆')
    elif action == 'clashroyale_product3_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id,
                               '🛍Ваш товар: 1200 гемов\n💰Цена: 30₽\n\n✅Вы выбрали товар👆')
    elif action == 'clashroyale_product4_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id,
                               '🛍Ваш товар: 2500 гемов\n💰Цена: 40₽\n\n✅Вы выбрали товар👆')
    elif action == 'clashroyale_product5_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id,
                               '🛍Ваш товар: 6500 гемов\n💰Цена: 50₽\n\n✅Вы выбрали товар👆')
    elif action == 'clashroyale_product6_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id,
                               '🛍Ваш товар: 14000 гемов\n💰Цена: 60₽\n\n✅Вы выбрали товар👆')
    elif action == 'clashroyale_product7_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id,
                               '🛍Ваш товар: Diamond pass\n💰Цена: 70₽\n\n✅Вы выбрали товар👆')
    elif action == 'clashroyale_product8_action':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id,
                               '🛍Ваш товар: Gold pass\n💰Цена: 80₽\n\n✅Вы выбрали товар👆')


async def sub_channel_done(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_username, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, f'Введите /start ещё раз')
    else:
        await bot.send_message(message.from_user.id, f'{NOTSUBMSG}', reply_markup=kb.checkSubMenu)


def register_handler_callbacks():
    dp.register_callback_query_handler(handle_game_actions,
                                       lambda query: query.data in ['clash_royale_action', 'super_sus_action',
                                                                    'pubg_mobile_action', 'clash_of_clans_action',
                                                                    'brawl_stars_action'])
    dp.register_callback_query_handler(handle_product_actions, lambda query: query.data.startswith('clashroyale'))
    dp.register_callback_query_handler(sub_channel_done)
