import config
from ShrutiMusic import app
from pyrogram.types import InlineKeyboardButton

def start_panel(_):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true")],
        [InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/{config.OWNER_USERNAME}"), InlineKeyboardButton(text=_["S_B_11"], callback_data="about_page")],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="help_page_1")]
    ]
    return buttons

def private_panel(_):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true")],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="help_page_1")],
        [InlineKeyboardButton(text=_["L_N_G"], callback_data="LG"), InlineKeyboardButton(text=_["S_B_11"], callback_data="about_page")],
        [InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/{config.OWNER_USERNAME}")]
    ]
    return buttons

def about_panel(_):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL), InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP)],
        [InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper")]
    ]
    return buttons


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi