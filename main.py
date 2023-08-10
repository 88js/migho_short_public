from helper import echo,bot,sudo,anyliz,check,set_channel,admin,user,new_url, baba
from telebot.types import InlineKeyboardButton as bb, InlineKeyboardMarkup as b


@bot.message_handler(func=lambda m:True)
def good_job(m):
    if m.text == "/start" and m.chat.id == sudo:
        bot.reply_to(m,'*اهلا عزيزي الادمن كيف حالك ؟*',reply_markup=admin(),parse_mode='markdown')
        user(m)
    else:
        try:
            check(m)
            if baba(m) == False:
                ch = open('ch.txt', 'r').read()
                s = bot.get_chat(ch)
                msg = f"""
            ♦يرجى الاشتراك في القناة لاستخدام البوت ♦
            
            @{s.username}

            وبعدها اضغط /start
            """
                b1 = bb(f'{s.title}', url=f't.me/{s.username}')
                bs = b().add(b1)
                bot.reply_to(m, msg, reply_markup=bs)
            else:
                user(m)
        except:
            user(m)
            check(m)
@bot.callback_query_handler(func=lambda call:True)
def rs(call):
    if call.data == 'echo':
        echo(call.message)
    if call.data == 'two':
        anyliz(call.message)
    if call.data == 'subscribe':
        set_channel(call.message)
    if call.data == 'new_url':
        new_url(call.message)
    if call.data == "my":
        try:
            bot.send_message(call.message.chat.id,
                        open(f'{call.message.chat.id}order.txt', 'r').read())
        except:
            bot.answer_callback_query(callback_query_id=call.id,
                                    text='ليس لديك طلبات',
                                    show_alert=True)

bot.infinity_polling()
