from aiogram import types, Router

echo_router = Router()

@echo_router.message()
async def echo(message: types.Message) -> types.Message:
    """
    Функция отвечает на сообщение от пользователя если сообщение не распознана как команда.
    """
    await message.answer('Неизвестная команда! \n'
                         'Воспользуйтесь меню или нажмите команду /start')
