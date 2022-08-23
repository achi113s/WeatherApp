from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUiType
import requests
import creds

def get_weather(zipcode: str) -> dict:
    APICALL = f'https://api.openweathermap.org/data/2.5/weather'
    # GET method at url, params is the set of extra variables for the api, returns a JSON object
    payload = {'zip': zipcode, 'appid': creds.APIKEY}
    resp = requests.get(APICALL, params=payload)

    if resp.status_code != 200:
        # something went wrong
        print(f'Something went wrong. Error code {resp.status_code}.')
    else:
        # success getting weather forecast
        return resp.json()

weather = get_weather('23322')
print(weather)

# # file from QtCreator
# qtcreator_file = '/Users/giorgio/Documents/mainwindow.ui'
# # import UI file, returns tuple of form class and Qt Base class
# Ui_MainWindow, QtBaseClass = loadUiType(qtcreator_file)


# class App(QMainWindow, Ui_MainWindow):
#     # constructor
#     def __init__(self):
#         # initialize main window class passing the App instance
#         QMainWindow.__init__(self)
#         Ui_MainWindow.__init__(self)
#         self.setupUi(self)

#         # since we named the button object in Qt Creator we can
#         # reference it here with self
#         self.getWeather_Button.clicked.connect(self.getWeather_Action)

#     def getWeather_Action(self):
#         zipcode = str(self.zipcode_Box.text()).strip()
#         weather = get_weather(zipcode)


# if __name__ == '__main__':
#     app = QApplication([])
#     window = App()
#     window.show()
#     app.exec_()
#     print("done")
