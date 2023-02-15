import re
from pyrogram import Client, filters, idle
from get_age import get_age

TOKEN = 'BOT_TOKEN_HERE' #Get it from @BotFather
API_ID = 'API_ID_HERE' #Get it from my.telegram.org
API_HASH = 'API_HASH_HERE' #Get it from my.telegram.org

pyrogramClient = Client(
   'getAges'+TOKEN.split(':')[0],
   API_ID, API_HASH,
   bot_token=TOKEN
)

pyrogramClient.start() # To start pyrogram client .
botUsername = pyrogramClient.me.username

def Find_urls(text):
  m = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(m,text)  
  return [x[0] for x in url]

@pyrogramClient.on_message(filters.regex('^/start$') & filters.private)
async def on_message_start(c,m):
    return await m.reply('''
**Hello, {username}! I am a computer program that can chat (also known as a 'bot') and I can tell you something about you and the messages you send me.

Try it out, just forward me some messages ;)

Note from the developers:
This is a very early version of the bot. Therefore a few things (explainatory texts, etc.) are still missing. If you can code, here is the [GitHub repo](https://github.com/x72x/telegram-bot-getids-py). If you don't know how to program, you can still help. Just tell us @DNDZAiD **.

👤 You
 ├ id: `{id}`
 ├ is_bot: {is_bot}
 ├ first_name: {first_name}
 ├ username: [{username}](https://t.me/{username})
 ├ language_code: {language_code} (-)
 └ is_premium: {is_premium}'''.format(
        username=m.from_user.username,
        first_name=m.from_user.first_name,
        is_premium=m.from_user.is_premium,
        id=m.from_user.id,
        is_bot=m.from_user.is_bot,
        language_code=m.from_user.language_code,
     ), disable_web_page_preview=False)
     

@pyrogramClient.on_message(filters.regex('^/about$') & filters.private)
async def on_message_about(c,m):
     age = get_age(m.from_user.id)
     return await m.reply('''
👤 You
 ├ id: `{id}`
 ├ is_bot: {is_bot}
 ├ first_name: {first_name}
 ├ username: [{username}](https://t.me/{username})
 ├ language_code: {language_code} (-)
 └ is_premium: {is_premium}
 └ created: {age0} {age1} [(?)](https://t.me/{botUsername}?start=idhelp)'''.format(
        username=m.from_user.username,
        first_name=m.from_user.first_name,
        is_premium=m.from_user.is_premium,
        id=m.from_user.id,
        is_bot=m.from_user.is_bot,
        language_code=m.from_user.language_code,
        botUsername=botUsername,
        age0=age[0], age1=age[1]
     ),disable_web_page_preview=True)

@pyrogramClient.on_message(filters.regex('^/start idhelp$') & filters.private)
async def on_message_idhelp(c,m):
     return await m.reply('''
**Account creation date**

How it works
To quote @Superuser27: Interpolation on known registration dates of certain IDs.
The bot just has a large list of Account's IDs and their associated (known) creation dates and compares your id against this list.

**My account creation date is wrong**
Sure. That is why there is a "~" in front of it. It is just a guess and very often the IDs given out at a time differ very much from each other, resulting in a sheer data mess. So just consider the date as some sort of art.
''')

@pyrogramClient.on_message(filters.private)
async def on_message_all(c,m):
     age = get_age(m.from_user.id)
     txt = '''👤 You
 ├ id: `{id}`
 ├ is_bot: {is_bot}
 ├ first_name: {first_name}
 ├ username: [{username}](https://t.me/{username})
 ├ language_code: {language_code} (-)
 └ is_premium: {is_premium}
 └ created: {age0} {age1} [(?)](https://t.me/{botUsername}?start=idhelp)'''.format(
        username=m.from_user.username,
        first_name=m.from_user.first_name,
        is_premium=m.from_user.is_premium,
        id=m.from_user.id,
        is_bot=m.from_user.is_bot,
        language_code=m.from_user.language_code,
        botUsername=botUsername,
        age0=age[0], age1=age[1]
     )
     if m.forward_sender_name:
        txt += f'''

👤 Forwarded from
 └ hidden: `This user hid his account information in Telegram's privacy settings, so I can't tell you anything about him.`

📃 Message
 └ forward_date: {m.forward_date} GMT
'''
     if m.forward_from and m.from_user.id != m.forward_from.id:
        username = '['+m.forward_from.username+']'+'('+'t.me/'+m.forward_from.username+')' if m.forward_from.username else 'None'
        age = get_age(m.forward_from.id)
        txt += f'''

👤 Forwarded from
 ├ id: `{m.forward_from.id}`
 ├ is_bot: {m.forward_from.is_bot}
 ├ first_name: {m.forward_from.first_name}
 ├ username: {username}
 └ created: {age[0]} {age[1]} [(?)](https://t.me/{botUsername}?start=idhelp)

📃 Message
 └ forward_date: {m.forward_date} GMT'''
     if m.forward_from_chat:
        username = '['+m.forward_from_chat.username+']'+'('+'t.me/'+m.forward_from_chat.username+')' if m.forward_from_chat.username else 'None'
        txt += f'''

💬 Origin chat
 ├ id: `{m.forward_from_chat.id}`
 ├ title: {m.forward_from_chat.title}
 ├ username: {username}

📃 Message
 └ message_id: [{m.forward_from_message_id}](https://t.me/c/{str(m.forward_from_chat.id).replace("-100","")}/{m.forward_from_message_id})
 └ forward_date: {m.forward_date} GMT
 '''
     if m.text or m.caption:
       find = Find_urls(m.text.html) if m.text else Find_urls(m.caption.html)
       if find:
          txt += '\nUrls:\n'
          for url in find:
            txt += f'\n └ {url}'
     
     return await m.reply(txt, disable_web_page_preview=True)
     

print('Your Client @'+botUsername+' started successfully ')
idle() 