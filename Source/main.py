from musicplayer import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
import wget
import pygame
from mutagen.mp3 import MP3
import _thread


class musicPlayer(QMainWindow):
    handle_menu = 0
    handle_download = 0
    handle_info = 0
    handle_volume = 0
    handle_play = "Play"
    connection = False
    volume_level = 0
    play_position = "Stop"
    music_address = r"C:\Users\sajjad\Desktop\Yas Sarbaze Vatan_(www.new-song.ir).mp3"
    hours_music = 0
    minutes_music = 0
    seconds_music = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Music Player")
        self.setWindowIcon(QIcon("photo/music.png"))

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.temp1_frame.hide()
        self.ui.temp2_frame.hide()
        self.ui.temp3_frame.hide()
        self.ui.download_frame.hide()
        self.ui.menu_frame.hide()
        self.ui.info_frame.hide()
        self.ui.volume_frame.hide()
        self.ui.conn_label.hide()
        self.ui.downloaad_frame_proccessbar.hide()
        self.ui.progressBar.setValue(0)
        self.ui.volume_Slider.setRange(0, 100)
        self.ui.volume_Slider.setFocusPolicy(Qt.NoFocus)
        self.ui.volume_Slider.setPageStep(1)

        pygame.mixer.init()

        self.ui.btn_menu.clicked.connect(self.menu_func)
        self.ui.btn_volume.clicked.connect(self.volume_func)
        self.ui.btn_play.clicked.connect(self.play_func)
        self.ui.btn_stop.clicked.connect(self.stop_func)

    def play_slider(self, x):
        audio = MP3(self.music_address)
        self.ui.horizontalSlider.setRange(0, int(audio.info.length))
        while True:
            if self.play_position == "Play":
                self.ui.horizontalSlider.setValue(int(pygame.mixer.music.get_pos() / 1000))
            elif self.play_position == "Stop":
                self.ui.horizontalSlider.setValue(0)
                self.stop_func()
                break
            if int(audio.info.length) == int(pygame.mixer.music.get_pos() / 1000):
                self.ui.horizontalSlider.setValue(0)
                self.stop_func()
                break

    def convert_time(self, seconds):
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        self.hours_music = hours
        self.minutes_music = minutes
        self.seconds_music = seconds

    def play_func(self):
        if self.play_position == "Play" or self.play_position == "Pause":
            self.pause_func()
        elif self.play_position == "Stop":
            if len(self.music_address) != 0:
                pygame.mixer.music.load(self.music_address)
                pygame.mixer.music.play()
                self.play_position = "Play"
                _thread.start_new_thread(self.play_slider, (2,))
                self.play_pause_icon()
            else:
                self.showError("Error", "Please choose a music from List.")

    def play_pause_icon(self):
        _translate = QCoreApplication.translate
        if self.handle_play == "Play":
            icon1 = QIcon()
            icon1.addPixmap(QPixmap("photo/outline_pause_white_24dp.png"), QIcon.Normal, QIcon.Off)
            self.ui.btn_play.setIcon(icon1)
            self.handle_play = "Pause"
            self.ui.btn_play.setToolTip(_translate("MainWindow", "Pause"))
        elif self.handle_play == "Pause":
            icon1 = QIcon()
            icon1.addPixmap(QPixmap("photo/outline_play_arrow_white_24dp.png"), QIcon.Normal, QIcon.Off)
            self.ui.btn_play.setIcon(icon1)
            self.handle_play = "Play"
            self.ui.btn_play.setToolTip(_translate("MainWindow", "Play"))

    def pause_func(self):
        self.play_pause_icon()
        if self.play_position == "Play":
            pygame.mixer.music.pause()
            self.play_position = "Pause"
        elif self.play_position == "Pause":
            pygame.mixer.music.unpause()
            self.play_position = "Play"

    def stop_func(self):
        pygame.mixer.music.stop()
        self.play_position = "Stop"
        _translate = QCoreApplication.translate
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("photo/outline_play_arrow_white_24dp.png"), QIcon.Normal, QIcon.Off)
        self.ui.btn_play.setIcon(icon1)
        self.handle_play = "Play"
        self.ui.btn_play.setToolTip(_translate("MainWindow", "Play"))

    def Anim_frame(self, frame, x, y, width, height, openState, frame_name):
        if openState:
            self.anim = QPropertyAnimation(frame, b"geometry")
            self.anim.setDuration(500)
            if frame_name == "download":
                self.anim.setStartValue(QRect(x, y, width, 0))
                self.anim.setEndValue(QRect(x, y, width, height))
            elif frame_name == "volume":
                self.anim.setStartValue(QRect(x, y, width, 0))
                self.anim.setEndValue(QRect(x, y, width, height))
            else:
                self.anim.setStartValue(QRect(x, y, 0, height))
                self.anim.setEndValue(QRect(x, y, width, height))
            self.anim.start()
        else:
            self.anim = QPropertyAnimation(frame, b"geometry")
            self.anim.setDuration(500)
            if frame_name == "download":
                self.anim.setStartValue(QRect(x, y, width, height))
                self.anim.setEndValue(QRect(x, y, width, 0))
            elif frame_name == "volume":
                self.anim.setStartValue(QRect(x, y, width, height))
                self.anim.setEndValue(QRect(x, y, width, 0))
            else:
                self.anim.setStartValue(QRect(x, y, width, height))
                self.anim.setEndValue(QRect(x, y, 0, height))
            self.anim.start()

    def menu_func(self):
        if self.handle_menu == 0:
            self.ui.menu_frame.show()
            self.Anim_frame(self.ui.menu_frame, 509, 0, 291, 591, True, "menu")
            self.ui.btn_menu.setStyleSheet("QPushButton{\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(95, 95, 95);\n"
                                           "border-radius:10px;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    \n"
                                           "    \n"
                                           "    background-color: rgb(95, 95, 95);\n"
                                           "border-radius:5px;\n"
                                           "}")
            self.handle_menu = 1
        elif self.handle_menu == 1:
            self.Anim_frame(self.ui.menu_frame, 509, 0, 291, 591, False, "menu")
            self.ui.btn_menu.setStyleSheet("QPushButton{\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: none;\n"
                                           "border-radius:10px;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    \n"
                                           "    \n"
                                           "    background-color: rgb(95, 95, 95);\n"
                                           "border-radius:5px;\n"
                                           "}")
            self.handle_menu = 0

        self.ui.download_btn_menu.clicked.connect(self.download_menu_func)
        self.ui.info_btn_menu.clicked.connect(self.info_func)

        # we should list all of music in menu list when user click on menu btn

    def download_menu_func(self):
        self.ui.downloaad_frame_proccessbar.hide()
        _translate = QCoreApplication.translate
        self.check_conn()
        if self.connection:
            self.ui.conn_label.setPixmap(QPixmap("photo/icons8-wi-fi-green.png"))
            self.ui.conn_label.show()
            self.ui.conn_label.setToolTip(_translate("MainWindow", "Connect to internet"))
        else:
            self.ui.conn_label.setPixmap(QPixmap("photo/icons8-wi-fi-red.png"))
            self.ui.conn_label.show()
            self.ui.conn_label.setToolTip(_translate("MainWindow", "Disconnect"))
        # =========================================================================
        if self.handle_download == 0:
            self.ui.download_frame.show()
            self.Anim_frame(self.ui.download_frame, 60, 590, 740, 111, True, "download")
            self.ui.download_btn_menu.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:10px;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    \n"
                                                    "    \n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")
            self.handle_download = 1
        elif self.handle_download == 1:
            self.ui.conn_label.hide()
            self.Anim_frame(self.ui.download_frame, 60, 590, 740, 111, False, "download")
            self.ui.download_btn_menu.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: none;\n"
                                                    "border-radius:10px;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    \n"
                                                    "    \n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")
            self.handle_download = 0

        self.ui.download_btn_download.clicked.connect(self.download_btn_func)
        self.ui.choose_btn_download.clicked.connect(self.choose_file)

    def download_btn_func(self):
        if self.connection:
            if len(self.ui.link_lineEdit.text()) != 0:
                if len(self.address_file) != 0:
                    self.ui.downloaad_frame_proccessbar.show()
                    try:
                        wget.download(self.ui.link_lineEdit.text(), self.address_file, bar=self.Handle_Progress)
                        self.showInfo("Download", "Download is successful.")
                        self.ui.progressBar.setValue(0)
                    except:
                        self.showError("Error", "Something went wrong.")
                else:
                    self.showError("Error", "You should choose an address for save file.")
            else:
                self.showError("Error", "You should fill link.")
        else:
            self.showError("Connection", "Please check your connection.")

    def Handle_Progress(self, current, total, width=80):
        value = current / total * 100
        self.ui.progressBar.setValue(int(value))

    def choose_file(self):
        self.address_file = QFileDialog.getExistingDirectory(self, "Choose Directory", "C:/Users/sajjad/Desktop")

    def info_func(self):
        if self.handle_info == 0:
            self.ui.info_frame.show()
            self.Anim_frame(self.ui.info_frame, 800, 0, 71, 591, True, "info")
            self.ui.info_btn_menu.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:10px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    \n"
                                                "    \n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:5px;\n"
                                                "}")
            self.handle_info = 1
        elif self.handle_info == 1:
            self.Anim_frame(self.ui.info_frame, 800, 0, 71, 591, False, "info")
            self.ui.info_btn_menu.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: none;\n"
                                                "border-radius:10px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    \n"
                                                "    \n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:5px;\n"
                                                "}")
            self.handle_info = 0
        self.ui.btn_author.clicked.connect(self.author_func)
        self.ui.btn_insta.clicked.connect(self.insta_func)
        self.ui.btn_telegram.clicked.connect(self.telegram_func)

    def volume_func(self):
        if self.handle_volume == 0:
            self.ui.volume_frame.show()
            self.Anim_frame(self.ui.volume_frame, -1, 110, 61, 361, True, "volume")
            self.ui.btn_volume.setStyleSheet("QPushButton{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    background-color: rgb(95, 95, 95);\n"
                                             "border-radius:10px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    \n"
                                             "    \n"
                                             "    background-color: rgb(95, 95, 95);\n"
                                             "border-radius:5px;\n"
                                             "}")
            self.handle_volume = 1
        elif self.handle_volume == 1:
            self.Anim_frame(self.ui.volume_frame, -1, 110, 61, 361, False, "volume")
            self.ui.btn_volume.setStyleSheet("QPushButton{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    background-color: none;\n"
                                             "border-radius:10px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    \n"
                                             "    \n"
                                             "    background-color: rgb(95, 95, 95);\n"
                                             "border-radius:5px;\n"
                                             "}")
            self.handle_volume = 0

        self.ui.btn_volume_up.clicked.connect(self.volume_up_func)
        self.ui.btn_volume_down.clicked.connect(self.volume_down_func)
        self.ui.btn_volume_mute.clicked.connect(self.volume_mute_func)
        self.ui.volume_Slider.valueChanged.connect(self.volume_slider_func)

    def volume_slider_func(self, value):
        self.volume_level = value / 100
        pygame.mixer.music.set_volume(self.volume_level)
        self.ui.volume_Slider.setToolTip(str(int(value)))

    def volume_mute_func(self):
        pygame.mixer.music.set_volume(0)
        self.volume_level = 0
        self.ui.volume_Slider.setValue(int(self.volume_level * 100))
        self.volume_slider_func(self.volume_level * 100)

    def volume_down_func(self):
        volume = pygame.mixer.music.get_volume()
        if not volume - 0.02 < 0:
            volume -= 0.02
        else:
            volume = 0
        self.volume_level = volume
        pygame.mixer.music.set_volume(self.volume_level)
        self.ui.volume_Slider.setValue(int(self.volume_level * 100))
        self.volume_slider_func(self.volume_level * 100)

    def volume_up_func(self):
        volume = pygame.mixer.music.get_volume()
        if not volume + 0.02 > 1:
            volume += 0.02
        else:
            volume = 1
        self.volume_level = volume
        pygame.mixer.music.set_volume(self.volume_level)
        self.ui.volume_Slider.setValue(int(self.volume_level * 100))
        self.volume_slider_func(self.volume_level * 100)

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def check_conn(self):
        url = r"https://www.google.com"
        timeout = 2
        try:
            requests.get(url, timeout=timeout)
            self.connection = True
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.connection = False

    def showInfo(self, title, msg):
        info = QMessageBox(self)
        info.setIcon(QMessageBox.Information)
        info.setText(msg)
        info.setWindowTitle(title)
        info.show()

    def showError(self, title, msg):
        info = QMessageBox(self)
        info.setIcon(QMessageBox.Critical)
        info.setText(msg)
        info.setWindowTitle(title)
        info.show()

    def author_func(self):
        self.showInfo("Author", "   Sajjad Fani   ")

    def insta_func(self):
        self.showInfo("Instagram", " @sjdfani")

    def telegram_func(self):
        self.showInfo("Telegram", " @sajad_fani")


def setup():
    app = QApplication([])
    ui = musicPlayer()
    ui.show()
    app.exec_()


setup()
