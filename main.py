from telebot import TeleBot
import config
from listener import start_listener, stop_listener
from event import NewEvent, TUNNEL_OPENED, TUNNEL_CLOSED

bot = TeleBot(config.BOT_TOKEN)


def handle_event(event: NewEvent):
    tunnel = event.get_tunnel()
    if event.get_type() == TUNNEL_OPENED:
        title = '<strong>New ngrok tunnel opened.</strong>'
    else:
        title = '<strong>Ngrok tunnel closed</strong>'
    bot.send_message(config.CHAT_ID, f'{title}\n'
                                     f'Started at: {tunnel.started_at}\n'
                                     f'Region: {tunnel.region}\n'
                                     f'Proto: {tunnel.proto}\n'
                                     f'Url: <code>{tunnel.public_url.split("//")[1]}</code>\n'
                                     f'Forward to: {tunnel.forwards_to}\n', parse_mode='html')


if __name__ == '__main__':
    start_listener(config.NGROK_API_TOKEN, handle_event)
