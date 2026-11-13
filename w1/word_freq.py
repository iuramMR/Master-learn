import string

# path = 'input.txt'
#
# with open(path, 'r', encoding='utf-8') as f:
#     text = f.read()
#
# text = text.lower()
# text = text.translate(str.maketrans('', '', string.punctuation))
# word = text.split()
#
# counter = {}
# for w in word:
#     counter[w] = counter.get(w, 0) + 1
#
# top20 = sorted(counter.items(),key = lambda kv:(-kv[1],kv[0]))[:20]
# for word, count in top20:
#     print(f'{word: <6}{count}')

import sys
import string
from collections import Counter


def count_words(text):
    """ 把文本切成小写并，返回单词统计词频dict。"""
    text = text.lower()
    #  掉所有英文点；光用删标strip 只能去首尾
    text = text.translate(str.maketrans("", "", string.punctuation))
    return Counter(text.split())


def top_words(counter, n=20):
    """ 按次数降序、同次数按字母升序，返回前n 名。"""
    return sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


def main():
    if len(sys.argv) < 2:
        print("用法：python word_freq.py <文件路径>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"找不到文件：{path}")
        sys.exit(1)

    counter = count_words(text)
    print(f"共{len(counter)}个不同的，以下是词频Top 20：")
    for word, count in top_words(counter):
        print(f"{word:<12}{count}")


if __name__ == "__main__":
    main()