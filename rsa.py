from PyQt5 import QtCore, QtGui, QtWidgets
import rsa


class Ui_MainWindow(object):
    def __init__(self):
        self.gen_key = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.label.setStyleSheet("font: 14pt \"Arial\";\n"
                                 "margin-left: 10px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 45, 100, 30))
        self.label_2.setStyleSheet("font: 14pt \"Arial\";\n"
                                   "margin-left: 10px")
        self.label_2.setObjectName("label_2")
        self.text_pubKey = QtWidgets.QTextEdit(self.centralwidget)
        self.text_pubKey.setGeometry(QtCore.QRect(100, 10, 435, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_pubKey.setFont(font)
        self.text_pubKey.setObjectName("text_pubKey")
        self.text_Privkey = QtWidgets.QTextEdit(self.centralwidget)
        self.text_Privkey.setGeometry(QtCore.QRect(100, 45, 435, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_Privkey.setFont(font)
        self.text_Privkey.setObjectName("text_Privkey")
        self.gen_key = QtWidgets.QPushButton(self.centralwidget)
        self.gen_key.setGeometry(QtCore.QRect(436, 90, 100, 30))
        self.gen_key.setStyleSheet("")
        self.gen_key.setObjectName("gen_key")
        self.gen_key.clicked.connect(self.gen_keyy)
        self.text_first = QtWidgets.QTextEdit(self.centralwidget)
        self.text_first.setGeometry(QtCore.QRect(30, 150, 541, 71))
        self.text_first.setObjectName("text_first")
        self.encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt.setGeometry(QtCore.QRect(250, 240, 100, 30))
        self.encrypt.setStyleSheet("")
        self.encrypt.setObjectName("encrypt")
        self.encrypt.clicked.connect(self.encryptt)
        self.decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt.setGeometry(QtCore.QRect(250, 280, 100, 30))
        self.decrypt.setStyleSheet("")
        self.decrypt.setObjectName("decrypt")
        self.decrypt.clicked.connect(self.decryptt)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 215, 521, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA_Example"))
        self.label.setText(_translate("MainWindow", "Pubkey:"))
        self.label_2.setText(_translate("MainWindow", "Privkey:"))
        self.gen_key.setText(_translate("MainWindow", "Gen_new_key"))
        self.encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.decrypt.setText(_translate("MainWindow", "Decrypt"))

    def gen_keyy(self):
        (self.pubkey, self.privkey) = rsa.newkeys(2048)
        self.text_pubKey.setText(str(self.pubkey))
        self.text_Privkey.setText(str(self.privkey))

        pub = open('pubkey.txt', 'w')
        pub.write(str(self.pubkey.n))
        pub.write('\n')
        pub.write(str(self.pubkey.e))
        pub.close()

        priv = open('privkey.txt', 'w')
        priv.write(str(self.privkey.n))
        priv.write('\n')
        priv.write(str(self.privkey.e))
        priv.write('\n')
        priv.write(str(self.privkey.d))
        priv.write('\n')
        priv.write(str(self.privkey.p))
        priv.write('\n')
        priv.write(str(self.privkey.q))
        priv.close()

    def encryptt(self):
        message = self.text_first.toPlainText()
        message = message.encode()

        pub = open('pubkey.txt', 'r')
        n = pub.readline()
        e = pub.readline()
        pub.close()

        pubkey = rsa.PublicKey(int(n), int(e))

        crypto = rsa.encrypt(message, pubkey)
        f = open('encrypto.txt', 'wb')
        f.write(crypto)
        f.close()

        self.text_first.setText(str(crypto))

    def decryptt(self):
        f = open('encrypto.txt', 'rb')
        message = f.read()
        f.close()

        self.text_first.setText(str(message))

        priv = open('privkey.txt', 'r')
        n = int(priv.readline())
        e = int(priv.readline())
        d = int(priv.readline())
        p = int(priv.readline())
        q = int(priv.readline())
        priv.close()

        privkey = rsa.PrivateKey(n, e, d, p, q)

        decrypto = rsa.decrypt(message, privkey)
        decrypto = decrypto.decode()

        de = open('decrypto.txt', 'w')
        de.write(str(decrypto))
        de.close()

        self.text_first.setText(decrypto)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
