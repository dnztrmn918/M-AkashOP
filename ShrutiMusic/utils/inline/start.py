# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com

import config
from ShrutiMusic import app
from pyrogram.types import InlineKeyboardButton

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],  # Add Bot To Group
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"],  # Developer
                url=f"https://t.me/{config.OWNER_USERNAME}"
            ),
            InlineKeyboardButton(
                text=_["S_B_11"],  # About
                callback_data="about_page"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],  # Help/Commands
                callback_data="help_page_1"
            )
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],  # Add Bot To Group
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"],  # Developer
                url=f"https://t.me/{config.OWNER_USERNAME}"
            ),
            InlineKeyboardButton(
                text=_["S_B_11"],  # About
                callback_data="about_page"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],  # Help/Commands
                callback_data="help_page_1"
            )
        ],
    ]
    return buttons

def about_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper")
        ]
    ]
    return buttons
