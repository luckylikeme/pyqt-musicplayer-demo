import sys
from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from pyqt5_plugins.examplebuttonplugin import QtGui
import dao.UserDao
from pojo import User


class LoginGui(QDialog):
    def __init__(self):
        super().__init__()
        self.flag = 0
        self.setObjectName("login-container")
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

