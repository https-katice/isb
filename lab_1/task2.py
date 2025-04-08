from work_files import *


def real_frequency(text) -> dict:
    frequency_dict = {}
    length = len(text)
    for char in text:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    for char in frequency_dict:
        frequency_dict[char] = frequency_dict[char] / length
    return dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))


def exchange(text, key) -> str:
    decrypted = ""
    for char in text:
        decrypted_s = key.get(char)
        if decrypted_s is None:
            decrypted_s = char
        decrypted += decrypted_s
    return decrypted


def main():
    try:
        task2 = read_json("settings.json")
        text = read_txt(task2["ENCRYPTED"])

        if text:
            freq_dict = real_frequency(text)
            write_json(freq_dict, (task2["REAL_FREQ"]))
            print(freq_dict)

            res = exchange(text, read_json(task2["KEY"]))
            write_txt(res, (task2["DECRYPTED"]))
            print(res)

    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
