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