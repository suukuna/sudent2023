from fastapi import FastAPI
import sentry_sdk

from pages.router import router

import libray


sentry_sdk.init(
    dsn="https://9be443bafe1445c8b17a269686c1078e@o4505250926886912.ingest.sentry.io/4505250941239296",
    traces_sample_rate=1.0,
)

app = FastAPI(title='CryptoData', version='1.0')
app.include_router(router)


@app.on_event('startup')
def startup():
    libray.send_telegram_message('API app started')


@app.on_event('shutdown')
def shutdown():
    libray.send_telegram_message('API app closed')


@app.get('/')
def index():
    message = 'root endpoint'
    print(libray.send_telegram_message(message))

    return {'message': message}


@app.get('/{number}')
def number_increaser(number: int, query: int = None):
    if query is not None:
        result = number / query
    else:
        result = number / 2

    return {
        'message': 'ok',
        'result': result,
    }
