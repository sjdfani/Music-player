# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 748)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(879, 699))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(60, 0, 451, 591))
        self.main_frame.setMinimumSize(QtCore.QSize(451, 591))
        self.main_frame.setMaximumSize(QtCore.QSize(451, 591))
        self.main_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #232526, stop:1 #414345);")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.exit_btn = QtWidgets.QPushButton(self.main_frame)
        self.exit_btn.setGeometry(QtCore.QRect(420, 10, 21, 21))
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:10px;")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.mini_btn = QtWidgets.QPushButton(self.main_frame)
        self.mini_btn.setGeometry(QtCore.QRect(390, 10, 21, 21))
        self.mini_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mini_btn.setStyleSheet("background-color: rgb(229, 229, 0);\n"
"border-radius:10px;")
        self.mini_btn.setText("")
        self.mini_btn.setObjectName("mini_btn")
        self.pict_label_bakground = QtWidgets.QLabel(self.main_frame)
        self.pict_label_bakground.setGeometry(QtCore.QRect(0, 40, 451, 551))
        self.pict_label_bakground.setStyleSheet("background-color: none;\n"
"")
        self.pict_label_bakground.setText("")
        self.pict_label_bakground.setObjectName("pict_label_bakground")
        self.btn_frame = QtWidgets.QFrame(self.main_frame)
        self.btn_frame.setGeometry(QtCore.QRect(0, 530, 451, 61))
        self.btn_frame.setStyleSheet("background-color: none;")
        self.btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_frame.setObjectName("btn_frame")
        self.btn_menu = QtWidgets.QPushButton(self.btn_frame)
        self.btn_menu.setGeometry(QtCore.QRect(385, 6, 51, 51))
        self.btn_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet("QPushButton{\n"
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
        self.btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/outline_menu_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(36, 36))
        self.btn_menu.setObjectName("btn_menu")
        self.btn_play = QtWidgets.QPushButton(self.btn_frame)
        self.btn_play.setGeometry(QtCore.QRect(200, 6, 51, 51))
        self.btn_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_play.setStyleSheet("QPushButton{\n"
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
        self.btn_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("photo/outline_play_arrow_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon1)
        self.btn_play.setIconSize(QtCore.QSize(45, 45))
        self.btn_play.setObjectName("btn_play")
        self.btn_repeat = QtWidgets.QPushButton(self.btn_frame)
        self.btn_repeat.setGeometry(QtCore.QRect(320, 6, 51, 51))
        self.btn_repeat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_repeat.setStyleSheet("QPushButton{\n"
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
        self.btn_repeat.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("photo/outline_replay_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_repeat.setIcon(icon2)
        self.btn_repeat.setIconSize(QtCore.QSize(36, 36))
        self.btn_repeat.setObjectName("btn_repeat")
        self.btn_next = QtWidgets.QPushButton(self.btn_frame)
        self.btn_next.setGeometry(QtCore.QRect(260, 6, 51, 51))
        self.btn_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_next.setStyleSheet("QPushButton{\n"
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
        self.btn_next.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("photo/outline_arrow_forward_ios_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon3)
        self.btn_next.setIconSize(QtCore.QSize(36, 36))
        self.btn_next.setObjectName("btn_next")
        self.btn_back = QtWidgets.QPushButton(self.btn_frame)
        self.btn_back.setGeometry(QtCore.QRect(140, 6, 51, 51))
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet("QPushButton{\n"
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
        self.btn_back.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("photo/outline_arrow_back_ios_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon4)
        self.btn_back.setIconSize(QtCore.QSize(36, 36))
        self.btn_back.setObjectName("btn_back")
        self.btn_volume = QtWidgets.QPushButton(self.btn_frame)
        self.btn_volume.setGeometry(QtCore.QRect(15, 6, 51, 51))
        self.btn_volume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_volume.setStyleSheet("QPushButton{\n"
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
        self.btn_volume.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("photo/outline_volume_up_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_volume.setIcon(icon5)
        self.btn_volume.setIconSize(QtCore.QSize(30, 30))
        self.btn_volume.setObjectName("btn_volume")
        self.btn_stop = QtWidgets.QPushButton(self.btn_frame)
        self.btn_stop.setGeometry(QtCore.QRect(80, 6, 51, 51))
        self.btn_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_stop.setStyleSheet("QPushButton{\n"
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
        self.btn_stop.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("photo/outline_stop_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon6)
        self.btn_stop.setIconSize(QtCore.QSize(42, 42))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_favorite = QtWidgets.QPushButton(self.main_frame)
        self.btn_favorite.setGeometry(QtCore.QRect(210, 370, 41, 41))
        self.btn_favorite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_favorite.setAutoFillBackground(False)
        self.btn_favorite.setStyleSheet("QPushButton{\n"
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
        self.btn_favorite.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("photo/outline_favorite_border_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_favorite.setIcon(icon7)
        self.btn_favorite.setIconSize(QtCore.QSize(30, 30))
        self.btn_favorite.setObjectName("btn_favorite")
        self.conn_label = QtWidgets.QLabel(self.main_frame)
        self.conn_label.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.conn_label.setStyleSheet("background-color: none;")
        self.conn_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conn_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.conn_label.setText("")
        self.conn_label.setPixmap(QtGui.QPixmap("photo/icons8-wi-fi-green.png"))
        self.conn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.conn_label.setObjectName("conn_label")
        self.label_mainPict = QtWidgets.QLabel(self.main_frame)
        self.label_mainPict.setGeometry(QtCore.QRect(90, 110, 281, 211))
        self.label_mainPict.setStyleSheet("border-radius:60px;")
        self.label_mainPict.setText("")
        self.label_mainPict.setObjectName("label_mainPict")
        self.horizontalSlider = QtWidgets.QSlider(self.main_frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(0, 490, 451, 22))
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.volume_frame = QtWidgets.QFrame(self.centralwidget)
        self.volume_frame.setGeometry(QtCore.QRect(-1, 110, 61, 361))
        self.volume_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #232526, stop:1 #414345);")
        self.volume_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.volume_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.volume_frame.setObjectName("volume_frame")
        self.volume_Slider = QtWidgets.QSlider(self.volume_frame)
        self.volume_Slider.setGeometry(QtCore.QRect(20, 51, 22, 201))
        self.volume_Slider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.volume_Slider.setStyleSheet("background-color: none;\n"
"")
        self.volume_Slider.setOrientation(QtCore.Qt.Vertical)
        self.volume_Slider.setObjectName("volume_Slider")
        self.btn_volume_up = QtWidgets.QPushButton(self.volume_frame)
        self.btn_volume_up.setGeometry(QtCore.QRect(10, 8, 41, 41))
        self.btn_volume_up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_volume_up.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: none;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(95, 95, 95);\n"
"border-radius:5px;\n"
"}")
        self.btn_volume_up.setText("")
        self.btn_volume_up.setIcon(icon5)
        self.btn_volume_up.setIconSize(QtCore.QSize(25, 25))
        self.btn_volume_up.setObjectName("btn_volume_up")
        self.btn_volume_down = QtWidgets.QPushButton(self.volume_frame)
        self.btn_volume_down.setGeometry(QtCore.QRect(10, 255, 41, 41))
        self.btn_volume_down.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_volume_down.setStyleSheet("QPushButton{\n"
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
        self.btn_volume_down.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("photo/outline_volume_down_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_volume_down.setIcon(icon8)
        self.btn_volume_down.setIconSize(QtCore.QSize(30, 30))
        self.btn_volume_down.setObjectName("btn_volume_down")
        self.btn_volume_mute = QtWidgets.QPushButton(self.volume_frame)
        self.btn_volume_mute.setGeometry(QtCore.QRect(10, 300, 41, 41))
        self.btn_volume_mute.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_volume_mute.setStyleSheet("QPushButton{\n"
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
        self.btn_volume_mute.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("photo/outline_volume_mute_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_volume_mute.setIcon(icon9)
        self.btn_volume_mute.setIconSize(QtCore.QSize(30, 30))
        self.btn_volume_mute.setObjectName("btn_volume_mute")
        self.temp1_frame = QtWidgets.QFrame(self.centralwidget)
        self.temp1_frame.setGeometry(QtCore.QRect(-1, 470, 61, 231))
        self.temp1_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #232526, stop:1 #414345);")
        self.temp1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temp1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temp1_frame.setObjectName("temp1_frame")
        self.info_frame = QtWidgets.QFrame(self.centralwidget)
        self.info_frame.setGeometry(QtCore.QRect(800, 0, 71, 591))
        self.info_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #232526, stop:1 #414345);")
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.btn_insta = QtWidgets.QPushButton(self.info_frame)
        self.btn_insta.setGeometry(QtCore.QRect(14, 534, 51, 51))
        self.btn_insta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_insta.setStyleSheet("QPushButton{\n"
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
        self.btn_insta.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("photo/5335781_camera_instagram_social media_instagram logo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_insta.setIcon(icon10)
        self.btn_insta.setIconSize(QtCore.QSize(35, 35))
        self.btn_insta.setObjectName("btn_insta")
        self.btn_telegram = QtWidgets.QPushButton(self.info_frame)
        self.btn_telegram.setGeometry(QtCore.QRect(14, 460, 51, 51))
        self.btn_telegram.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_telegram.setStyleSheet("QPushButton{\n"
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
        self.btn_telegram.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("photo/7693324_telegram_social media_logo_messenger_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_telegram.setIcon(icon11)
        self.btn_telegram.setIconSize(QtCore.QSize(35, 35))
        self.btn_telegram.setObjectName("btn_telegram")
        self.btn_author = QtWidgets.QPushButton(self.info_frame)
        self.btn_author.setGeometry(QtCore.QRect(14, 386, 51, 51))
        self.btn_author.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_author.setStyleSheet("QPushButton{\n"
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
        self.btn_author.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("photo/5402435_account_profile_user_avatar_man_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_author.setIcon(icon12)
        self.btn_author.setIconSize(QtCore.QSize(40, 40))
        self.btn_author.setObjectName("btn_author")
        self.temp2_frame = QtWidgets.QFrame(self.centralwidget)
        self.temp2_frame.setGeometry(QtCore.QRect(800, 590, 71, 111))
        self.temp2_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #232526, stop:1 #414345);")
        self.temp2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temp2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temp2_frame.setObjectName("temp2_frame")
        self.download_frame = QtWidgets.QFrame(self.centralwidget)
        self.download_frame.setGeometry(QtCore.QRect(60, 590, 740, 111))
        self.download_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #232526, stop:1 #414345);")
        self.download_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.download_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.download_frame.setObjectName("download_frame")
        self.label = QtWidgets.QLabel(self.download_frame)
        self.label.setGeometry(QtCore.QRect(7, 6, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.link_lineEdit = QtWidgets.QLineEdit(self.download_frame)
        self.link_lineEdit.setGeometry(QtCore.QRect(60, 7, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.link_lineEdit.setFont(font)
        self.link_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.link_lineEdit.setObjectName("link_lineEdit")
        self.download_btn_download = QtWidgets.QPushButton(self.download_frame)
        self.download_btn_download.setGeometry(QtCore.QRect(470, 4, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.download_btn_download.setFont(font)
        self.download_btn_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_btn_download.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0f0c29, stop:0.5 #302b63 ,stop:1 #24243e);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(95, 95, 95);\n"
"    border-radius:10px;\n"
"}")
        self.download_btn_download.setObjectName("download_btn_download")
        self.downloaad_frame_proccessbar = QtWidgets.QFrame(self.download_frame)
        self.downloaad_frame_proccessbar.setGeometry(QtCore.QRect(0, 50, 741, 71))
        self.downloaad_frame_proccessbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.downloaad_frame_proccessbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.downloaad_frame_proccessbar.setObjectName("downloaad_frame_proccessbar")
        self.progressBar = QtWidgets.QProgressBar(self.downloaad_frame_proccessbar)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 441, 31))
        self.progressBar.setStyleSheet("QProgressBar::chunk{\n"
"border-radius:15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0f0c29, stop:0.5 #302b63 ,stop:1 #24243e);\n"
"}\n"
"QProgressBar{\n"
"background-color:#CCCCFF;\n"
"color:#000000;\n"
"border-style:none;\n"
"border-radius:15px;\n"
"text-align:center;\n"
"height:50px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.play_btn_download = QtWidgets.QPushButton(self.downloaad_frame_proccessbar)
        self.play_btn_download.setGeometry(QtCore.QRect(470, 3, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.play_btn_download.setFont(font)
        self.play_btn_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play_btn_download.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0f0c29, stop:0.5 #302b63 ,stop:1 #24243e);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(95, 95, 95);\n"
"    border-radius:10px;\n"
"}")
        self.play_btn_download.setObjectName("play_btn_download")
        self.choose_btn_download = QtWidgets.QPushButton(self.download_frame)
        self.choose_btn_download.setGeometry(QtCore.QRect(580, 4, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.choose_btn_download.setFont(font)
        self.choose_btn_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_btn_download.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0f0c29, stop:0.5 #302b63 ,stop:1 #24243e);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(95, 95, 95);\n"
"    border-radius:10px;\n"
"}")
        self.choose_btn_download.setObjectName("choose_btn_download")
        self.temp3_frame = QtWidgets.QFrame(self.centralwidget)
        self.temp3_frame.setGeometry(QtCore.QRect(-1, 0, 61, 111))
        self.temp3_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #232526, stop:1 #414345);")
        self.temp3_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temp3_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temp3_frame.setObjectName("temp3_frame")
        self.menu_frame = QtWidgets.QFrame(self.centralwidget)
        self.menu_frame.setGeometry(QtCore.QRect(509, 0, 291, 591))
        self.menu_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #232526, stop:1 #414345);")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.btn_menu_frame = QtWidgets.QFrame(self.menu_frame)
        self.btn_menu_frame.setGeometry(QtCore.QRect(0, 530, 291, 61))
        self.btn_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_menu_frame.setObjectName("btn_menu_frame")
        self.download_btn_menu = QtWidgets.QPushButton(self.btn_menu_frame)
        self.download_btn_menu.setGeometry(QtCore.QRect(15, 6, 51, 51))
        self.download_btn_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_btn_menu.setStyleSheet("QPushButton{\n"
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
        self.download_btn_menu.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("photo/outline_download_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_btn_menu.setIcon(icon13)
        self.download_btn_menu.setIconSize(QtCore.QSize(35, 35))
        self.download_btn_menu.setObjectName("download_btn_menu")
        self.favorite_btn_menu = QtWidgets.QPushButton(self.btn_menu_frame)
        self.favorite_btn_menu.setGeometry(QtCore.QRect(85, 6, 51, 51))
        self.favorite_btn_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.favorite_btn_menu.setStyleSheet("QPushButton{\n"
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
        self.favorite_btn_menu.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("photo/outline_favorite_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.favorite_btn_menu.setIcon(icon14)
        self.favorite_btn_menu.setIconSize(QtCore.QSize(35, 35))
        self.favorite_btn_menu.setObjectName("favorite_btn_menu")
        self.folder_btn_menu = QtWidgets.QPushButton(self.btn_menu_frame)
        self.folder_btn_menu.setGeometry(QtCore.QRect(155, 6, 51, 51))
        self.folder_btn_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.folder_btn_menu.setStyleSheet("QPushButton{\n"
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
        self.folder_btn_menu.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("photo/outline_folder_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.folder_btn_menu.setIcon(icon15)
        self.folder_btn_menu.setIconSize(QtCore.QSize(35, 35))
        self.folder_btn_menu.setObjectName("folder_btn_menu")
        self.info_btn_menu = QtWidgets.QPushButton(self.btn_menu_frame)
        self.info_btn_menu.setGeometry(QtCore.QRect(225, 6, 51, 51))
        self.info_btn_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.info_btn_menu.setStyleSheet("QPushButton{\n"
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
        self.info_btn_menu.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("photo/outline_info_white_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_btn_menu.setIcon(icon16)
        self.info_btn_menu.setIconSize(QtCore.QSize(35, 35))
        self.info_btn_menu.setObjectName("info_btn_menu")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit_btn.clicked.connect(MainWindow.close)
        self.mini_btn.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit_btn.setToolTip(_translate("MainWindow", "Exit"))
        self.mini_btn.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_menu.setToolTip(_translate("MainWindow", "Menu"))
        self.btn_play.setToolTip(_translate("MainWindow", "Play"))
        self.btn_repeat.setToolTip(_translate("MainWindow", "Repeat"))
        self.btn_next.setToolTip(_translate("MainWindow", "Next"))
        self.btn_back.setToolTip(_translate("MainWindow", "Back"))
        self.btn_volume.setToolTip(_translate("MainWindow", "Volume"))
        self.btn_stop.setToolTip(_translate("MainWindow", "Stop"))
        self.btn_favorite.setToolTip(_translate("MainWindow", "Favorite"))
        self.conn_label.setToolTip(_translate("MainWindow", "Connect to internet"))
        self.btn_volume_up.setToolTip(_translate("MainWindow", "Volume Up"))
        self.btn_volume_up.setShortcut(_translate("MainWindow", "Volume Up"))
        self.btn_volume_down.setToolTip(_translate("MainWindow", "Volume Down"))
        self.btn_volume_down.setShortcut(_translate("MainWindow", "Volume Down"))
        self.btn_volume_mute.setToolTip(_translate("MainWindow", "Mute"))
        self.btn_volume_mute.setShortcut(_translate("MainWindow", "Volume Mute"))
        self.btn_insta.setToolTip(_translate("MainWindow", "Instagram"))
        self.btn_telegram.setToolTip(_translate("MainWindow", "Telegram"))
        self.btn_author.setToolTip(_translate("MainWindow", "Author"))
        self.label.setText(_translate("MainWindow", "Link:"))
        self.download_btn_download.setText(_translate("MainWindow", "Download"))
        self.play_btn_download.setText(_translate("MainWindow", "Play"))
        self.choose_btn_download.setText(_translate("MainWindow", "Choose address"))
        self.download_btn_menu.setToolTip(_translate("MainWindow", "Download"))
        self.favorite_btn_menu.setToolTip(_translate("MainWindow", "Favorite List"))
        self.folder_btn_menu.setToolTip(_translate("MainWindow", "Folder"))
        self.info_btn_menu.setToolTip(_translate("MainWindow", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
