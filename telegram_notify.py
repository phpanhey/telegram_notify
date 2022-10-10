import argparse
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", required=True)
    parser.add_argument("--telegram_bot_token", required=True)
    parser.add_argument("--telegram_user_id", required=True)    
    return vars(parser.parse_args())


def send_telegram(args):
    request_string = (
        "https://api.telegram.org/bot"
        + args["telegram_bot_token"]
        + "/sendMessage?chat_id="
        + args["telegram_user_id"]
        + "&parse_mode=Markdown&text="
        + args["message"]
    )
    response = requests.get(request_string)
    return response.json()

if __name__ == "__main__":
    args = parse_args()
    send_telegram(args)