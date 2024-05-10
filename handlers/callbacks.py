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