import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QIcon, QMovie, QPixmap
from qfluentwidgets import SplitFluentWindow, FluentIcon, Flyout, MessageBox, NavigationItemPosition

import interfaces
import translate
import other_functions
import web
import doc

__version__ = '4.0.0-pre2'


class Window(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f'谷歌生草机 {__version__}')
        self.setWindowIcon(QIcon('img/icon.png'))
        self.resize(800, 600)

        # 添加子界面
        self.ui_t = interfaces.InterfaceTranslate()
        self.addSubInterface(self.ui_t, FluentIcon.HOME, '生草')

        self.ui_w = interfaces.InterfaceWeb()
        self.addSubInterface(self.ui_w, FluentIcon.WIFI, '生草网页')

        self.ui_d = interfaces.InterfaceDoc()
        self.addSubInterface(self.ui_d, FluentIcon.DOCUMENT, '生草文档（实验功能）')

        self.ui_s = interfaces.InterfaceSettings()
        self.addSubInterface(self.ui_s, FluentIcon.SETTING, '设置', position=NavigationItemPosition.BOTTOM)

        self.ui_a = interfaces.InterfaceAbout()
        self.addSubInterface(self.ui_a, FluentIcon.INFO, '关于', position=NavigationItemPosition.BOTTOM)

        # gif
        self.movie = QMovie('img/loading.gif')

        # 初始化窗口
        self.init_window()

        # 翻译线程
        self.thread_start = translate.ThreadStartTranslating(self)
        # 计时器线程
        self.thread_timer = other_functions.ThreadTimer()
        # 生草网页
        self.wpg = web.WebPageGetter(self)
        # 生草文档
        self.Docgetter = doc.DocGetter
        # 下载音频
        self.thread_mp3 = other_functions.ThreadDownloadMP3(self)
        # 连接信号与槽
        self.connect()

        # 捕捉主线程报错
        sys.excepthook = self.error

    def init_window(self):
        # 加载gif
        self.ui_t.ImageLabel.setMovie(self.movie)
        self.movie.stop()

        # 语言设置下拉框
        self.ui_s.ComboBox_lang.addItem('所有语言')
        self.ui_s.ComboBox_lang.addItem('仅联合国六大语言')

        # 给按钮添加图标
        self.ui_t.PrimaryPushButton_start.setIcon(FluentIcon.PLAY)
        self.ui_t.PushButton_ctrl_c.setIcon(FluentIcon.COPY)
        self.ui_t.PushButton_ctrl_v.setIcon(FluentIcon.PASTE)
        self.ui_t.PushButton_download_mp3.setIcon(FluentIcon.DOWNLOAD)
        self.ui_a.HyperlinkButton_mczhdbk.setIcon(FluentIcon.LINK)
        self.ui_a.HyperlinkButton_xdedan.setIcon(FluentIcon.LINK)
        self.ui_a.HyperlinkButton_thun888.setIcon(FluentIcon.LINK)
        self.ui_a.HyperlinkButton_gitee.setIcon(FluentIcon.LINK)
        self.ui_a.HyperlinkButton_statistics.setIcon(FluentIcon.PIE_SINGLE)
        self.ui_a.AvatarWidget_mczhdbk.setPixmap(QPixmap('img/MC着火的冰块.png').scaled(40, 40))
        self.ui_a.AvatarWidget_xdedan.setPixmap(QPixmap('img/薛定谔的按钮.png').scaled(40, 40))
        self.ui_a.AvatarWidget_thun888.setPixmap(QPixmap('img/thun888.png').scaled(40, 40))

        # 生草网页下拉框
        self.ui_w.ComboBox_where.addItem('URL')
        self.ui_w.ComboBox_where.addItem('HMTL')

        # 生草文本下拉框
        self.ui_d.ComboBox_where.addItem('TXT')
        self.ui_d.ComboBox_where.addItem('PDF')
        # self.ui_d.ComboBox_where.addItem('Word')

    def connect(self):
        # 开始翻译按钮
        self.ui_t.PrimaryPushButton_start.clicked.connect(self.thread_start.start)
        # 开始翻译线程
        self.thread_start.started.connect(lambda: self.set_enabled(False))  # 禁用组件
        self.thread_start.started.connect(self.movie.start)  # 开启gif
        self.thread_start.finished.connect(lambda: self.set_enabled(True))  # 启用组件
        self.thread_start.finished.connect(self.movie.stop)  # 停止gif
        self.thread_start.sig_success.connect(self.msgbox_finished)  # 弹窗提醒
        self.thread_start.sig_pb_sv.connect(self.ui_t.ProgressBar.setVal)  # 设置进度条值
        self.thread_start.sig_pb_sm.connect(self.ui_t.ProgressBar.setMaximum)  # 设置进度条最大值
        self.thread_start.sig_tpbi_st.connect(self.ui_t.TransparentPushButton_info.setText)  # 显示信息
        self.thread_start.sig_pteo_spt.connect(self.ui_t.PlainTextEdit_output.setPlainText)  # 输出文本
        self.thread_start.sig_error.connect(self.error)  # 报错
        # 信息标签浮出详细信息
        self.ui_t.TransparentPushButton_info.clicked.connect(self.flyout_info)
        # 复制粘贴
        self.ui_t.PushButton_ctrl_c.clicked.connect(lambda: other_functions.ctrl_c(self))
        self.ui_t.PushButton_ctrl_v.clicked.connect(lambda: other_functions.ctrl_v(self))
        # 下载音频
        # self.ui_t.PushButton_download_mp3.clicked.connect(lambda: other_functions.download_mp3(self))
        self.ui_t.PushButton_download_mp3.clicked.connect(self.thread_mp3.start)
        self.thread_mp3.started.connect(lambda: self.ui_t.PushButton_download_mp3.setEnabled(False))
        self.thread_mp3.started.connect(self.thread_mp3.set_path)
        self.thread_mp3.finished.connect(lambda: self.ui_t.PushButton_download_mp3.setEnabled(True))
        self.thread_mp3.finished.connect(self.thread_mp3.msgbox)
        # 计时器
        self.thread_timer.sig_slt_st.connect(self.ui_t.SubtitleLabel_timer.setText)
        self.thread_start.started.connect(self.thread_timer.start)
        self.thread_start.finished.connect(self.thread_timer.turn_off)
        # 生草网页
        self.ui_w.PushButton_choose_file.clicked.connect(self.wpg.choose_file)
        self.ui_w.PushButton_get_text.clicked.connect(self.wpg.get_text)
        self.ui_w.PushButton_make_html.clicked.connect(self.wpg.make_html)
        # 生草文档
        self.dg = doc.DocGetter(self)
        self.ui_d.PushButton_choose_file.clicked.connect(self.dg.choose_file)
        self.ui_d.PushButton_get_text.clicked.connect(self.dg.get_text)
        # self.ui_d.PushButton_make_doc.clicked.connect(self.dg.make_txt)
        self.ui_d.PushButton_go.clicked.connect(self.ui_t.PrimaryPushButton_start.clicked.emit)

    def set_enabled(self, enabled: bool):
        # 生草
        self.ui_t.PrimaryPushButton_start.setEnabled(enabled)
        self.ui_t.PushButton_ctrl_c.setEnabled(enabled)
        self.ui_t.PushButton_ctrl_v.setEnabled(enabled)
        self.ui_t.PushButton_download_mp3.setEnabled(enabled)
        self.ui_t.PlainTextEdit_input.setEnabled(enabled)
        self.ui_t.SpinBox_times.setEnabled(enabled)
        self.ui_t.SpinBox_timeout.setEnabled(enabled)
        self.ui_t.SpinBox_retry.setEnabled(enabled)
        self.ui_t.RadioButton_together.setEnabled(enabled)
        self.ui_t.RadioButton_sentences.setEnabled(enabled)
        self.ui_t.LineEdit_url_base.setEnabled(enabled)
        # 设置
        self.ui_s.CheckBox_proxies.setEnabled(enabled)
        self.ui_s.LineEdit_http.setEnabled(enabled)
        self.ui_s.LineEdit_https.setEnabled(enabled)
        self.ui_s.ComboBox_lang.setEnabled(enabled)
        # 文档
        self.ui_d.PushButton_go.setEnabled(enabled)
        self.ui_d.PushButton_make_doc.setEnabled(enabled)
        self.ui_d.PushButton_get_text.setEnabled(enabled)

    def flyout_info(self):
        Flyout.create('详细信息', self.thread_start.info, target=self.ui_t.TransparentPushButton_info,
                      icon=FluentIcon.INFO)

    def msgbox_finished(self):
        w = MessageBox('谷歌生草机', '生草完成', self)
        w.exec()

    def error(self, etype, value, tb):
        """弹窗报错，而不是直接崩溃"""
        format_exc = ''.join(traceback.format_exception(etype, value, tb))
        QMessageBox.critical(self, '错误', format_exc)
        print(format_exc)
        try:
            translate.ERROR_DICT[etype]
        except KeyError:
            translate.ERROR_DICT[etype] = '未知错误，请联系up主'
        w = MessageBox('错误', f'{etype().__class__.__name__}: {value}\n{translate.ERROR_DICT[etype]}', self)
        w.exec()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
