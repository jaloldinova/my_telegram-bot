                    #REMINDER BOT
import asyncio
import sqlite3
import datetime
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

TOKEN = "8521459442:AAHuG9X6sdbM-j3KG10Hkzc84ImsycxiLvI"

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

def save_db():
    conn = sqlite3.connect("reminder.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminder (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sana Varchar(200),
            vaqt Varchar(200),
        )
    """)
    cursor.execute("""
    INSERT INTO reminder (sana, vaqt)
    VALUES (sana, vaqt)
    """)
    conn.commit()
    conn.close()


def save_db(sana: str, vaqt: str):
    conn = sqlite3.connect("reminder.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reminder (sana, vaqt) VALUES (?, ?)",
        (sana, vaqt)
    )
    conn.commit()
    conn.close()

class ReminderState(StatesGroup):
    sana = State()
    vaqt = State()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Assalomu alaykum!  Reminder botiga xush kelibsiz")

@dp.message(Command("reminder"))
async def reminder_start(message: Message, state: FSMContext):
    await message.answer(" Sanani kiriting ")
    await state.set_state(ReminderState.sana)

@dp.message(ReminderState.sana)
async def get_sana(message: Message, state: FSMContext):
    await state.update_data(sana=message.text)
    await message.answer(" Vaqtni kiriting ")
    await state.set_state(ReminderState.vaqt)

@dp.message(ReminderState.vaqt)
async def get_vaqt(message: Message, state: FSMContext):
    data = await state.get_data()
    sana = data["sana"]
    vaqt = message.text

    save_db(sana, vaqt)

    await message.answer(f" Reminder saqlandi:\n Sana: {sana}\n Vaqt: {vaqt}")
    await state.clear()

async def main():
    save_db()
    print(" Bot ishga tushdi!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())