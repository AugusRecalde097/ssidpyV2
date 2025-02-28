from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        MainWindow.setWindowTitle("Redes WiFi - SSIDPy")
        MainWindow.setWindowIcon(QtGui.QIcon("favicon.ico"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Titulo de la ventana
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setText("Lista de redes WiFi")

        # Lista de redes WiFi
        self.listNetworks = QtWidgets.QComboBox(self.centralwidget)
        self.listNetworks.setObjectName("listNetworks")

        # Input para la contraseña de la red
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setObjectName("labelPassword")
        self.labelPassword.setText("Contraseña")

        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setObjectName("inputPassword")
        self.inputPassword.setReadOnly(True)

        # Mensaje de error
        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setObjectName("labelError")
        self.labelError.setVisible(False)

        # Imagen de QR
        self.labelQR = QtWidgets.QLabel(self.centralwidget)
        self.labelQR.setObjectName("labelQR")
        self.labelQR.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelQR.setStyleSheet("border: 1px solid black;")
        self.labelQR.setFixedSize(350, 350)
        
        # Boton para abrir galeria de QR generados
        self.buttonGallery = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGallery.setObjectName("buttonGallery")
        self.buttonGallery.setText("QR generados")

        # Layout de la ventana
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        # Agregamos los widgets de Titulo y Lista de redes al layout 
        self.layout.addWidget(self.labelTitle)
        self.layout.addWidget(self.listNetworks)
        self.layout.addWidget(self.labelPassword)
        self.layout.addWidget(self.inputPassword)
        self.layout.addWidget(self.labelError)
        self.layout.addWidget(self.labelQR)
        self.layout.setAlignment(self.labelQR, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addStretch()
        # Agregamos el boton de Galeria de QR al layout
        self.layout.addWidget(self.buttonGallery)
        self.centralwidget.setLayout(self.layout)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
