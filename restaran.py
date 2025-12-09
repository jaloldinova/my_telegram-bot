import asyncio
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = "8021887735:AAFBYbUe_6WUCVTjkjgm130H-4i5cmwxaIE"

storage = MemoryStorage()
dp = Dispatcher(storage=storage)


def save_db(ism: str, nomi: str, narxi: str, joyi: str, ichimliklar: str):
    conn = sqlite3.connect("restaran.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaran (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ism TEXT NOT NULL,
            nomi TEXT NOT NULL,
            narxi TEXT NOT NULL,
            joyi TEXT NOT NULL,
            ichimliklar TEXT NOT NULL
        )
    """)
    # BU YERDA XATO BOR EDI: ustunlar soni va qiymatlar soni teng emas edi
    cursor.execute(
        "INSERT INTO restaran (ism, nomi, narxi, joyi, ichimliklar) VALUES (?, ?, ?, ?, ?)",
        (ism, nomi, narxi, joyi, ichimliklar)
    )
    conn.commit()
    conn.close()


class RegisterStates(StatesGroup):
    ism = State()
    nomi = State()
    narxi = State()
    joyi = State()
    ichimliklar = State()


# YANGI OVQAT TANLASH TUGMALARI (restorandagidek)
ovqat_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Palov", callback_data="Palov")],
        [InlineKeyboardButton(text="Mastava", callback_data="Mastava")],
    ]
)

ichimliklar_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Fanta 🍷", callback_data="Fanta")],
        [InlineKeyboardButton(text="Choy 🫖", callback_data="Choy")],
    ]
)

joyi_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Joy 1", callback_data="Joy 1")],
        [InlineKeyboardButton(text="Joy 2", callback_data="Joy 2")],
        [InlineKeyboardButton(text="Joy 3", callback_data="Joy 3")],
        [InlineKeyboardButton(text="Joy 4", callback_data="Joy 4")],
        [InlineKeyboardButton(text="Joy 5", callback_data="Joy 5")],
    ]
)

narxi_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Palov - 50 000", callback_data="50000")],
        [InlineKeyboardButton(text="Mastava - 30 000", callback_data="30000")],
        [InlineKeyboardButton(text="Fanta - 20 000", callback_data="20000")],
        [InlineKeyboardButton(text="Choy - 10 000", callback_data="10000")],
    ]
)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Assalomu alaykum! Restoran botiga xush kelibsiz."
        "Buyurtma berish uchun /register buyrug'ini yuboring."
    )


@dp.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(RegisterStates.ism)


@dp.message(RegisterStates.ism)
async def ism(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    # BU YERDA DAVOMI YO'Q EDI, STATE O'ZGARMAY QOLIB KETARDI
    await message.answer("Ovqatni tanlang:", reply_markup=ovqat_markup)
    await state.set_state(RegisterStates.nomi)


@dp.callback_query(RegisterStates.nomi)
async def nomi(callback: CallbackQuery, state: FSMContext):
    food = callback.data
    await state.update_data(nomi=food)
    await callback.message.edit_text(f"Tanlangan ovqat: {food}")
    await callback.message.answer("Ovqat narxini tanlang:", reply_markup=narxi_markup)
    await state.set_state(RegisterStates.narxi)
    await callback.answer()


@dp.callback_query(RegisterStates.narxi)
async def narxi(callback: CallbackQuery, state: FSMContext):
    price = callback.data
    await state.update_data(narxi=price)
    await callback.message.edit_text(f"Tanlangan narx: {price} so'm")
    await callback.message.answer("Joyni tanlang:", reply_markup=joyi_markup)
    await state.set_state(RegisterStates.joyi)
    await callback.answer()


@dp.callback_query(RegisterStates.joyi)
async def joyi(callback: CallbackQuery, state: FSMContext):
    place = callback.data
    await state.update_data(joyi=place)
    await callback.message.edit_text(f"Tanlangan joy: {place}")
    await callback.message.answer("Ichimlikni tanlang:", reply_markup=ichimliklar_markup)
    await state.set_state(RegisterStates.ichimliklar)
    await callback.answer()


@dp.callback_query(RegisterStates.ichimliklar)
async def ichimliklar(callback: CallbackQuery, state: FSMContext):
    drink = callback.data
    await state.update_data(ichimliklar=drink)

    data = await state.get_data()
    ism = data.get("ism")
    nomi = data.get("nomi")
    narxi = data.get("narxi")
    joyi = data.get("joyi")
    ichimliklar_value = data.get("ichimliklar")

    save_db(ism, nomi, narxi, joyi, ichimliklar_value)

    text = (
        "Hurmatli mijoz buyurtmangiz qabul qilindi!\n"
        f"Ism: {ism}\n"
        f"Ovqat: {nomi}\n"
        f"Narxi: {narxi} so'm\n"
        f"Joy: {joyi}\n"
        f"Ichimlik: {ichimliklar_value}\n"
    )

    await callback.message.edit_text(text)
    await state.clear()
    await callback.answer("Hurmatli mijoz buyurtmalaringiz  saqlandi!😇")


async def main():
    bot = Bot(TOKEN)
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
