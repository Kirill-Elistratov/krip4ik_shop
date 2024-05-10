from bot import dp
from aiogram.utils import executor
from handlers import client, admin, fsm, callbacks


admin.register_handler_admin()
fsm.register_handler_FSM()
client.register_handler_client()
callbacks.register_handler_callbacks()


executor.start_polling(dp, skip_updates=True)