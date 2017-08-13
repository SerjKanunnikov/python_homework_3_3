import requests
import os
import config


def translator():
    txt_files = [file for file in os.listdir(os.getcwd()) if file.endswith(".txt")]
    for file in txt_files:
        print("Перевод файла", file)
        with open(file, encoding="utf-8") as f:
            lang = input("Выберите исходный язык (ru, de, es, fr):\n")
            to_lang = input("Выберите язык перевода (ru, de, es, fr):\n")
            params = {
                'key': config.API_KEY,
                'text': f.read(),
                'lang': "{}-{}".format(lang, to_lang)
            }
            response = requests.get(config.URL, params)
            response_json = response.json()
            with open(os.path.join(os.getcwd(), "translated_" + os.path.splitext(file)[0] + "_" + to_lang + ".txt"), "w", encoding="utf-8") as f:
                f.write(' '.join(response_json['text']))

if __name__ == '__main__':
    translator()
