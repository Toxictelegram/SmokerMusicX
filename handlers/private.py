import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bb7e6f59b3db29b215446.jpg",
        caption=f"""**ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ ðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð ðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð ððð¯ðð¥ð¨ð©ðð ðð² = [Toxic ð¬â¤ï¸](https://t.me/its_toxicop)

ðð«ððð­ð¨ð« :- [â¨ TOXICð¬ ð](https://t.me/its_toxicop)
ðð®ð©ð©ð¨ð«ð­ :- [â¨ Dangerous ðð¼ð§ð â¤ï¸ð¸](https://t.me/DANGEROUSFIGHTER)
ðð¢ð¬ðð®ð¬ð¬ :- [â¨  Dangerous ðð¹ð®ð» ð§](https://t.me/Dangerousfighters)
ðð¨ð®ð«ðð  :- [â¨  ðð¹ð¶ð°ð¸ âï¸ ð¥ð²ð½ð¼ ð](https://t.me/its_toxicop)
ðð¨ð¦ð¦ðð§ð :- [â¨ðð¹ð¶ð°ð¸ âï¸ ð¡ð¼ð ð©](https://t.me/its_toxicop)
ððððð¢ð§ð 'ð :- [â¨ ðð¼ð¶ð» â¤ï¸ð¥](https://t.me/DANGEROUSFIGHTER)

ðð ðð¨ð® ððð¯ð ðð§ð² ðð®ðð¬ð­ð¢ð¨ð§ð¬ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð¨ð¬ð¬ = [TOXIC ð¬ â¤ï¸](https://t.me/its_toxicop)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ Já´ÉªÉ´ Há´Êá´ & Sá´á´á´á´Êá´ â¨", url=f"https://t.me/DANGEROUSFIGHTER")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6886f2463b4da4887458a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ CÊÉªá´á´ Má´ Tá´ Gá´á´ Rá´á´á´ ð", url=f"https://t.me/DANGEROUSFIGHTER")
                ]
            ]
        ),
    )
