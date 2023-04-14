from aiogram import types, Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State

API  = '6139125398:AAGwqoWTEeKhpkLJcrXoLSyBclk_3texRVg'
bot = Bot(API)
dp = Dispatcher(bot, storage=MemoryStorage())

class Charachter():
    name = State()
    protect = State()
    attack = State()
    speed = State()


@dp.message_handlers(commads=['save'])
async def save_charachter(message: types.Message):
    await message.answer('кидай имя персоанажа')
    await Charachter.name.set()
#
# @dp.message_handlers(state=Charachter.name)
# async def save_name(message: types.Message, state: FSMContext):
#     # async with state.proxy() as data:



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)