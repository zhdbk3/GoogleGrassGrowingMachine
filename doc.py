import os
from PyQt5.QtWidgets import QFileDialog
import PyPDF2


class DocGetter:
    def __init__(self, window):
        self.window = window
        self.path = ''
        self.txt = ''
        self.texts = []
        self.pdf = []

    def choose_file(self):
        self.path = QFileDialog.getOpenFileName(self.window,
                                                '选择文件',
                                                None,
                                                'Text files (*.txt);;Word documents (*.doc *.docx);;PDF files (*.pdf);')[
            0]
        self.window.ui_d.LineEdit_doc.setText(self.path)

    # fileName,fileType = QFileDialog.getOpenFileName(self,
    #                                                 "please open excel file",
    #                                                  r"F:\autoTest\20181015_Cases",
    #                                                 "Text Files (*.txt);;Text Files (*.xlsx;*.xls);;")#设置文件扩展名过滤

    def run(self):
        if self.window.ui_d.ComboBox_where.currentIndex() == 0:
            self.make_txt()
            self.save_txt()
        elif self.window.ui_d.ComboBox_where.currentIndex() == 1:
            print('pdf!')

    def get_text(self):
        # 获取文件
        if self.window.ui_d.ComboBox_where.currentIndex() == 0:
            # txt
            with open(self.window.ui_d.LineEdit_doc.text(), encoding='utf-8') as f:
                self.txt = f.read()
            # 设置输入框
            self.window.ui_t.PlainTextEdit_input.setPlainText(self.txt)
            # 提取文本
            # self.txt = self.txt()  # 狗屁不通
            # print(self.txt)

        elif self.window.ui_d.ComboBox_where.currentIndex() == 1:
            # PDF
            # path_pdf = f"'{self.path}'"
            # print(path_pdf)               #注意：PyPDF中路径用无引号
            # with open(self.window.ui_d.LineEdit_doc.text(), encoding='utf-8') as f:
            #     self.pdf = f.read()
            pdfFile = open(self.path, 'rb')
            # print(pdfFile)
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            print(pdfReader.Pages)
            # 设置输入框
            self.window.ui_t.PlainTextEdit_input.setPlainText(self.txt)

    def make_txt(self):
        # 生成txt
        new_txt = self.window.ui_t.PlainTextEdit_output.toPlainText()
        self.txt = new_txt

    def save_txt(self):
        # 保存
        path = QFileDialog.getSaveFileName(self.window, '合成文件', None, 'Text files (*.txt)')[0]
        with open(path, mode='w', encoding='utf-8') as f:
            f.write(self.txt)

        # 打开文件
        os.popen(f'start {path}')

# ###pdf写法备忘:
# import pdfrw

# # 打开PDF文件
# input_pdf = pdfrw.PdfReader('example.pdf')

# # 获取第一页的内容
# page1 = input_pdf.pages[0]

# # 获取第一页中的文本信息
# page1_text = page1.extract_text()

# # 修改文本信息
# new_text = page1_text.replace('old_text', 'new_text')

# # 更新第一页的内容
# page1.Contents = pdfrw.objects.pdfstring.PdfString(new_text.encode('utf-8'))

# # 创建一个新的PDF对象
# output_pdf = pdfrw.PdfWriter()

# # 将更新后的第一页添加到新的PDF对象中
# output_pdf.addpage(page1)

# # 保存修改后的PDF文件
# output_pdf.write('output.pdf')


#
