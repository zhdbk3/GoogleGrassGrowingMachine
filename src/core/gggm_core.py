import argparse
from concurrent.futures import ThreadPoolExecutor
import random
import time
import logging

from tqdm import tqdm

if __name__ == '__main__':
    import str_utils
    from gtn_modified import GoogleTranslator
    from hint import TypedNamespace
    from languages import *
else:
    from . import str_utils
    from .gtn_modified import GoogleTranslator
    from .hint import TypedNamespace
    from .languages import *

# 全局变量
current_text_list: list[str] = []
total_progress: int = 0
finished_thread_cnt: int = 0
error: BaseException | None = None


def init():
    """初始化全局变量"""
    global current_text_list, total_progress, finished_thread_cnt, error
    current_text_list.clear()
    total_progress = 0
    finished_thread_cnt = 0
    error = None


class ThreadTranslateOne:
    def __init__(self, idx: int, args: TypedNamespace):
        """
        生草一句的线程
        :param idx: 线程编号，操作全局列表的索引
        :param args: 参数
        :return: None，结果实时更新到全局列表
        """
        self.idx = idx
        self.args = args
        # 初始化谷歌翻译引擎
        translator = GoogleTranslator(args.url_base, args.timeout, args.proxies)
        self.func = lambda text, src, tgt: translator.translate(text, tgt, src, cookies=args.cookies)

    def keep_retrying(self, text: str, src: str, tgt: str) -> str:
        """
        执行self.func，但是会自动重试
        :param text: 文本
        :param src: 源语言
        :param tgt: 目标语言
        :return: 翻译后的文本
        """
        for i in range(self.args.retry_times + 1):
            try:
                text = self.func(text, src, tgt)
            except BaseException as e:
                e0 = e
            else:
                return text
        raise e0

    def run(self):
        """生草"""
        global total_progress, finished_thread_cnt
        # 开始生草
        for i in range(self.args.times):
            text = current_text_list[self.idx]  # 从全局变量中获取自己的文本
            if i == 0:  # 第一次自动检测源语言
                src = 'auto'
            tgt = random.choice(self.args.languages)  # 随机目标语言
            text = self.keep_retrying(text, src, tgt)  # 翻译
            current_text_list[self.idx] = text  # 写入全局列表
            total_progress += 1  # 总进度+1（经测试，这一操作在Python3.11中是安全的）
            src = tgt  # 这次的目标语言作为下一次的源语言

        # 完成的线程数+1
        finished_thread_cnt += 1

    def __call__(self):
        global error
        try:
            self.run()
        except BaseException as e:
            error = e


def main(args: TypedNamespace):
    global current_text_list
    # 初始化
    init()
    # 必须用英文输出，不然github actions解码不了
    # print('Arguments:', args)

    # 读取文本
    with open(args.read, encoding='utf-8') as f:
        text = f.read()

    # 分割文本
    text_list = [text] if not args.sentences else str_utils.split_with_keeping_separators(text, args.separator)
    max_progress = len(text_list) * args.times  # 进度最大值，即完成时的进度值
    print('Text list:', text_list)
    print(f'There are {len(text_list)} sentences in all, it will request for {max_progress} times.')

    # 线程池
    with ThreadPoolExecutor(max_workers=args.max_thread_cnt) as pool:
        # 将文本复制给全局列表
        current_text_list = text_list.copy()
        # 将任务提交给线程池
        for i in range(len(text_list)):
            pool.submit(ThreadTranslateOne(i, args))

        # 持续输出
        with tqdm(total=max_progress, desc="Growing grass") as pbar:
            while True:
                # 输出结果
                with open(f'{args.output}.txt', mode='w', encoding='utf-8') as f:
                    f.write(''.join(current_text_list))

                # 更新进度条
                pbar.update(total_progress - pbar.n)
                # 检测完成
                if pbar.n == max_progress:
                    pbar.write("Finished growing grass.")
                    break

                # 检查报错
                if error is not None:
                    try:
                        raise error
                    except:
                        logging.exception('核心出错')
                    raise error

                # 防止cpu爆掉，并防止输出占用太多时间导致生草线程没时间运行
                time.sleep(0.01)


if __name__ == '__main__':
    # 初始化logging
    logging.basicConfig(filename='错误日志.txt', encoding='utf-8')
    # 接受参数
    parser = argparse.ArgumentParser('谷歌生草机核心')
    parser.add_argument('-r', '--read', type=str, required=True, help='要生草的文件路径')
    parser.add_argument('-o', '--output', type=str, required=True, help='输出的文件路径，不带后缀')
    parser.add_argument('-u', '--url-base', type=str, default='https://translate.google.com',
                        help='谷歌翻译（镜像）网站，默认为谷歌翻译官网（中国大陆不可用）')
    parser.add_argument('-ts', '--times', type=int, default=20, help='翻译次数，默认为20')
    parser.add_argument('-to', '--timeout', type=int, default=5, help='超时，默认为5')
    parser.add_argument('-rt', '--retry-times', type=int, default=5, help='自动重试次数，默认为5')
    parser.add_argument('-sn', '--sentences', action='store_true', help='使用逐句翻译，默认不开启')
    parser.add_argument('-p', '--proxies', type=eval, help='代理，应输入字典，用引号括住，默认为None')
    parser.add_argument('-l', '--languages', type=str, default='ALL', help='使用的语言，默认为ALL，联合国六大语言为UN6')
    parser.add_argument('-c', '--cookies', type=str, help='自定义cookies，默认为None')
    parser.add_argument('-m', '--max-thread-cnt', type=int, default=100, help='最大线程数量，默认为100')
    parser.add_argument('-sp', '--separator', type=str, default='\n。？！：,.', help='分隔符，默认为\\n。？！：,.')
    _args: TypedNamespace = parser.parse_args()
    _args.languages = eval(_args.languages)
    _args.separator = _args.separator.replace('\\n', '\n')
    main(_args)
