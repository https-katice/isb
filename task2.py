from work_files import *


def real_frequency(text) -> dict:
    frequency_dict = {}
    length = len(text)
    for char in text:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    for char in frequency_dict:
        frequency_dict[char] = frequency_dict[char] / length
    return dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))


def form_key(standard, real):
    res = {
        key1: key2
        for (key1, _), (key2, _) in zip(standard.items(), real.items())
        if key1 in standard and key2 in real
    }
    return res


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

            sample_freq = read_json(task2["STANDARD"])
            new_dict = form_key(freq_dict, sample_freq)
            write_json(new_dict, (task2["KEY_DECODE"]))
            print(new_dict)

            res = exchange(text, new_dict)
            write_txt(res, (task2["DECRYPTED"]))
            print(res)

            read = exchange(res, read_json(task2["KEY"]))
            write_txt(read, (task2["TEXT"]))
            print(read)

    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
