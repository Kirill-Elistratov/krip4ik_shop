import kb
from configurebot import cfg
from bans import banned_users

welcomemessage = cfg['welcome_message']
errormessage = cfg['error_message']
devid = cfg['dev_id']
aboutus = cfg['about_us']
question_first_msg = cfg['question_type_ur_question_message']
x = cfg['x']

handler_button_new_question = cfg['button_new_question']
handler_button_about_us = cfg['button_about_us']
handler_button_rules = cfg['button_rules']
handler_button_catalog = cfg['button_catalog']

channel_username = cfg['tgk_id']
NOTSUBMSG = cfg['not_sub_message']
ban_message = cfg['ban_message']


def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] == 'left':
        return False
    else:
        return True


async def client_start(message: types.Message):
    try:
        if message.chat.type != 'private':
            await message.answer('Данную команду можно использовать только в личных сообщениях с ботом.')
        else:
            if check_sub_channel(await bot.get_chat_member(chat_id=channel_username, user_id=message.from_user.id)):
                user_id = message.from_user.id
                if user_id in banned_users and banned_users[user_id]:
                    await message.answer(f'{ban_message}', parse_mode="Markdown")
                else:
                    await message.answer(f'{welcomemessage}', reply_markup=kb.mainmenu)
            else:
                await message.answer(f'{NOTSUBMSG}', reply_markup=kb.checkSubMenu)
    except Exception as e:
        cid = message.chat.id
        await message.answer(f"{errormessage}", parse_mode='Markdown')
        await bot.send_message(devid, f"Случилась *ошибка* в чате *{cid}*\nСтатус ошибки: {e}", parse_mode='Markdown')


async def client_newquestion(message: types.Message):
    try:
        if message.text == handler_button_new_question:
            if check_sub_channel(await bot.get_chat_member(chat_id=channel_username, user_id=message.from_user.id)):
                user_id = message.from_user.id
                if user_id in banned_users and banned_users[user_id]:
                    await message.answer(f'{ban_message}', parse_mode="Markdown")
                else:
                    await message.answer(f"{question_first_msg}")
                    await FSMQuestion.text.set()
                    if sleep_mod == True and message.chat.id != tehchatid:
                        await bot.send_message(chat_id=message.chat.id)
            else:
                await message.answer(f'{NOTSUBMSG}', reply_markup=kb.checkSubMenu)
        elif message.text == handler_button_about_us:
            if check_sub_channel(await bot.get_chat_member(chat_id=channel_username, user_id=message.from_user.id)):
                user_id = message.from_user.id
                if user_id in banned_users and banned_users[user_id]:
                    await message.answer(f'{ban_message}', parse_mode="Markdown")
                else:
                    await message.answer(f"{aboutus}", reply_markup=kb.reviewsmenu)
            else:
                await message.answer(f'{NOTSUBMSG}', reply_markup=kb.checkSubMenu)
        elif message.text == handler_button_rules:
            if check_sub_channel(await bot.get_chat_member(chat_id=channel_username, user_id=message.from_user.id)):
                user_id = message.from_user.id
                if user_id in banned_users and banned_users[user_id]:
                    await message.answer(f'{ban_message}', parse_mode="Markdown")
                else:
                    await message.answer('''1. Следовать инструкциям бота 🧭
2. Писать боту исключительно в целях покупки товара 🛒
3. Не спамить повторяющимися запросами или сообщениями. Нарушение правила - бан на 24 часа, последующее нарушение правила - бан навсегда ☠
4. Мат в меру, нарушение правила - бан на 24 часа, последующее нарушение правила - бан навсегда ☠
5. Незнание правил не освобождает от ответственности)''')
            else:
                await message.answer(f'{NOTSUBMSG}', reply_markup=kb.checkSubMenu)

    except Exception as e:
        cid = message.chat.id
        await message.answer(f"{errormessage}",
                             parse_mode='Markdown')
        await bot.send_message(devid, f"Случилась *ошибка* в чате *{cid}*\nСтатус ошибки: `{e}`",
                               parse_mode='Markdown')


async def client_getgroupid(message: types.Message):
    try:
        await message.answer(f"Chat id is: *{message.chat.id}*\nYour id is: *{message.from_user.id}*",
                             parse_mode='Markdown')
    except Exception as e:
        cid = message.chat.id
        await message.answer(f"{errormessage}",
                             parse_mode='Markdown')
        await bot.send_message(devid, f"Случилась *ошибка* в чате *{cid}*\nСтатус ошибки: `{e}`",
                               parse_mode='Markdown')