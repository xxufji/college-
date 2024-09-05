from PyQt5 import QtWidgets, QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from menu import Ui_MainWindow
from levels import Ui_LevelsWindow
from settings import Ui_SettingsWindow
from rules import Ui_RulesWindow
from lvl_1 import Ui_Level1Window
from lvl_2 import Ui_Level2Window
from lvl_3 import Ui_Level3Window
from lvl_4 import Ui_Level4Window
from lvl_5 import Ui_Level5Window
from lvl_6 import Ui_Level6Window
from lvl_7 import Ui_Level7Window
from lvl_8 import Ui_Level8Window

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.menu = Ui_MainWindow()
        self.menu.setupUi(self)

        self.menu.pushButton.clicked.connect(self.close_application)
        self.menu.pushButton_2.clicked.connect(self.open_settings)
        self.menu.pushButton_3.clicked.connect(self.open_levels_window)
        self.menu.pushButton_4.clicked.connect(self.open_rules)

    def close_application(self):
        sys.exit()

    def open_levels_window(self):
        self.levels_window = LevelsWindow()
        self.levels_window.show()
        self.close()

    def open_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()
        self.close()

    def open_rules(self):
        self.rules_window = RulesWindow()
        self.rules_window.show()
        self.close()

class LevelsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LevelsWindow, self).__init__()
        self.levels = Ui_LevelsWindow()
        self.levels.setupUi(self)

        self.levels.pushButton.clicked.connect(self.go_home)
        self.levels.pushButton_2.clicked.connect(self.go_lvl1)
        self.levels.pushButton_3.clicked.connect(self.go_lvl2)
        self.levels.pushButton_4.clicked.connect(self.go_lvl3)
        self.levels.pushButton_5.clicked.connect(self.go_lvl4)
        self.levels.pushButton_6.clicked.connect(self.go_lvl5)
        self.levels.pushButton_7.clicked.connect(self.go_lvl6)
        self.levels.pushButton_8.clicked.connect(self.go_lvl7)
        self.levels.pushButton_9.clicked.connect(self.go_lvl8)

    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_lvl1(self):
        self.main_window = Level1Window()
        self.main_window.show()
        self.close()

    def go_lvl2(self):
        self.main_window = Level2Window()
        self.main_window.show()
        self.close()

    def go_lvl3(self):
        self.main_window = Level3Window()
        self.main_window.show()
        self.close()

    def go_lvl4(self):
        self.main_window = Level4Window()
        self.main_window.show()
        self.close()

    def go_lvl5(self):
        self.main_window = Level5Window()
        self.main_window.show()
        self.close()

    def go_lvl6(self):
        self.main_window = Level6Window()
        self.main_window.show()
        self.close()

    def go_lvl7(self):
        self.main_window = Level7Window()
        self.main_window.show()
        self.close()

    def go_lvl8(self):
        self.main_window = Level8Window()
        self.main_window.show()
        self.close()

class Level1Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Level1Window, self).__init__()
        self.lvl_1 = Ui_Level1Window()
        self.lvl_1.setupUi(self)

        self.lvl_1.pushButton.clicked.connect(self.go_home)
        self.lvl_1.pushButton_2.clicked.connect(self.go_back)
        self.lvl_1.pushButton_3.clicked.connect(self.restart)
        self.lvl_1.circle_1.clicked.connect(self.Connect_Points_1)
        self.lvl_1.circle_3.clicked.connect(self.Connect_Points_3)
        self.lvl_1.circle_4.clicked.connect(self.Connect_Points_4)
        self.stopper = True

    def Connect_Points_1(self):
        if not self.stopper:
            return
        else:
            self.lvl_1.circle_1.setEnabled(False)
            if not self.lvl_1.circle_3.isEnabled():
                self.lvl_1.label_7.setStyleSheet("background-image: url(:/newPrefix/photo/Line 4.2.png);")
                self.lvl_1.label_6.setStyleSheet("background-image: url(:/newPrefix/photo/Line 3.2.png);")
            self.stopper = False

    def Connect_Points_3(self):
        self.lvl_1.circle_3.setEnabled(False)
        self.lvl_1.circle_2.setEnabled(False)
        self.stopper = True
        if not self.lvl_1.circle_1.isEnabled():
            self.lvl_1.label_7.setStyleSheet("background-image: url(:/newPrefix/photo/Line 4.2.png);")
            self.lvl_1.label_6.setStyleSheet("background-image: url(:/newPrefix/photo/Line 3.2.png);")
        if not self.lvl_1.circle_4.isEnabled():
            self.lvl_1.label_3.setStyleSheet("background-image: url(:/newPrefix/photo/Line 1.2.png);")
            self.lvl_1.label_5.setStyleSheet("background-image: url(:/newPrefix/photo/Line 2.2.png);")


    def Connect_Points_4(self):
        if not self.stopper:
            return
        else:
            self.lvl_1.circle_4.setEnabled(False)
            if not self.lvl_1.circle_3.isEnabled():
                self.lvl_1.label_3.setStyleSheet("background-image: url(:/newPrefix/photo/Line 1.2.png);")
                self.lvl_1.label_5.setStyleSheet("background-image: url(:/newPrefix/photo/Line 2.2.png);")
            self.stopper = False


    def restart(self):
        self.stopper = True
        self.lvl_1.circle_1.setEnabled(True)
        self.lvl_1.circle_2.setEnabled(True)
        self.lvl_1.circle_3.setEnabled(True)
        self.lvl_1.circle_4.setEnabled(True)
        self.lvl_1.label_7.setStyleSheet("background-image: url(:/newPrefix/photo/Line 4.png);")
        self.lvl_1.label_6.setStyleSheet("background-image: url(:/newPrefix/photo/Line 3.png);")
        self.lvl_1.label_3.setStyleSheet("background-image: url(:/newPrefix/photo/Line 1.png);")
        self.lvl_1.label_5.setStyleSheet("background-image: url(:/newPrefix/photo/Line 2.png);")


    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_back(self):
        self.main_window = LevelsWindow()
        self.main_window.show()
        self.close()

class Level2Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Level2Window, self).__init__()
        self.lvl_2 = Ui_Level2Window()
        self.lvl_2.setupUi(self)

        self.lvl_2.pushButton.clicked.connect(self.go_home)
        self.lvl_2.pushButton_2.clicked.connect(self.go_back)
        self.lvl_2.pushButton_3.clicked.connect(self.restart)
        self.lvl_2.circle_1.clicked.connect(self.Connect_Points_1)
        self.lvl_2.circle_2.clicked.connect(self.Connect_Points_2)
        self.lvl_2.circle_3.clicked.connect(self.Connect_Points_3)
        self.lvl_2.circle_4.clicked.connect(self.Connect_Points_4)
        self.lvl_2.circle_5.clicked.connect(self.Connect_Points_5)
        self.lvl_2.circle_6.clicked.connect(self.Connect_Points_6)
        self.stopper = True


    def Connect_Points_1(self):
        if not self.stopper:
            return
        else:
            self.lvl_2.circle_1.setEnabled(False)
            if not self.lvl_2.circle_2.isEnabled():
                self.lvl_2.label_4.setStyleSheet("background-image: url(:/newPrefix/photo/Line2 1.2png);")
                self.lvl_2.label_5.setStyleSheet("background-image: url(:/newPrefix/photo/Line2 2.2png);")
            self.stopper = False

    def Connect_Points_2(self):
        self.lvl_2.circle_2.setEnabled(False)
        self.lvl_2.circle_10.setEnabled(False)
        self.stopper = True

    def Connect_Points_3(self):
        self.lvl_2.circle_3.setEnabled(False)
        self.lvl_2.circle_9.setEnabled(False)

    def Connect_Points_4(self):
        self.lvl_2.circle_4.setEnabled(False)
        self.lvl_2.circle_8.setEnabled(False)

    def Connect_Points_5(self):
        self.lvl_2.circle_5.setEnabled(False)
        self.lvl_2.circle_7.setEnabled(False)

    def Connect_Points_6(self):
        self.lvl_2.circle_6.setEnabled(False)

    def restart(self):
        self.stopper = True
        self.lvl_2.circle_1.setEnabled(True)
        self.lvl_2.circle_2.setEnabled(True)
        self.lvl_2.circle_3.setEnabled(True)
        self.lvl_2.circle_4.setEnabled(True)
        self.lvl_2.circle_5.setEnabled(True)
        self.lvl_2.circle_6.setEnabled(True)
        self.lvl_2.circle_7.setEnabled(True)
        self.lvl_2.circle_8.setEnabled(True)
        self.lvl_2.circle_9.setEnabled(True)
        self.lvl_2.circle_10.setEnabled(True)
        self.lvl_2.label_4.setStyleSheet("background-image: url(:/newPrefix/photo/Line2 1.png);")
        self.lvl_2.label_5.setStyleSheet("background-image: url(:/newPrefix/photo/Line2 2.png);")

    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_back(self):
        self.main_window = LevelsWindow()
        self.main_window.show()
        self.close()

class Level3Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Level3Window, self).__init__()
        self.lvl_3 = Ui_Level3Window()
        self.lvl_3.setupUi(self)

        self.lvl_3.pushButton.clicked.connect(self.go_home)
        self.lvl_3.pushButton_2.clicked.connect(self.go_back)
        self.lvl_3.pushButton_3.clicked.connect(self.restart)
        self.lvl_3.circle_1.clicked.connect(self.Connect_Points_1)
        self.lvl_3.circle_3.clicked.connect(self.Connect_Points_3)
        self.lvl_3.circle_4.clicked.connect(self.Connect_Points_4)
        self.lvl_3.circle_6.clicked.connect(self.Connect_Points_6)
        self.lvl_3.circle_7.clicked.connect(self.Connect_Points_7)


    def Connect_Points_1(self):
        self.lvl_3.circle_1.setEnabled(False)
        self.lvl_3.circle_2.setEnabled(False)
    def Connect_Points_3(self):
        self.lvl_3.circle_3.setEnabled(False)

    def Connect_Points_4(self):
        self.lvl_3.circle_4.setEnabled(False)
        self.lvl_3.circle_5.setEnabled(False)

    def Connect_Points_6(self):
        self.lvl_3.circle_6.setEnabled(False)

    def Connect_Points_7(self):
        self.lvl_3.circle_7.setEnabled(False)
        self.lvl_3.circle_8.setEnabled(False)

    def restart(self):
        self.lvl_3.circle_1.setEnabled(True)
        self.lvl_3.circle_2.setEnabled(True)
        self.lvl_3.circle_3.setEnabled(True)
        self.lvl_3.circle_4.setEnabled(True)
        self.lvl_3.circle_5.setEnabled(True)
        self.lvl_3.circle_6.setEnabled(True)
        self.lvl_3.circle_7.setEnabled(True)
        self.lvl_3.circle_8.setEnabled(True)

    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_back(self):
        self.main_window = LevelsWindow()
        self.main_window.show()
        self.close()

class Level4Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Level4Window, self).__init__()
        self.lvl_4 = Ui_Level4Window()
        self.lvl_4.setupUi(self)

        self.lvl_4.pushButton.clicked.connect(self.go_home)
        self.lvl_4.pushButton_2.clicked.connect(self.go_back)
        self.lvl_4.pushButton_3.clicked.connect(self.restart)
        self.lvl_4.circle_1.clicked.connect(self.Connect_Points_1)
        self.lvl_4.circle_2.clicked.connect(self.Connect_Points_2)
        self.lvl_4.circle_3.clicked.connect(self.Connect_Points_3)
        self.lvl_4.circle_8.clicked.connect(self.Connect_Points_8)
        self.lvl_4.circle_9.clicked.connect(self.Connect_Points_9)

    def Connect_Points_1(self):
        self.lvl_4.circle_1.setEnabled(False)
        self.lvl_4.circle_5.setEnabled(False)

    def Connect_Points_2(self):
        self.lvl_4.circle_2.setEnabled(False)
        self.lvl_4.circle_4.setEnabled(False)

    def Connect_Points_3(self):
        self.lvl_4.circle_3.setEnabled(False)

    def Connect_Points_8(self):
        self.lvl_4.circle_7.setEnabled(False)
        self.lvl_4.circle_8.setEnabled(False)

    def Connect_Points_9(self):
        self.lvl_4.circle_6.setEnabled(False)
        self.lvl_4.circle_9.setEnabled(False)

    def restart(self):
        self.lvl_4.circle_1.setEnabled(True)
        self.lvl_4.circle_2.setEnabled(True)
        self.lvl_4.circle_3.setEnabled(True)
        self.lvl_4.circle_4.setEnabled(True)
        self.lvl_4.circle_5.setEnabled(True)
        self.lvl_4.circle_6.setEnabled(True)
        self.lvl_4.circle_7.setEnabled(True)
        self.lvl_4.circle_8.setEnabled(True)
        self.lvl_4.circle_9.setEnabled(True)


    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_back(self):
        self.main_window = LevelsWindow()
        self.main_window.show()
        self.close()

class Level5Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Level5Window, self).__init__()
        self.lvl_5 = Ui_Level5Window()
        self.lvl_5.setupUi(self)

        self.lvl_5.pushButton.clicked.connect(self.go_home)
        self.lvl_5.pushButton_2.clicked.connect(self.go_back)
        self.lvl_5.pushButton_3.clicked.connect(self.restart)
        self.lvl_5.circle_1.clicked.connect(self.Connect_Points_1)
        self.lvl_5.circle_2.clicked.connect(self.Connect_Points_2)
        self.lvl_5.circle_3.clicked.connect(self.Connect_Points_3)
        self.lvl_5.circle_4.clicked.connect(self.Connect_Points_4)
        self.lvl_5.circle_5.clicked.connect(self.Connect_Points_5)
        self.lvl_5.circle_6.clicked.connect(self.Connect_Points_6)


    def Connect_Points_1(self):
        self.lvl_5.circle_1.setEnabled(False)
        self.lvl_5.circle_10.setEnabled(False)

    def Connect_Points_2(self):
        self.lvl_5.circle_2.setEnabled(False)
        self.lvl_5.circle_9.setEnabled(False)

    def Connect_Points_3(self):
        self.lvl_5.circle_3.setEnabled(False)

    def Connect_Points_4(self):
        self.lvl_5.circle_4.setEnabled(False)
        self.lvl_5.circle_8.setEnabled(False)

    def Connect_Points_5(self):
        self.lvl_5.circle_5.setEnabled(False)
        self.lvl_5.circle_7.setEnabled(False)

    def Connect_Points_6(self):
        self.lvl_5.circle_6.setEnabled(False)

    def restart(self):
        self.lvl_5.circle_1.setEnabled(True)
        self.lvl_5.circle_2.setEnabled(True)
        self.lvl_5.circle_3.setEnabled(True)
        self.lvl_5.circle_4.setEnabled(True)
        self.lvl_5.circle_5.setEnabled(True)
        self.lvl_5.circle_6.setEnabled(True)
        self.lvl_5.circle_7.setEnabled(True)
        self.lvl_5.circle_8.setEnabled(True)
        self.lvl_5.circle_9.setEnabled(True)
        self.lvl_5.circle_10.setEnabled(True)


    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_back(self):
        self.main_window = LevelsWindow()
        self.main_window.show()
        self.close()

class Level6Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Level6Window, self).__init__()
        self.lvl_6 = Ui_Level6Window()
        self.lvl_6.setupUi(self)

        self.lvl_6.pushButton.clicked.connect(self.go_home)
        self.lvl_6.pushButton_2.clicked.connect(self.go_back)
        self.lvl_6.pushButton_3.clicked.connect(self.restart)
        self.lvl_6.circle_1.clicked.connect(self.Connect_Points_1)
        self.lvl_6.circle_2.clicked.connect(self.Connect_Points_2)
        self.lvl_6.circle_3.clicked.connect(self.Connect_Points_3)
        self.lvl_6.circle_4.clicked.connect(self.Connect_Points_4)
        self.lvl_6.circle_5.clicked.connect(self.Connect_Points_5)
        self.lvl_6.circle_6.clicked.connect(self.Connect_Points_6)

    def Connect_Points_1(self):
        self.lvl_6.circle_1.setEnabled(False)

    def Connect_Points_2(self):
        self.lvl_6.circle_2.setEnabled(False)
        self.lvl_6.circle_9.setEnabled(False)

    def Connect_Points_3(self):
        self.lvl_6.circle_3.setEnabled(False)
        self.lvl_6.circle_8.setEnabled(False)

    def Connect_Points_4(self):
        self.lvl_6.circle_4.setEnabled(False)
        self.lvl_6.circle_7.setEnabled(False)

    def Connect_Points_5(self):
        self.lvl_6.circle_5.setEnabled(False)

    def Connect_Points_6(self):
        self.lvl_6.circle_6.setEnabled(False)

    def restart(self):
        self.lvl_6.circle_1.setEnabled(True)
        self.lvl_6.circle_2.setEnabled(True)
        self.lvl_6.circle_3.setEnabled(True)
        self.lvl_6.circle_4.setEnabled(True)
        self.lvl_6.circle_5.setEnabled(True)
        self.lvl_6.circle_6.setEnabled(True)
        self.lvl_6.circle_7.setEnabled(True)
        self.lvl_6.circle_8.setEnabled(True)
        self.lvl_6.circle_9.setEnabled(True)

    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_back(self):
        self.main_window = LevelsWindow()
        self.main_window.show()
        self.close()

class Level7Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Level7Window, self).__init__()
        self.lvl_7 = Ui_Level7Window()
        self.lvl_7.setupUi(self)

        self.lvl_7.pushButton.clicked.connect(self.go_home)
        self.lvl_7.pushButton_2.clicked.connect(self.go_back)
        self.lvl_7.restart_btn.clicked.connect(self.restart)
        self.lvl_7.circle_1.clicked.connect(self.Connect_Points_1)
        self.lvl_7.circle_2.clicked.connect(self.Connect_Points_2)
        self.lvl_7.circle_3.clicked.connect(self.Connect_Points_3)
        self.lvl_7.circle_4.clicked.connect(self.Connect_Points_4)
        self.lvl_7.circle_5.clicked.connect(self.Connect_Points_5)

    def Connect_Points_1(self):
        self.lvl_7.circle_1.setEnabled(False)

    def Connect_Points_2(self):
        self.lvl_7.circle_2.setEnabled(False)
        self.lvl_7.circle_7.setEnabled(False)

    def Connect_Points_3(self):
        self.lvl_7.circle_3.setEnabled(False)
        self.lvl_7.circle_8.setEnabled(False)

    def Connect_Points_4(self):
        self.lvl_7.circle_4.setEnabled(False)
        self.lvl_7.circle_6.setEnabled(False)

    def Connect_Points_5(self):
        self.lvl_7.circle_5.setEnabled(False)

    def restart(self):
        self.lvl_7.circle_1.setEnabled(True)
        self.lvl_7.circle_2.setEnabled(True)
        self.lvl_7.circle_3.setEnabled(True)
        self.lvl_7.circle_4.setEnabled(True)
        self.lvl_7.circle_5.setEnabled(True)
        self.lvl_7.circle_6.setEnabled(True)
        self.lvl_7.circle_7.setEnabled(True)
        self.lvl_7.circle_8.setEnabled(True)

    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_back(self):
        self.main_window = LevelsWindow()
        self.main_window.show()
        self.close()

class Level8Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Level8Window, self).__init__()
        self.lvl_8 = Ui_Level8Window()
        self.lvl_8.setupUi(self)

        self.lvl_8.pushButton.clicked.connect(self.go_home)
        self.lvl_8.pushButton_2.clicked.connect(self.go_back)
        self.lvl_8.pushButton_3.clicked.connect(self.restart)
        self.lvl_8.circle_1.clicked.connect(self.Connect_Points_1)
        self.lvl_8.circle_2.clicked.connect(self.Connect_Points_2)
        self.lvl_8.circle_3.clicked.connect(self.Connect_Points_3)
        self.lvl_8.circle_4.clicked.connect(self.Connect_Points_4)
        self.lvl_8.circle_5.clicked.connect(self.Connect_Points_5)
        self.lvl_8.circle_6.clicked.connect(self.Connect_Points_6)
        self.lvl_8.circle_7.clicked.connect(self.Connect_Points_7)
        self.lvl_8.circle_8.clicked.connect(self.Connect_Points_8)

    def Connect_Points_1(self):
        self.lvl_8.circle_1.setEnabled(False)
        self.lvl_8.circle_13.setEnabled(False)

    def Connect_Points_2(self):
        self.lvl_8.circle_2.setEnabled(False)
        self.lvl_8.circle_14.setEnabled(False)

    def Connect_Points_3(self):
        self.lvl_8.circle_3.setEnabled(False)
        self.lvl_8.circle_15.setEnabled(False)

    def Connect_Points_4(self):
        self.lvl_8.circle_4.setEnabled(False)
        self.lvl_8.circle_12.setEnabled(False)

    def Connect_Points_5(self):
        self.lvl_8.circle_5.setEnabled(False)
        self.lvl_8.circle_11.setEnabled(False)

    def Connect_Points_6(self):
        self.lvl_8.circle_6.setEnabled(False)
        self.lvl_8.circle_10.setEnabled(False)

    def Connect_Points_7(self):
        self.lvl_8.circle_7.setEnabled(False)
        self.lvl_8.circle_9.setEnabled(False)

    def Connect_Points_8(self):
        self.lvl_8.circle_8.setEnabled(False)

    def restart(self):
        self.lvl_8.circle_1.setEnabled(True)
        self.lvl_8.circle_2.setEnabled(True)
        self.lvl_8.circle_3.setEnabled(True)
        self.lvl_8.circle_4.setEnabled(True)
        self.lvl_8.circle_5.setEnabled(True)
        self.lvl_8.circle_6.setEnabled(True)
        self.lvl_8.circle_7.setEnabled(True)
        self.lvl_8.circle_8.setEnabled(True)
        self.lvl_8.circle_9.setEnabled(True)
        self.lvl_8.circle_10.setEnabled(True)
        self.lvl_8.circle_11.setEnabled(True)
        self.lvl_8.circle_12.setEnabled(True)
        self.lvl_8.circle_13.setEnabled(True)
        self.lvl_8.circle_14.setEnabled(True)
        self.lvl_8.circle_15.setEnabled(True)

    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def go_back(self):
        self.main_window = LevelsWindow()
        self.main_window.show()
        self.close()


class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.settings = Ui_SettingsWindow()
        self.settings.setupUi(self)

        self.settings.pushButton.clicked.connect(self.go_home)
        self.settings.pushButton_2.clicked.connect(self.sound_on)
        self.settings.pushButton_3.clicked.connect(self.sound_off)

    def go_home(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def sound_on(self):
        media_player.play()

    def sound_off(self):
        media_player.stop()

class RulesWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(RulesWindow, self).__init__()
        self.rules = Ui_RulesWindow()
        self.rules.setupUi(self)

        self.rules.pushButton.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    media_player = QMediaPlayer()
    background_music = QMediaPlaylist()
    background_music.addMedia(QMediaContent(QtCore.QUrl.fromLocalFile("the sound.mp3")))
    background_music.setPlaybackMode(QMediaPlaylist.Loop)
    media_player.setPlaylist(background_music)
    media_player.play()
    window.show()
    sys.exit(app.exec())

