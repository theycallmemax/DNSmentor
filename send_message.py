import requests

def telegram_bot_sendtext(bot_message, bot_chatID='1674351438'):
    bot_token = '5712199811:AAF7-n5ceuzwIRcBRr7yaNZnvpk-oqAEqYk'

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

