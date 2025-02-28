import os
import re
import subprocess
import webbrowser
import sys
import qrcode
from gui.ui_main import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.selected_profile = ""
        self.ssid_profile = ""
        self.pass_profile = ""
        self.directorio = os.path.join(os.environ['USERPROFILE'], "Documents", "Redes Guardadas")

        self.ui.buttonQR.clicked.connect(self.generate_qr_code)
        self.ui.listNetworks.currentIndexChanged.connect(lambda: self.search_profiles(self.ui.listNetworks.currentText()))
        self.ui.buttonGallery.clicked.connect(lambda: webbrowser.open(f"file://{self.directorio}"))

        self.crear_carpeta_qr()
        self.show_profiles_combo()
    
    # Crear la carpeta para guardar los códigos QR
    def crear_carpeta_qr(self):
        if not os.path.isdir(self.directorio):
            os.mkdir(self.directorio)

  	# Mostrar los perfiles de red disponibles    
    def show_profiles_combo(self):
        profiles_info = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode('latin-1')
        lista_perfiles = re.findall("Perfil de todos los usuarios     : (.*)\r", profiles_info)

        self.ui.listNetworks.clear()
        self.ui.listNetworks.setPlaceholderText("Selecciona una red")
        for perfil in lista_perfiles:
            self.ui.listNetworks.addItem(perfil)

    # Buscar la información de la red seleccionada
    def search_profiles(self, name):
        self.ui.labelError.setVisible(False)
        command = ["netsh", "wlan", "show", "profiles", name, "key=clear"]
        profile_info_pass = subprocess.run(command, capture_output=True).stdout.decode('latin-1')
        if 'No se encuentra el perfil' in profile_info_pass:
            self.setError('No se encuentra el perfil')
        else:
            password = re.search("Contenido de la clave  : (.*)\r", profile_info_pass)
            self.ui.inputPassword.setText(f"{password.group(1) if password else 'N/A'}")
            self.ui.inputNetwork.setText(f"{name}")
            self.ssid_profile = name
            self.pass_profile = password.group(1) if password else ''

    # Mensaje de error
    def setError(self, mensaje):
        self.ui.labelError.setText(mensaje)
        self.ui.labelError.setStyleSheet("color: red;")
        self.ui.labelError.setVisible(True)
    
    # Generar código QR de la red seleccionada
    def generate_qr_code(self):
        ssid = self.ssid_profile
        password = self.pass_profile

        if ssid:
            text = f"WIFI:T:WPA;S:{ssid};P:{password};;"
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(text)

            file_name = f"{ssid.replace(' ', '_')}.png"
            img_path = os.path.join(self.directorio, file_name)
            img = qr.make_image()
            img.save(img_path)
            img.show()
        else:
            self.setError('Debe seleccionar una red antes de generar el QR')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
