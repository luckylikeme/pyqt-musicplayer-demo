import sys

from PyQt5.QtCore import Qt
import qdarkstyle
import Login
from PyQt5.QtWidgets import *
from pojo import *
from pojo.User import User


def load_user_message(user, user1):
    user.user_id = user1[0]
    user.account = user1[1]
    user.nick_name = user1[2]
    user.sex = user1[3]
    user.password = user1[4]
    user.auth = user1[5]


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)
    # 加载样式表
    qApp.setStyleSheet(open('static/music_player.qss').read()+qdarkstyle.load_stylesheet_pyqt5())
    # 登录验证结束后才可以进行入的主窗口
    window = QWidget()
    user = User()
    # 进入登录流程
    frame1 = Login.LoginGui()
    frame1.setParent(window)
    if frame1.flag == 200:
        # 稍后删除
        frame1.deleteLater()
        window.resize(600, 600)
        window.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        window.setWindowTitle("禅铲馋播放器")
        window.show()
        load_user_message(user, frame1.user)

    # 进入事件循环
    sys.exit(app.exec_())
