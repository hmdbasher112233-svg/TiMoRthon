#HSTHON 
# Copyright (C) 2026 HSTHON . All Rights Reserved
#
# This file is a part of < https://github.com/Repthon-Arabic/RepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Repthon-Arabic/RepthonAr/blob/master/LICENSE/>.

import asyncio
import requests
import logging
from asyncio import sleep

from telethon.tl import functions, types
from telethon.errors import UserAdminInvalidError
from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest

from repthon import zq_lo

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import gvarstatus
from ..helpers import readable_time
from ..helpers.utils import reply_id
from ..utils import is_admin
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

spam_chats = []

# =========================================================== #
#                           الملـــف كتـــابـــة مـــن الصفـــر - T.me/HSTHON                         #
# =========================================================== #
Warn = "تخمـط بـدون ذكـر المصـدر - ابلعــك نعــال وراح اهينــك"
REPTHON_BEST_SOURCE = "[ᯓ 𝑯𝑺𝑻𝑯𝑶𝑵 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة خـاص 🚹](t.me/Repthon) .\n\n**- جـارِ الاذاعـه خـاص لـ أعضـاء الكـروب 🛗\n- الرجـاء الانتظـار .. لحظـات ⏳**"
REPTHON_PRO_SOURCE = "[ᯓ 𝑯𝑺𝑻𝑯𝑶𝑵 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة زاجـل 🕊](t.me/HSTHON) .\n\n**- جـارِ الاذاعـه لـ قائمـة زاجـل 📜\n- الرجـاء الانتظـار .. لحظـات ⏳**"
BAQIR_PRO_DEV = "[ᯓ 𝑯𝑺𝑻𝑯𝑶𝑵 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة زاجـل 🕊](t.me/HSTHON) .\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n**⎉╎قائمـة الاذاعـه فارغـه ؟! ❌**\n**⎉╎قم باضافة يوزرات عبـر الامر**\n`.اضف فار زاجل` **بالـرد ع عدة يوزرات تفصل بينهم مسافات**"
# =========================================================== #
#                                      بـاقـر - T.me/E_7_V                                 #
# =========================================================== #
#                                      تـاريـخ كتابـة الملـف - 24 ديسمبر/2023                                  #
# =========================================================== #


@zq_lo.rep_cmd(pattern=f"للكل(?: |$)(.*)", groups_only=True)
async def malath(event):
    repthon = event.pattern_match.group(1)
    if repthon:
        await edit_or_reply(event, "**⎉╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        baqir = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**⎉╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    chat_id = event.chat_id
    is_admin = False
    try:
        await zq_lo(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        pass
    spam_chats.append(chat_id)
    rrr = await edit_or_reply(event, REPTHON_BEST_SOURCE, link_preview=False)
    total = 0
    success = 0
    async for usr in event.client.iter_participants(event.chat_id):
        total += 1
        if not chat_id in spam_chats:
            break
        username = usr.username
        magtxt = f"@{username}"
        if str(username) == "None":
            idofuser = usr.id
            magtxt = f"{idofuser}"
        if baqir.text:
            try:
                await borg.send_message(magtxt, baqir, link_preview=False)
                success += 1
            except BaseException:
                return
        else:
            try:
                await borg.send_file(
                    magtxt,
                    baair,
                    caption=baqir.caption,
                    link_preview=False,
                )
                success += 1
            except BaseException:
                return
    BAQIR_BEST_DEV = f"[ᯓ 𝑯𝑺𝑻𝑯𝑶𝑵 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة خـاص 🚹](t.me/HSTHON) .\n\n**⎉╎تمت الاذاعـه لـ اعضـاء الكـروب .. بنجـاح  ✅**\n**⎉╎عـدد {success} عضـو**"
    await rrr.edit(BAQIR_BEST_DEV, link_preview=False)
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@zq_lo.rep_cmd(pattern="ايقاف للكل", groups_only=True)
async def unmalath(event):
    if not event.chat_id in spam_chats:
        return await event.edit("**- لاتوجـد عمليـة اذاعـه للاعضـاء هنـا لـ إيقافـها ؟!**")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.edit("**⎉╎تم إيقـاف عمليـة الاذاعـه للاعضـاء هنـا .. بنجـاح✓**")



#                                       تـاريـخ كتابـة الكـود - 24 ديسمبر/2023                                  #
#                                        الملف كتابتي من الصفر ومتعوب عليه                                  #
#                                           تخمط بدون ذكر المصدر = اهينك                                     #
@zq_lo.rep_cmd(pattern="زاجل(?: |$)(.*)")
async def malath(event):
    repthon = event.pattern_match.group(1)
    if repthon:
        await edit_or_reply(event, "**⎉╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    baqir = await event.get_reply_message()
    if gvarstatus("ZAGL_Rep") is None:
        return await event.edit(BAQIR_PRO_DEV, link_preview=False)
    baqir = gvarstatus("ZAGL_Rep")
    users = baqir.split(" ")
    rrr = await edit_or_reply(event, REPTHON_PRO_SOURCE, link_preview=False)
    total = 0
    success = 0
    user_entity = None
    for user in users:
        total += 1
        if baqir.text:
            try:
                user_entity = await zq_lo.get_entity(user)
                if user_entity.bot or user_entity.deleted:
                    continue
                await zq_lo.send_message(user_entity.id, zilzal, link_preview=False)
                success += 1
            except UserAdminInvalidError:
                pass
            except Exception as e:
                rrr.edit(f"خطأ في إرسال الرسالة إلى {user_entity.id}: {str(e)}")
        elif baqir.media:
            try:
                user_entity = await zq_lo.get_entity(user)
                if user_entity.bot or user_entity.deleted:
                    continue
                await zq_lo.send_file(user_entity.id, zilzal.media, caption=zilzal.text)
                success += 1
            except UserAdminInvalidError:
                pass
            except Exception as e:
                rrr.edit(f"خطأ في إرسال الرسالة إلى {user_entity.id}: {str(e)}")
    BAQIR_BEST_DEV = f"[ᯓ 𝑯𝑺𝑻𝑯𝑶𝑵 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة زاجـل 🕊](t.me/HSTHON) .\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n**⎉╎تمت الاذاعـه .. بنجـاح  ✅**\n**⎉╎عـدد {success} أشخـاص**"
    await rrr.edit(BAQIR_BEST_DEV, link_preview=False)
