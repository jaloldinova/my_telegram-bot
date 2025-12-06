# import asyncio
#
# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
#
# TOKEN = "8010488853:AAGQnt4B-X2LChkQTaZjnPTgC8E54SSx8QY"
#
# bot = Bot(TOKEN)
# dp = Dispatcher()
#
# # STATES
# class RegisterStates(StatesGroup):
#     name = State()
#     age = State()
#     phone = State()
#     kurs = State()
#     tajriba = State()
#     vaqt = State()
#     confirm = State()
# # KURS TANLASH KNOPKALARI
# kurs_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Backend🥇", callback_data="backend")],
#         [InlineKeyboardButton(text="Frontend🌐", callback_data="frontend")],
#         [InlineKeyboardButton(text="SMM🎥", callback_data="smm")],
#         [InlineKeyboardButton(text="Grafik dizayn📈", callback_data="design")],
#     ]
# )
# tajriba_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Bor", callback_data="bor")],
#         [InlineKeyboardButton(text="Yo'q", callback_data="yoq")],
#     ]
# )
# vaqt_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="09:00–13:00", callback_data="09-13")],
#         [InlineKeyboardButton(text="14:00–18:00", callback_data="14-18")],
#     ]
# )
# confirm_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Tasdiqlayman✅", callback_data="confirm_yes")],
#         [InlineKeyboardButton(text="Bekor qilindi❌", callback_data="confirm_no")],
#     ]
# )
# @dp.message(Command("register"))
# async def start_register(message: Message, state: FSMContext):
#     await message.answer("Ismingizni kiriting:")
#     await state.set_state(RegisterStates.name)
# # GET ism
# @dp.message(RegisterStates.name)
# async def get_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer("Yoshingizni kiriting:")
#     await state.set_state(RegisterStates.age)
# # GET yosh
# @dp.message(RegisterStates.age)
# async def get_age(message: Message, state: FSMContext):
#     if not message.text.isdigit():
#         await message.answer("Yosh faqat son bo‘lishi kerak!")
#         return
#     await state.update_data(age=message.text)
#     await message.answer("Telefon raqamingizni kiriting:")
#     await state.set_state(RegisterStates.phone)
# #GET PHONE
# @dp.message(RegisterStates.phone)
# async def get_phone(message: Message, state: FSMContext):
#     await state.update_data(phone=message.text)
#     await message.answer("Qaysi kursni tanlaysiz?", reply_markup=kurs_markup)
#     await state.set_state(RegisterStates.kurs)
# #GET KURS
# @dp.callback_query(RegisterStates.kurs)
# async def get_kurs(callback: CallbackQuery, state: FSMContext):
#     await state.update_data(kurs=callback.data)
#     await callback.message.edit_text(
#         "Tajriba bormi?", reply_markup=tajriba_markup
#     )
#     await state.set_state(RegisterStates.tajriba)
# # GET TAJRIBA
# @dp.callback_query(RegisterStates.tajriba)
# async def get_tajriba(callback: CallbackQuery, state: FSMContext):
#     await state.update_data(tajriba=callback.data)
#     await callback.message.edit_text(
#         "Qaysi vaqtda o‘qimoqchisiz?", reply_markup=vaqt_markup
#     )
#     await state.set_state(RegisterStates.vaqt)
# #GET VAQT
# @dp.callback_query(RegisterStates.vaqt)
# async def get_time(callback: CallbackQuery, state: FSMContext):
#     await state.update_data(vaqt=callback.data)
#     data = await state.get_data()
#
#     text = (
#         "*Ro‘yxatdan o‘tish ma’lumotlari:*\n\n"
#         f"👤 Ism: *{data['name']}*\n"
#         f"🔢 Yosh: *{data['age']}*\n"
#         f"☎️ Telefon: *{data['phone']}*\n"
#         f"📚 Tanlangan kurs: *{data['kurs']}*\n"
#         f"🧪 Tajriba: *{data['tajriba']}*\n"
#         f"⏰ Vaqt: *{data['vaqt']}*\n\n"
#         "HURMATLI MIJOZ, MA'LUMOTLAR TO‘G‘RIMI?"
#     )
#
#     await callback.message.edit_text(
#         text,
#         reply_markup=confirm_markup,
#         parse_mode="Markdown"
#     )
#     await state.set_state(RegisterStates.confirm)
# @dp.callback_query(RegisterStates.confirm, lambda c: c.data == "confirm_yes")
# async def confirm_register(callback: CallbackQuery, state: FSMContext):
#     await callback.message.edit_text(
#         "*Tabriklaymiz!*\nSiz muvaffaqiyatli ro‘yxatdan o‘tdingiz.🤩",
#         parse_mode="Markdown"
#     )
#     await state.clear()
# @dp.callback_query(RegisterStates.confirm, lambda c: c.data == "confirm_no")
# async def cancel_register(callback: CallbackQuery, state: FSMContext):
#     await state.clear()
#     await callback.message.edit_text(
#         "Hurmatli mijoz, ma’lumotlar bekor qilindi❌\n"
#         "Iltimos, qayta /register orqali ro‘yxatdan o‘ting.↩️"
#     )
#
#
# async def main():
#     print("Bot ishga tushdi...")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())
                 # topshiriqlar
# from aiogram import Bot,Dispatcher,types
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.filters import Command
# from aiogram.fsm.state import StatesGroup,State
# bot=Bot(token='TOKEN')
# db=Dispatcher(storage=MemoryStorage())
# class RegisterStates(StatesGroup):
#     name=State()
#     age=State()
#     address=State()
# @db.message(Command("start"))
# async def start(message: types.Message):
#     await message.answer("Ismingizni kiriting:")
#     await state.set_state(RegisterState.name)
# @db.message(RegisterState.name)
# async def get_name(message: types.Message,state):
#     await state.update_data(name=message.text)
#     data=await state.get_data()
#     await message.answer(f"Xush kelibsiz,{data['name']}")
#     await
          # 39 guruh vazifalari
import asyncio
from idlelib.undo import Command
from aiogram import Dispatcher,Bot,types
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup,State
token="8010488853:AAGQnt4B-X2LChkQTaZjnPTgC8E54SSx8QY"
bot = Bot(token=token)
db=Dispatcher(storage=MemoryStorage())
class RegisterStates(StatesGroup):
    ism = State()
    yosh = State()
    manzil= State()
@db.message(Command("register"))
async def start_register(message: Message,state:FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(RegisterStates.ism)
@db.message(RegisterStates.ism)
async def get_name(message: Message,state:FSMContext):
    await state.update_data(ism=message.text)
    await message.answer("Yoshingizni kiriting")
    await state.set_state(RegisterStates.yosh)
@db.message(RegisterStates.manzil)
async def get_manzil(message: Message,state:FSMContext):
    await state.update_data(manzil=message.text)
    await message.answer("Manzilingizni kiriting")
    await state.set_state(RegisterStates.manzil)
#2
import json
def load_db():
    try:
        with open("fotima.json","r",encoding="utf-8") as file:
            return json.load(file)
    except:
        return{}
def save_db(data):
    with open("fotima.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
def ensure(user_id):
    data = load_db()
    user_id = str(user_id)
    if user_id not in data:
        data[user_id] = {}
        save_db(data)
    return data
@db.message(Command("foyda"))
async def foyda(message:types.Message):
    try:
        miqdor=int(message.text.split(" ")[1])
    except:
        return await message.answer("xatosiz yozing!:")
    data = ensure(message.from_user.id)
    data[str(message.from_user.id)]["balance"]+=miqdor
    save_db(data)
    await message.answer(f"Balansga {miqdor} qo'shildi!")
@db.message(Command("chiqim"))
async def chiqim(message:types.Message):
    try:
        miqdor=int(message.text.split(" ")[1])
    except:
        return await message.answer("xatosiz yozing!:")
    data = ensure(message.from_user.id)
    data[str(message.from_user.id)]["balance"]-=miqdor
    save_db(data)
    await message.answer(f"Balansdan {miqdor} ayirildi!")
@db.message(Command("balans"))
async def balans(message:types.Message):
    data = ensure(message.from_user.id)
    balance=data[str(message.from_user.id)]["balance"]
    await message.answer(f"Sizning balansingiz:{balance}")
    save_db(data)
async def main():
    print("Bot ishga tushdi...")
    await db.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

import sqlite3
def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """)

    conn.commit()
    return conn
def add_product(title, price):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO products (title, price) VALUES (?, ?)", (title, price))
    conn.commit()
    print(f"Mahsulot qo'shildi: {title} - {price} so'm")
def get_products():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, title, price FROM products")
    products = cur.fetchall()
    if not products:
        print("Mahsulotlar mavjud emas.")
        return
    print("\n--- Mahsulotlar ro‘yxati ---")
    for p in products:
        print(f"ID: {p[0]} | Nomi: {p[1]} | Narxi: {p[2]} so'm")
def update_price(product_id, new_price):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE products SET price=? WHERE id=?", (new_price, product_id))
    conn.commit()
    print(f"ID {product_id} mahsulot narxi {new_price} so'mga yangilandi.")
if __name__ == "__main__":
    connect()
    add_product("Olma", 7000)
    add_product("Non", 3000)
    get_products()
    update_price(1, 7500)
    get_products()

















