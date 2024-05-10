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