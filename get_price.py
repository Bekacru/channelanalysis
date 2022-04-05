import json
import translators as ts
from langdetect import detect
with open('channel_messages.json', 'r') as f:
    data = json.load(f)


for message in data:
    message = (message['message'])


# print(message_trans)


def get_title(message):
    title = message.split('\n')[0]
    return title


def lang_en(message):
    if detect(message) == 'en':
        return message
    else:
        message = ts.google(message, to_language='en')
        return message


def get_price(message):
    message = message.lower()
    message_arr = message.split()
    if "price" in message_arr:
        price_index = message_arr.index("price")
        for n in range(1, 3):
            price_value = message_arr[price_index + n]
            if price_value.isnumeric():
                price = price_value
                break
            elif price_value.find("birr") != -1:
                price = price_value.replace("birr", '')
                break
            elif price_value.find("br") != -1:
                price = price_value.replace("birr", '')
                break
            elif price_value.find("k") != -1:
                price = price_value.replace("k", "000")
                break
            # ADD NEW CHECKS HERE
            elif price_value.find("#") != -1:
                price = price_value.replace("#", "")
                break
            else:
                price = '0'
    elif "birr" in message_arr:
        birr_index = message_arr.index("birr")
        for n in range(1, 3):
            price_value = message_arr[birr_index + n]
            price_value2 = message_arr(birr_index - n)
            if price_value.isnumeric():
                price = price_value
                break
            elif price_value2.isnumeric():
                price = price_value2
                break
            else:
                price = '0'
    return price


print(get_price(message))
