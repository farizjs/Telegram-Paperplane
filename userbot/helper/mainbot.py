#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon.tl.types import Channel

from userbot import *
from userbot import ALIVE_NAME, bot, BOT_VER as telever

# stats
if BOTLOG_CHATID:
    log = "Enabled"
else:
    log = "Disabled"

if BOT_USERNAME:
    bots = "Enabled"
else:
    bots = "Disabled"


if PM_AUTO_BAN == "False":
    pm = "Disabled"
else:
    pm = "Enabled"

TELEUSER = ALIVE_NAME

tele = f"Userbot Version: {telever}\n"
tele += f"Log Group: {log}\n"
tele += f"Assistant Bot: {bots}\n"
tele += f"PMSecurity: {pm}\n"
tele += f"\nVisit @FlicksSupport for assistance.\n"
telestats = f"{tele}"

user = bot.get_me()
TELE_NAME = user.first_name
OWNER_ID = user.id

# count total number of groups


async def tele_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
