# Задание 2 вариант 14
import re
import os

def find_common_word():
    filename = input("Введите имя файла (например, text.txt): ").strip()

    if not os.path.exists(filename):
        print(f"Ошибка: Файл '{filename}' не найден в папке со скриптом.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read().lower()

        sentences = [s.strip() for s in re.split(r'[.!?]', text) if s.strip()]

        if not sentences:
            print("Файл пуст или в нем нет предложений.")
            return

        common_words = set(re.findall(r'[а-яёa-z0-0]+', sentences[0]))

        for sentence in sentences[1:]:
            words_in_sentence = set(re.findall(r'[а-яёa-z0-0]+', sentence))
            common_words &= words_in_sentence

        if common_words:
            print(f"Общие слова во всех предложениях: {', '.join(common_words)}")
        else:
            print("Слов, которые есть в каждом предложении, не найдено.")

    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

if __name__ == "__main__":
    find_common_word()