import requests

def telegram_bot_sendtext(bot_message, bot_chatID='1674'):
    bot_token = '5892365212:AAELYsxonLoApk5H28Lsc9ins2OoxdXiy2g'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

