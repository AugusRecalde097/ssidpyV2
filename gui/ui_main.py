from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        MainWindow.setWindowTitle("Redes WiFi - SSIDPY")
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

        # Input para el nombre de la red
        self.labelNetwork = QtWidgets.QLabel(self.centralwidget)
        self.labelNetwork.setObjectName("labelNetwork")
        self.labelNetwork.setText("Nombre")

        self.inputNetwork = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNetwork.setObjectName("inputNetwork")
        self.inputNetwork.setReadOnly(True)

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

        # Boton para generar QR
        self.buttonQR = QtWidgets.QPushButton(self.centralwidget)
        self.buttonQR.setObjectName("buttonQR")
        self.buttonQR.setText("Generar QR")
        
        # Boton para abrir galeria de QR generados
        self.buttonGallery = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGallery.setObjectName("buttonGallery")
        self.buttonGallery.setText("QR generados")

        # Layout de la ventana
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        # Agregamos los widgets de Titulo y Lista de redes al layout 
        self.layout.addWidget(self.labelTitle)
        self.layout.addWidget(self.listNetworks)
        self.layout.addStretch()
        # Agregamos los widgets de Input de nombre y contraseña al layout
        self.layout.addWidget(self.labelNetwork)
        self.layout.addWidget(self.inputNetwork)
        # self.layout.addSpacerItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding))
        self.layout.addWidget(self.labelPassword)
        self.layout.addWidget(self.inputPassword)
        self.layout.addWidget(self.labelError)
        self.layout.addStretch()
        # Agregamos los botones de Generar QR y Galeria de QR al layout
        self.layout.addWidget(self.buttonQR)
        self.layout.addWidget(self.buttonGallery)
        self.centralwidget.setLayout(self.layout)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
