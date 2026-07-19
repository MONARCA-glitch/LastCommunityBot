import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

LANG_BUTTONS = types.InlineKeyboardMarkup(row_width=2)
LANG_BUTTONS.add(
    types.InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
    types.InlineKeyboardButton("🇮🇹 Italiano", callback_data="lang_it"),
    types.InlineKeyboardButton("🇮🇷 فارسی", callback_data="lang_fa"),
    types.InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar"),
    types.InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
)

@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def welcome_new_member(message: types.Message):
    for user in message.new_chat_members:
        await bot.send_message(
            chat_id=message.chat.id,
            text="Welcome to the Last Community.\nPlease select your language.",
            reply_markup=LANG_BUTTONS
        )

@dp.callback_query_handler(lambda c: c.data.startswith("lang_"))
async def process_language_choice(callback_query: types.CallbackQuery):
    lang = callback_query.data.split("_")[1]
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.message.chat.id,
        text=f"Language set: {lang.upper()}.\nRules and main menu will be here..."
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
