def split_with_keeping_separators(text: str, separator: str) -> list[str]:
    """
    分割字符串，但是会保留标点
    :param text: 要分割的字符串
    :param separator: 分隔符
    :return: 分割后文本的列表
    """

    def is_meaningful(s: str) -> bool:
        """
        判断字符串是否有意义
        :param s: 字符串
        :return: 有意义为True，反之False
        """
        for i in s:
            if i not in ' \n':
                return True
        return False

    result = []
    i0 = 0
    for i in range(len(text)):
        if text[i] in separator:
            s = text[i0:i + 1]
            if is_meaningful(s):
                result.append(s)
            i0 = i + 1
    s = text[i0:i + 1]
    if is_meaningful(s):
        result.append(s)
    return result


if __name__ == '__main__':
    _test_text = """不向焦虑与抑郁投降，这个世界终会有我们存在的地方

如果你能记住我的名字，如果你们都能记住我的名字，也许我或者“我们”，终有一天能自由地生存着。"""
    print(split_with_keeping_separators(_test_text, '\n。，'))
