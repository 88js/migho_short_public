from requests import get
from telebot import TeleBot
from telebot.types import InlineKeyboardButton as bb,InlineKeyboardMarkup as b,KeyboardButton as k, ReplyKeyboardMarkup as re



token = '' #telegram bot token
bot = TeleBot(token)
sudo = 0 #ur account id telegram

def baba(m):
    try:
        if m.text:
            ch = open('ch.txt', 'r').read()
            che = bot.get_chat_member(int(ch), m.from_user.id)
            if che.status == 'left':
                return False
    except:
        return False

def user(m):
    mm = b()
    b1 = bb('روابطي',callback_data='my')
    b2 = bb('اختصار جديد',callback_data='new_url')
    mm.add(b2)
    mm.add(b1)
    bot.reply_to(m,'*اهلا بك عزيزي في بوت اختصار الروابط*',reply_markup=mm,parse_mode='markdown')

def new_url(m):
  x = bot.send_message(m.chat.id,'*ارسل الرابط ليتم اختصاره : *',parse_mode='markdown')
  bot.register_next_step_handler(x,url_done)

def url_done(m):
    url = shorten(str(m.text))
    print(url)
    if 'success' == url["status"]:
      msg = f'''✅ اختصار ناجح : \n\n*الرابط* : {url['shortenedUrl']}'''
      bot.reply_to(m,msg,parse_mode='markdown',disable_web_page_preview=True)
      open(f'{m.chat.id}order.txt', 'a').write(f'{m.text}\n')
    else:
      msgg = '''يرجى ادخال رابط صحيح💢'''
      bot.reply_to(m,msgg,parse_mode='markdown')
def shorten(url : str):
    url_api = f'https://exe.io/api?api=7d14f914e049416618bf630b8311258bc307b5b7&url={url}'
    return get(url=url_api).json()


def anyliz(m):
    s = open('user.txt','r')
    for count, line in enumerate(s):
        pass
    msg = f'عدد الاعضاء : \n \n *{str(count + 1)}*'
    bot.send_message(
                    chat_id=m.chat.id,
                    text=msg,
                    parse_mode='markdown'
                    )


def admin():
    b1 = bb(text='اذاعه للمستخدمين',callback_data='echo')
    b2 = bb(text='تعيين قناة الاشتراك الاجباري',callback_data='subscribe')
    b3 = bb(text='الاحصائيات',callback_data='two')
    s = b()
    s.add(b1,b2,b3)
    return s


def check(m):
    s = open('user.txt', 'r').read()
    if str(m.chat.id) not in s:
        open(f'{m.chat.id}.txt', 'w').write('0')
        open(f'{m.chat.id}ordernum.txt', 'w').write('0')
        open('user.txt', 'a').write(str(m.chat.id) + '\n')
        bot.send_message(sudo,f'=========\nعضو جديد في البوت : \n\nايدي : {m.chat.id}\nمعرفه @{m.from_user.username}\n=========')


def set_channel(m):
    sm = k(text='الغاء')
    ss = re(resize_keyboard=True).add(sm)
    s = bot.send_message(
        m.chat.id,
        '*قم بتحويل اي رسالة من القناة المراد تعيينها : *\n\nقم بأرسال كلمه الغاء لالغاء العمليه',
        reply_markup=ss)
    bot.register_next_step_handler(s, done_add)


def done_add(m):
    try:
        if 'الغاء' == m.text:
            bot.reply_to(m, 'اضغط /start')
            pass
        else:
            bot.get_chat_administrators(chat_id=m.forward_from_chat.id)
            open('ch.txt', 'w').write(str(m.forward_from_chat.id))
            bot.reply_to(m, 'تم تعيين القناة')
    except:
        bot.reply_to(m, 'قم برفع البوت ادمن واعد المحاوله')



##/// echo


def echos(idd, m):
    try:
        bot.forward_message(chat_id=int(idd),
                            from_chat_id=m.chat.id,
                            message_id=m.message_id)
        return True
    except:
        return False


def echo(m):
    s = bot.send_message(
        m.chat.id,
        '*قم بأرسال (صورة - ملف - ستيكر - رساله) لتحويلها الى جميع المستخدمين : *'
    )
    bot.register_next_step_handler(s, echo_)


def echo_(m):
    done = 0
    xdone = 0
    users = open('user.txt', 'r').readlines()
    for i in users:
        s = echos(m=m, idd=i)
        if s == True:
            done += 1
        elif s == False:
            xdone += 1
            bot.send_message(
                m.chat.id,
                f'تمت الاذاعة الى : \n\n اذاعة ناجحة : {done}\nاشخاص قاموا بحظرالبوت : {xdone}'
        )
