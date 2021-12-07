from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.admin_keyboards import menu_keyboards
from keyboards.default.register import phone
from states.admin import Admin
from states.registration import new_user
from data.config import ADMINS
from keyboards.default.menu import main_menu

from loader import dp, Database as db


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: Message):
    user = await db.check_user(message.from_user.id)
    if message.from_user.id in ADMINS:
        await message.answer("<b>Salom janob admin, xush kelibsiz!</b>", reply_markup=menu_keyboards)
        try:
            await db.apply("insert into admins(admin_id, username) values(%s, %s)", (message.from_user.id, message.from_user.username))
        except UnicodeEncodeError:
            pass
        await Admin.menu.set()
    elif user:
        await message.answer("Quyidagi buyruqlardan birini tanlang", reply_markup=main_menu)
        await new_user.bosh_menyu.set()
    else:
        await message.answer(f"<b>Salom, {message.from_user.full_name}!</b>\n\n"
                             f"<i>❗️Iltimos registratsiyadan o'tish uchun, telefon raqamingizni kiriting.</i>",
                             reply_markup=phone())
        await new_user.telephone.set()


@dp.message_handler(content_types=["contact"], state=new_user.telephone)
async def register(message: Message):
    await db.apply("insert into users(phone_number, full_name, telegram_id, username) values(%s, %s, %s, %s)",
                   (str(message.contact.phone_number), message.from_user.full_name, message.from_user.id, message.from_user.username))
    await message.answer("Quyidagi buyruqlar birini tanlang", reply_markup=main_menu)
    await new_user.bosh_menyu.set()
