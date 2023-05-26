import requests

TOKEN_TELEGRAM = '5829354270:AAHtjoswafm0nLY8ecViwXxCpn-QTVyS5lA'
TELEGRAM_CHAT_ID = 1650281295


def send_telegram_message(
        message: str,
        my_token: str = TOKEN_TELEGRAM,
        method: str = 'sendMessage'):
    url = f'https://api.telegram.org/bot{my_token}/{method}'
    response = requests.post(
        url=url,
        data={'chat_id': TELEGRAM_CHAT_ID, 'text': message},
    )

    return response.json()
