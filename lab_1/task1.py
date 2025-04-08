from work_files import *


def vigenere_cipher(text, key, alphabet) -> str:
    text = text.upper()
    key = key["key"]

    encoded_text = ''
    key_index = 0

    for char in text:
        if char in alphabet:
            char_pos = alphabet.index(char)

            key_char_pos = alphabet.index(key[key_index % len(key)])

            new_pos = (char_pos + key_char_pos) % len(alphabet)

            encoded_text += alphabet[new_pos]

            key_index += 1
        else:
            encoded_text += char

    return encoded_text


def main():
    try:
        task1 = read_json("settings.json")
        text = read_txt(task1["PLANE_TEXT"])
        key = read_json(task1["KEY_ENCODE"])
        alphabet = task1["ALPHABET"]
        res = vigenere_cipher(text, key, alphabet)
        write_txt(res, task1["RESULT"])
        print(res)

    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()

