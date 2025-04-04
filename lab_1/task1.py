from work_files import *


def vigenere_cipher(text, key, alfavit):
    text = text.upper()
    key = key["key"]

    encoded_text = ''
    key_index = 0

    for char in text:
        if char in alfavit:
            char_pos = alfavit.index(char)

            key_char_pos = alfavit.index(key[key_index % len(key)])

            if (char_pos + key_char_pos) < len(alfavit):
                new_pos = (char_pos + key_char_pos)
            elif (char_pos + key_char_pos) > len(alfavit):
                new_pos = (char_pos + key_char_pos) - len(alfavit) + 1
            else:
                new_pos = len(alfavit) - 1

            encoded_text += alfavit[new_pos]

            key_index += 1
        else:
            encoded_text += char

    return encoded_text


def main():
    task1 = read_json("settings.json")
    text = read_txt(task1["PLANE_TEXT"])
    key = read_json(task1["KEY_ENCODE"])
    alfavit = task1["ALPHABET"]
    res = vigenere_cipher(text, key, alfavit)
    write_txt(res, 'encoded.txt')
    print(res)


if __name__ == "__main__":
    main()

