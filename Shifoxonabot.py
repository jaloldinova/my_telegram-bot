# clinic_bot.py
import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8503560803:AAEjZVro35VVF7V8Y9Y54nEWzgoFWw9nnjA"
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
def connect():
    conn = sqlite3.connect("clinic.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS doctors(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            specialty TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS consultations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_id INTEGER,
            patient_id INTEGER,
            question TEXT,
            answer TEXT
        )
    """)
    conn.commit()
    return conn

def add_doctor(user_id, name, specialty):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO doctors (user_id, name, specialty) VALUES (?, ?, ?)",
                (user_id, name, specialty))
    conn.commit()

def get_doctors():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, specialty FROM doctors")
    return cur.fetchall()

def add_patient(user_id, name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO patients (user_id, name) VALUES (?, ?)", (user_id, name))
    conn.commit()

def create_consultation(doctor_id, patient_id, question):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO consultations (doctor_id, patient_id, question) VALUES (?, ?, ?)",
                (doctor_id, patient_id, question))
    conn.commit()

def doctor_get_requests(doctor_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, question FROM consultations WHERE doctor_id=? AND answer IS NULL", (doctor_id,))
    return cur.fetchall()

def answer_request(consult_id, answer):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE consultations SET answer=? WHERE id=?", (answer, consult_id))
    conn.commit()
class DoctorStates(StatesGroup):
    name = State()
    specialty = State()

class PatientStates(StatesGroup):
    name = State()
    question = State()
    choose_doctor = State()
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👨‍⚕️ Shifokor bo‘lish", callback_data="doctor")],
        [InlineKeyboardButton(text="👤 Bemor bo‘lish", callback_data="patient")],
        [InlineKeyboardButton(text="💬 Konsultatsiya", callback_data="consult")]
    ])

def doctors_keyboard():
    kb = []
    for doc in get_doctors():
        kb.append([InlineKeyboardButton(text=f"{doc[1]} ({doc[2]})", callback_data=f"choose_{doc[0]}")])
    return InlineKeyboardMarkup(inline_keyboard=kb)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Salom! Onlayn shifokor konsultatsiya tizimiga xush kelibsiz.",
        reply_markup=main_menu()
    )
@dp.callback_query(lambda c: c.data=="doctor")
async def doctor_start(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Ismingizni kiriting:")
    await state.set_state(DoctorStates.name)

@dp.message(DoctorStates.name)
async def get_doctor_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Mutaxassisligingizni kiriting:")
    await state.set_state(DoctorStates.specialty)

@dp.message(DoctorStates.specialty)
async def get_doctor_specialty(message: types.Message, state: FSMContext):
    data = await state.get_data()
    add_doctor(user_id=message.from_user.id, name=data["name"], specialty=message.text)
    await message.answer("Siz shifokor sifatida ro'yxatdan o'tdingiz!")
    await state.clear()
@dp.callback_query(lambda c: c.data=="patient")
async def start_patient(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Ismingizni kiriting:")
    await state.set_state(PatientStates.name)

@dp.message(PatientStates.name)
async def save_patient(message: types.Message, state: FSMContext):
    add_patient(message.from_user.id, message.text)
    await message.answer("Shifokorga savolingizni yozing:")
    await state.set_state(PatientStates.question)

@dp.message(PatientStates.question)
async def get_question(message: types.Message, state: FSMContext):
    await state.update_data(question=message.text)
    await message.answer("Shifokorni tanlang:", reply_markup=doctors_keyboard())
    await state.set_state(PatientStates.choose_doctor)

@dp.callback_query(lambda c: c.data.startswith("choose_"))
async def choose_doctor(callback: types.CallbackQuery, state: FSMContext):
    doctor_id = int(callback.data.split("_")[1])
    data = await state.get_data()
    create_consultation(doctor_id=doctor_id, patient_id=callback.from_user.id, question=data["question"])
    await callback.message.answer("Savolingiz yuborildi. Shifokor javob beradi.")
    await state.clear()

@dp.callback_query(lambda c: c.data=="consult")
async def see_requests(callback: types.CallbackQuery):
    doctor_id = callback.from_user.id
    requests = doctor_get_requests(doctor_id)
    if not requests:
        await callback.message.answer("Sizga hozircha so‘rov yo‘q.")
        return
    for req in requests:
        await callback.message.answer(
            f"📩 Yangi so‘rov:\nID: {req[0]}\nSavol: {req[1]}\nJavob yuborish: /reply {req[0]} javob"
        )

@dp.message()
async def reply_handler(message: types.Message):
    if message.text and message.text.startswith("/reply"):
        try:
            _, consult_id, answer = message.text.split(" ", 2)
            consult_id = int(consult_id)
        except ValueError:
            await message.answer("Format: /reply ID javob")
            return
        answer_request(consult_id, answer)
        await message.answer("Javob yuborildi!")

async def main():
    print("✅ Bot ishga tushdi…")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
