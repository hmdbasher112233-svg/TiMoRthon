# Repthon - Baqir
# Copyright (C) 2023 RepthonArabic. All Rights Reserved
#
# This file is a part of < https://github.com/RepthonArabic/RepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/RepthonArabic/RepthonAr/blob/master/LICENSE/>.
""" 
OpenAi & ChatGpt for Repthon™ t.me/Repthon
Write file by ZelZal, Roger t.me/E_7_V, t.me/zzzzl1l
ها خماط بعدك تخمط مني .. ماتستحي ؟
متى راح تصير مطور وانت مقضيها خمط تعب وحقوق الناس
ههههههههههههههههههههههههههههههههههههههههههههههههههههههه
"""

import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import zq_lo
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"


# code by t.me/M4M4M4T
@zq_lo.rep_cmd(pattern="اج اس ثون(?: |$)(.*)")
async def repthon_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@GPT4Telegrambot" #code by t.me/zzzzl1l
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**⎉╎بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**⎉╎مثـــال :**\n`.HSTHON من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/zzzzl1l
        zelzal = zzz.text
    if not event.reply_to_msg_id: #code by t.me/zzzzl1l
        zelzal = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**⎉╎جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n⎉╎الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/zzzzl1l
        try:
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/zzzzl1l
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            repthon = await conv.get_response()
            malath = repthon.text
            if "understanding" in zedthon.text: #code by t.me/zzzzl1l
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {zelzal}\n\n{malath}**\n\n───────────────────\n𝗥𝗲𝗽𝘁𝗵𝗼𝗻 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t𝐁𝐀𝐐𝐈𝐑 • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/zzzzl1l
            await zq_lo(unblock("GPT4Telegrambot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/zzzzl1l
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/zzzzl1l
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in zedthon.text: #code by t.me/HSTHON
                await asyncio.sleep(5)
                zedthon = await conv.get_response()
                malath = zedthon.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {zelzal}\n\n{malath}**\n\n───────────────────\n𝗭𝗧𝗵𝗼𝗻 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tᶻᵉˡᶻᵃˡ • ᴼᵖᵉⁿᴬᴵ")


# تخمــط اهينـــك Fuk-You

# code by t.me/E_7_V
@zq_lo.rep_cmd(pattern="س(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@GPT4Telegrambot" #code by t.me/HSTHON
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**⎉╎بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**⎉╎مثـــال :**\n`.HSTHON من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/zzzzl1l
        zelzal = zzz.text
    if not event.reply_to_msg_id: #code by t.me/zzzzl1l
        zelzal = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**⎉╎جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n⎉╎الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/zzzzl1l
        try:
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/zzzzl1l
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/zzzzl1l
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in zedthon.text: #code by t.me/zzzzl1l
                await asyncio.sleep(5)
                zedthon = await conv.get_response()
                malath = zedthon.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {zelzal}\n\n{malath}**\n\n───────────────────\n𝑯𝑺𝑻𝑯𝑶𝑵 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ꜱᴇʀʙᴏᴛ**\n\t\t\t\t\t\t\t\t𝑻𝑰𝑴𝑶𝑹 • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/zzzzl1l
            await zq_lo(unblock("GPT4Telegrambot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/zzzzl1l
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/zzzzl1l
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {zelzal}\n\n{malath}**\n\n───────────────────\n𝑯𝑺𝑻𝑯𝑶𝑵 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t𝑻𝑰𝑴𝑶𝑹 𝑯𝑴𝑫 • ᴼᵖᵉⁿᴬᴵ")
