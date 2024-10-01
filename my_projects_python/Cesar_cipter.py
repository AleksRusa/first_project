def cipter(way, language, shift, text):
    text2 = []
    while True:
        if language == "rus":
            if way == "1":
                for c in text:
                    if ord(c.lower()) + shift > ord("я"):
                        if 1040 <= ord(c) <= 1071:
                            text2.append(chr(1040 + (shift - (1072 - ord(c)))))            
                        else:
                            text2.append(chr(1072 + (shift - (1104 - ord(c)))))
                    else:
                        text2.append(chr(ord(c) + shift))
                return text2
            else:
                for c in text:
                    if ord(c.lower()) - shift < ord("а"):
                        if 1040 <= ord(c) <= 1071:
                            text2.append(chr(1071 - (shift - (ord(c) - 1039))))
                        else:
                            text2.append(chr(1103 - (shift - (ord(c) - 1071))))
                    else:
                        text2.append(chr(ord(c) - shift))
                return text2
        else:
            if way == "1":
                for c in text:
                    if ord(c.lower()) + shift > ord("z"):
                        if 65 <= ord(c) <= 90:
                            text2.append(chr(65 + (shift - (91 - ord(c)))))            
                        else:
                            text2.append(chr(97 + (shift - (123 - ord(c)))))
                    else:
                        text2.append(chr(ord(c) + shift))
                return text2
            else:
                for c in text:
                    if ord(c.lower()) - shift < ord("a"):
                        if 97 <= ord(c) <= 122:
                            text2.append(chr(90 - (shift - (ord(c) - 64))))
                        else:
                            text2.append(chr(122 - (shift - (ord(c) - 96))))
                    else:
                        text2.append(chr(ord(c) - shift))
                return text2

def is_valid_text(text, lang):
    if text.isalpha():
        if lang == "eng":
            for c in text:
                if not (65 <= ord(c) <= 90 or 97 <= ord(c) <= 122):
                    return False
        elif lang == "rus":
            for c in text:
                if not (1040 <= ord(c) <= 1103):
                    return False
        return True
    return False


def is_valid_num(way):
    if way.isdigit() and 1 <= int(way) <= 2 and len(way) == 1:
        return way
    else:
        return False


def shift_is_valid(shift, n):
    if shift.isdigit() and 1 <= int(shift) <= n:
        return True
    else:
        return False


def language_is_valid(language):
    if language.isalpha() and language[0:3].lower() == "rus":
        return True, "rus"
    elif language.isalpha() and language[0:3].lower() == "eng":
        return True, "eng"
    else:
        return False, ""


def print_task():
    while True:
        way = input("Choose option: encryption - 1 / decryption - 2: ")
        if is_valid_num(way):
            break
        else:
            print("mistake")

    while True:
        language = input("Choose language: russian/english: ")
        flag, language = language_is_valid(language.strip())
        if flag:
            break
        else:
            print("mistake")

    while True:
        if language == "rus":
            n = 32
        elif language == "eng":
            n = 26
        shift = input(f"Choose shift in range(1 - {n}) ")
        if shift_is_valid(shift, n):
            break
        else:
            print("mistake, shift is out of range")

    while True:
        text = input("print massage: ")
        if is_valid_text(text.strip(), language):
            break
        else:
            print("mistake? massage must by in one language")
    return way, language, int(shift), text


print("Hello user")
way, language, shift, text = print_task()
massage = cipter(way, language, shift, text)
print(''.join(massage))
