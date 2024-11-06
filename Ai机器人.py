

# 代码如下 为了让你们更理解添加了标注
import telebot
import time
import json
# 上方是需要安装和使用的库

bot = telebot.TeleBot('7591858553:AAHu_SJXnApMaJpNbKNUHehUC3UwsOhyxWE')
#上方是机器人填写令牌的地方 删除文字即可

# 下方是主要填写的代码 

# 设置一个标志来检测是否需要回复
greet_user = False

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global greet_user

    # 当用户输入“小猫小猫”时 启动回复模式
# 也可以把小猫小猫变成其他的关键词 只要发送以后即可启动

    if message.text == "小猫小猫":
        greet_user = True
        user_id = message.from_user.id
        username = message.from_user.username if message.from_user.username else "未知用户"

# 上方未知用户是获取下方设置用户名
        
        welcome_message = (
            f"亲爱的主人，我是您的专属 AI小猫 \n\n"
            f"〈😍フ 【 您的用户名: @{username} 】\n"
            f"   〇〇     【 您的用户ID: {user_id} 】\n"
            f"    ) . (        【 公益AI: .Viz 】\n"
            f"   ( Y  )\n"
            f"    \\|  /\n\n"
            f"不需要我的时候请发送 “再见小猫” 结束我！"            
        )

# 上方是发送关键词以后机器人返回的信息你也可以改成其他的

        bot.reply_to(message, welcome_message)

    # 当用户输入“退下吧小猫”时，结束回复模式

# 如上一样 回复关键词退出 模式

    elif message.text == "再见小猫":
        greet_user = False
        bot.reply_to(message, "再见\n亲爱的主人，我期待下次与你相遇")
    
    # 如果在回复模式中，处理用户发送的内容
    elif greet_user:
        # 处理用户发送的其他内容
        ai_input = message.text  # 使用用户输入的内容
        url = f"https://api.mhimg.cn/api/gpt_aimaoniang/?prompt={ai_input}"
        response = requests.get(url)

        if response.status_code == 200:
            bot.reply_to(message, response.text)  # 假设返回的是文本内容
        else:
            bot.reply_to(message, f"请求失败，状态码: {response.status_code}")

if name == "main":
    while True:
        try:
            bot.polling()
        except Exception as e:
            print(f"遇到错误：{e}，自动重启")
            time.sleep(5)  #