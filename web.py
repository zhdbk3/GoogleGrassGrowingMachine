import os

import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QFileDialog


class WebPageGetter:
    def __init__(self, window):
        self.window = window
        self.html = ''
        self.texts = []

    def choose_file(self):
        path = QFileDialog.getOpenFileName(self.window, '选择文件', None, 'HTML文件(*.html)')[0]
        self.window.ui_w.LineEdit_url_or_html.setText(path)

    def get_text(self):
        # 获取网页
        if self.window.ui_w.ComboBox_where.currentIndex() == 0:
            # url
            response = requests.get(self.window.ui_w.LineEdit_url_or_html.text())
            response.encoding = 'utf-8'
            self.html = response.text
        elif self.window.ui_w.ComboBox_where.currentIndex() == 1:
            # html
            with open(self.window.ui_w.LineEdit_url_or_html.text(), encoding='utf-8') as f:
                self.html = f.read()
        # 提取文本
        soup = BeautifulSoup(self.html, 'lxml')
        self.texts = soup.stripped_strings
        joined_texts = '\n'.join(self.texts)
        print(joined_texts)
        # 设置输入框
        self.window.ui_t.PlainTextEdit_input.setPlainText(joined_texts)

    def make_html(self):
        # 生成html
        old_texts = self.window.ui_t.PlainTextEdit_input.toPlainText()
        list_old = old_texts.split('\n')
        new_texts = self.window.ui_t.PlainTextEdit_output.toPlainText()
        list_new = new_texts.split('\n')
        new_html = self.html
        for i, j in zip(list_old, list_new):
            new_html = new_html.replace(i, j)

        # 保存
        path = QFileDialog.getSaveFileName(self.window, '保存网页', None, 'HTML文件(*.html)')[0]
        with open(path, mode='w', encoding='utf-8') as f:
            f.write(new_html)

        # 打开网页
        os.popen(f'start {path}')
