from config import *
from database import *
from insult import insult
import os
from pyrogram import Client ,filters , enums
from pyrogram.errors import *
#os.mkdir("downloads")
insult = Client (  "vocal",
                api_id = API_ID,
                api_hash = API_HASH ,
                bot_token = BOT_TOKEN 
                )

@insult.on_message(filters.private &filters.user([2069970688])& filters.regex('!¡'))
async def cast_mes(c,m):
    blocked = ''
    idinvalid  = ''
    deactive = ''
    for user in bot_users.find():
        try :
            await m.copy(user['userid'],m.text.replace('/cast',''))
        except UserIsBlocked:
            blocked+=f"{user['userid']} - {user['name']} - @{user['username']}\n"
        except InputUserDeactivated:
            deactive+=f"{user['userid']} : {user['name']} : {user['username']}\n"
        except PeerIdInvalid:
            idinvalid+=f" {user['userid']} : {user['name']} : {user['username']}\n"
        except FloodWait as e:
            await asyncio.sleep(e.x)     
        except Exception as error:
          await m.reply(error)
    mj = f"Cast Logs\n\nBlocked\n{blocked}\nInvalid Ids\n{idinvalid}\nDeactivated\n{deactive}"         
    with open('log.txt','w') as f:
        f.write(mj)
    await m.reply_document('log.txt')
    
    
                
                
@insult.on_message(filters.private &  filters.command(['start']))
async def start(_, m):
    await m.delete()
    usr_name = m.from_user.first_name 
    usr_id = m.from_user.id
    usr_username= m.from_user.username
    add_user(usr_name,usr_id ,usr_username)
    await m.reply(f"**hi {usr_name} you bitch Cattle wanger how are you?\ninsult me once i kill you twice?**")

        
                

@insult.on_message(filters.private & filters.text)
async def letyou(c,m):
    await m.reply_chat_action(enums.ChatAction.TYPING)
    if 1 == 1 :
        try :
            await c.get_chat_member(-1001776406696,m.from_user.id)
        except UserNotParticipant:
            await m.reply('**as this Bot provides free service for users you have to join the bot channel \n@neuralp**')
            return
    else :
        pass
    ans = insult(m.text)
    await m.reply(ans)
print('everything is fine ')
insult.run()
