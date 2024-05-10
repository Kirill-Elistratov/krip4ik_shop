from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import bot, dp
from configurebot import cfg

tehchatid = cfg['teh_chat_id']
message_seneded = cfg['question_ur_question_sended_message']
sleep_mod = cfg['sleep']

class FSMQuestion(StatesGroup):
    text = State()


# Обработчики
async def newquestion(message: types.Message, state: FSMContext):
    global sleep_mod
    async with state.proxy() as data:
        if message.content_type == 'photo':
            data['text'] = message.caption
        else:
            data['text'] = message.text
    await state.finish()
    if message.chat.username == None:
        who = "Ник не установлен"
    else:
        who = "@" + message.chat.username.replace('_', r'\_')
    question = data['text']
    if message.content_type == 'photo':
        ph = message.photo[0].file_id

        if sleep_mod:
            await message.reply(
                f'✉ Ваш вопрос был отослан\n'
                f'❗НО техподдержка сейчас спит, когда проснётся, то обязательно ответит.❗'
            )
        else:
            await message.reply(f"{message_seneded}", parse_mode='Markdown')

        await bot.send_photo(tehchatid, ph,
                             caption=f"✉ | Новый вопрос\nОт: {who}\nВопрос: `{data['text']}`\n\n📝 Чтобы ответить на вопрос введите `/ответ {message.chat.id} Ваш ответ`",
                             parse_mode='Markdown')
    else:
        if sleep_mod:
            await message.reply(
                f'✉ Ваш вопрос был отослан\n'
                f'❗НО техподдержка сейчас спит, когда проснётся, то обязательно ответит.❗'
            )
        else:
            await message.reply(f"{message_seneded}", parse_mode='Markdown')

        await bot.send_message(tehchatid,
                               f"✉ | Новый вопрос\nОт: {who}\nВопрос: `{data['text']}`\n\n📝 Чтобы ответить на вопрос введите `/ответ {message.chat.id} Ваш ответ`",
                               parse_mode='Markdown')


async def sleep(message: types.Message):
    global sleep_mod
    if message.chat.id == tehchatid:
        sleep_mod = True
        await message.reply('Спим')
    else:
        return