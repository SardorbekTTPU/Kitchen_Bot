from collections import OrderedDict
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery, InputMediaPhoto, Message
from keyboards.inline.taomlar import buyrtma_buttons
from loader import dp, Database as db


@dp.callback_query_handler(text=["add", 'delete'], state="*")
async def add_product(query: CallbackQuery):
    reply_markup = query.message.reply_markup
    item_count = reply_markup.inline_keyboard[0][1].text
    item_count = int(item_count) + 1 if query.data == 'add' else int(item_count) - 1
    item_id = reply_markup.inline_keyboard[1][0].callback_data.replace('AddBasket#', '')
    try:
        if item_count > 0:
            await query.message.edit_media(InputMediaPhoto(
                query.message.photo[-1].file_id,
                caption=query.message.html_text
            ),
                reply_markup=buyrtma_buttons(item_id, item_count))
    except:
        pass
    await query.answer(cache_time=0)
#4

@dp.callback_query_handler(text_startswith="AddBasket", state="*")
async def add_basket(call: CallbackQuery):
    name = call.data.split("#")[1]
    reply_markup = call.message.reply_markup
    item_count = reply_markup.inline_keyboard[0][1].text
    exist_product = await db.get("select * from basket where product_name=%s", name)
    if len(exist_product) > 0:
        await db.apply("update basket set quantity=%s where user_id=%s", (item_count, call.from_user.id))
    else:
        await db.apply("insert into basket (product_name, user_id, quantity, price) values (%s, %s, %s, %s)", (name, call.from_user.id, item_count, price))
    await call.answer("Savatka joylandi", show_alert=True)


@dp.message_handler(text="📥 Korzina", state="*")
async def my_basket(message: Message):
    user = await db.user_data(telegram_id=message.from_user.id)
    products = await db.selected_products(user_id=message.from_user.id)
    text = ""
    for product in products:
        text += f"{product.get('product_name')}\n"
    full_name = user.get("full_name")
    await message.answer(f"<b> User: {full_name} </b>\n\n"
                             f"{text}")



