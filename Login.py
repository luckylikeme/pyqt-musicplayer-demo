import sys
from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from pyqt5_plugins.examplebuttonplugin import QtGui
import dao.UserDao
from pojo import User


class LoginGui(QDialog):
    def __init__(self):
        super().__init__()
        self.flag = 0
        self.setObjectName("login-container")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.95)
        self.flag_move = False
        self.setMouseTracking(True)
        # 登录字样
        login_label = QLabel(self)
        login_label.setObjectName("LoginOrRegister")
        login_label.setText("login")
        # login_label.move(250, 150)

        # 用户名字样
        account_label = QLabel(self)
        account_label.setText("账号: ")
        # account_label.move(190, 200)
        account_label.setStyleSheet("font-size: 20px;  font-weight: bold;  margin-bottom: 20px;  color: #999; ")

        # 密码字样
        password_label = QLabel(self)
        password_label.setText("密码: ")
        # password_label.move(190, 230)
        password_label.setStyleSheet("font-size: 20px;  font-weight: bold;  margin-bottom: 20px;  color: #999; ")

        # 输入框
        text_flied1 = QLineEdit(self)
        text_flied1.setObjectName("login-input1")
        # text_flied1.move(250, 200)
        text_flied2 = QLineEdit(self)
        text_flied2.setObjectName("login-input2")
        # text_flied2.move(250, 230)

        # 登录按钮
        btn = QPushButton(self)
        btn.setText("登录")
        btn.resize(100, 40)
        # btn.move(250, 270)
        btn.clicked.connect(self.search_user)

        lay_out = QFormLayout(self)
        lay_out.setWidget(0, QFormLayout.FieldRole, login_label)
        lay_out.setWidget(1, QFormLayout.LabelRole, account_label)
        lay_out.setWidget(1, QFormLayout.FieldRole, text_flied1)
        lay_out.setWidget(2, QFormLayout.LabelRole, password_label)
        lay_out.setWidget(2, QFormLayout.FieldRole, text_flied2)
        lay_out.setWidget(3, QFormLayout.FieldRole, btn)

        # 边框按钮设置
        btn_exit = QPushButton(self)
        icon_exit = QIcon("static/pictrue/close-line.png")
        btn_exit.setIcon(icon_exit)
        btn_exit.resize(30, 30)
        btn_exit.move(230, 0)
        btn_exit.clicked.connect(self.exit)

        btn_subtract = QPushButton(self)
        icon_subtract = QIcon("static/pictrue/subtract-line.png")
        btn_subtract.setIcon(icon_subtract)
        btn_subtract.resize(30, 30)
        btn_subtract.move(200, 0)
        btn_subtract.clicked.connect(self.minSubtract)

        # 登录错误按钮对话框
        self.dialog = QDialog()
        label1 = QLabel(self.dialog)
        label1.setText("登录失败")
        label1.move(40, 30)
        btn1 = QPushButton()
        btn1.setText("确定")
        btn1.setParent(self.dialog)
        btn1.move(60, 60)
        btn1.clicked.connect(self.comfirm_msg)
        self.user = None
        self.dialog.resize(100, 100)

        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.exec_()

    def search_user(self):
        print("函数被调用")
        account = self.findChild(QLineEdit, "login-input1").text()
        password = self.findChild(QLineEdit, "login-input2").text()
        user_dao = dao.UserDao.GetUserDao()
        user = user_dao.select_one(account, password)
        self.user = user

        if user is not None:
            print("验证通过")
            self.hide()
            self.flag = 200

        else:
            print("用户不存在")
            self.dialog.exec_()

    def comfirm_msg(self):
        self.dialog.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        sys.exit()

    def exit(self):
        sys.exit()

    def minSubtract(self):
        self.showMinimized()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.orign_x = self.pos().x()
        self.orign_y = self.pos().y()
        self.mouse_x = a0.globalX()
        self.mouse_y = a0.globalY()
        # print(self.mouse_x, self.mouse_y)
        self.flag_move = True

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.flag_move:
            # print(a0.globalX(), a0.globalY())
            move_x = a0.globalX() - self.mouse_x
            move_y = a0.globalY() - self.mouse_y
            # print(move_x,move_y)
            dest_x = self.orign_x + move_x
            dest_y = self.orign_y + move_y
            # print(dest_x, dest_y)
            self.move(dest_x, dest_y)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.flag_move = False
