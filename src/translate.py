import asyncio

from aiogoogletrans import Translator
from aiogoogletrans.models import Translated

timeout = 5.0


async def coro_translate_batch(text_list: list[str], dest, src) -> list[Translated]:
    translator = Translator()
    translations = await asyncio.gather(
        *[translator.translate(text, dest=dest, src=src) for text in text_list]
    )
    return translations


def translate_batch(text_list: list[str], dest='en', src='auto') -> list[str]:
    """
    批量翻译
    :param text_list: 文本列表
    :param dest: 源语言
    :param src: 目标语言
    :return: 翻译后的文本列表
    """
    translations = asyncio.run(coro_translate_batch(text_list, dest, src))
    return [translation.text for translation in translations]


if __name__ == '__main__':
    import time

    with open('../examples/end.txt', 'r', encoding='utf-8') as f:
        _text_list = f.read().split('\n\n')

    t1 = time.time()
    translated = translate_batch(_text_list, 'zh-cn')
    t2 = time.time()
    print('\n'.join(translated))
    print(t2 - t1)
