from handlers.client import *
from configurebot import cfg
import kb
from bans import banned_users


errormessage = cfg['error_message']
devid = cfg['dev_id']


def extract_arg(arg):
    return arg.split()[1:]


async def admin_ot(message: types.Message):
    if message.chat.id == tehchatid:
        try:
            uid = message.from_user.id
            args = extract_arg(message.text)

            if len(args) >= 2:
                chatid = str(args[0])
                args.pop(0)
                answer = ""
                for ot in args:
                    answer += ot + " "
                await message.reply('✅ Вы успешно ответили на вопрос!')
                await bot.send_message(chatid, f"✉ Новое уведомление!\nОтвет от тех.поддержки:\n\n{answer}",
                                       parse_mode='Markdown')
                return
            else:
                await message.reply('⚠ Укажите аргументы команды\nПример: `/ответ 516712732 Ваш ответ`',
                                    parse_mode='Markdown')
                return
        except Exception as e:
            cid = message.chat.id
            await message.answer(f"{errormessage}",
                                 parse_mode='Markdown')
            await bot.send_message(devid, f"Случилась *ошибка* в чате *{cid}*\nСтатус ошибки: `{e}`",
                                   parse_mode='Markdown')
    else:
        return


async def admin_ban(message: types.Message):
    if message.chat.id == tehchatid:
        try:
            uidown = message.from_user.id
            args = extract_arg(message.text)
            if len(args) == 2:
                uid = int(args[0])
                reason = args[1]
                if uid:
                    banned_users[uid] = True
                    await message.reply(f'✅ Вы успешно забанили этого пользователя\nПричина: `{reason}`',
                                        parse_mode='Markdown')

                    await bot.send_message(uid, f"⚠ Администратор *заблокировал* Вас в боте\nПричина: `{reason}`",
                                           parse_mode='Markdown')
                    return
                else:
                    await message.reply("⚠ Этого пользователя *не* существует!", parse_mode='Markdown')
                    return
            else:
                await message.reply('⚠ Укажите аргументы команды\nПример: `/бан 51623722 Причина`',
                                    parse_mode='Markdown')
                return
        except Exception as e:
            cid = message.chat.id
            await message.answer(f"{errormessage}",
                                 parse_mode='Markdown')
            await bot.send_message(devid, f"Случилась *ошибка* в чате *{cid}*\nСтатус ошибки: `{e}`",
                                   parse_mode='Markdown')
    else:
        return


async def admin_unban(message: types.Message):
    if message.chat.id == tehchatid:
        try:
            uidown = message.from_user.id
            args = extract_arg(message.text)
            if len(args) == 1:
                uid = int(args[0])
                if uid:
                    del banned_users[uid]
                    await message.reply(f'✅ Вы успешно разблокировали этого пользователя', parse_mode='Markdown')
                    await bot.send_message(uid, f"⚠ Администратор *разблокировал* Вас в боте!", parse_mode='Markdown')
                    return
                else:
                    await message.reply("⚠ Этого пользователя *не* существует!", parse_mode='Markdown')
                    return
            else:
                await message.reply('⚠ Укажите аргументы команды\nПример: `/разбан 516272834`',
                                    parse_mode='Markdown')
                return
        except Exception as e:
            cid = message.chat.id
            await message.answer(f"{errormessage}",
                                 parse_mode='Markdown')
            await bot.send_message(devid, f"Случилась *ошибка* в чате *{cid}*\nСтатус ошибки: `{e}`",
                                   parse_mode='Markdown')
    else:
        return


def register_handler_admin():
    dp.register_message_handler(admin_ot, commands=['ответ', 'ot'])
    dp.register_message_handler(admin_ban, commands=['бан', 'ban'])
    dp.register_message_handler(admin_unban, commands=['разбан', 'unban'])