# w1 · 英文文本词频统计

读取英文文本，统计每个单词出现的次数，输出高频词排名。

## 功能

读取一个英文文本文件，清除标点并统一小写后统计词频，
按「次数降序、同次数按字母升序」输出前 20 个高频词。

## 运行方式

需要 Python 3.8+，无第三方依赖。

```bash
# 使用仓库自带的示例文本
python word_freq.py input.txt

# 统计你自己的文件
python word_freq.py 你的文件.txt
```

`input.txt` 是随仓库附带的示例文本，可直接用于测试。

不给参数时脚本会打印用法提示并退出；文件不存在时会给出提示，不会抛出异常堆栈。

## 输出示例

`python word_freq.py input.txt` 的实际输出：

```
共15个不同的，以下是词频Top 20：
fox         4
the         4
quick       3
a           2
dog         2
and         1
away        1
barks       1
brown       1
```

左列固定 12 字符宽，单词不足补空格，因此右侧次数列对齐。

## 实现要点

- `str.maketrans` + `translate` 一次性删除所有英文标点（`strip` 只能去首尾）
- `lower()` 统一大小写，避免 `The` 与 `the` 被算成两个词
- `collections.Counter` 统计词频
- `sorted(key=lambda kv: (-kv[1], kv[0]))` 实现「次数降序 + 字母升序」双关键字排序，负号用于把升序翻转为降序
- `[:20]` 切片取前 20 名
- `sys.argv` 读取命令行参数，`FileNotFoundError` 单独捕获，给出友好提示而非异常堆栈
- 拆分为 `count_words` / `top_words` / `main` 三个函数，配合 `if __name__ == "__main__"` 守卫，便于被其他模块导入复用
