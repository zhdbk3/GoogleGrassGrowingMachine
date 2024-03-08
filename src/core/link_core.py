from argparse import Namespace

from .languages import *

if __name__ == '__main__':
    from main import Window


def get_args(window: "Window") -> Namespace:
    """
    从GUI中读取参数
    :param window: window
    :return: 核心需要的命名空间
    """
    args = Namespace()
    args.read = 'tmp/gui_input.txt'
    args.output = 'tmp/gui_output.txt'
    args.url_base = window.ui_settings.SearchLineEdit_url_base.text()
    args.times = window.ui_translate.SpinBox_times.value()
    args.timeout = window.ui_translate.SpinBox_timeout.value()
    args.retry_times = window.ui_translate.SpinBox_retry.value()
    args.sentences = window.ui_translate.RadioButton_sentences.isChecked()
    if window.ui_settings.CheckBox_proxies.isChecked():
        args.proxies = {
            'http': window.ui_settings.LineEdit_http.text(),
            'https': window.ui_settings.LineEdit_https.text(),
            'socks5': window.ui_settings.LineEdit_socks5.text(),
        }
    else:
        args.proxies = None
    match window.ui_settings.ComboBox_lang.currentIndex():
        case 0:
            args.languages = ALL
        case 1:
            args.languages = UN6
    if len(cookies := window.ui_settings.LineEdit_cookies.text()) > 0:
        args.cookies = cookies
    else:
        args.cookies = None
    args.max_thread_count = window.ui_settings.SpinBox_max_thread_cnt.value()
    args.separators = window.ui_settings.LineEdit_separator.text()
    return args
