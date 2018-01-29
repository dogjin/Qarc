# -*- coding: utf-8 -*-
import os
from functools import partial
import time
import imp

"""
This test stylesheet ui script is based on a blog post https://dftalk.jp/?p=20768""
"""
try:
    imp.find_module('PySide2')
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *

except ImportError:
    from PySide.QtGui import *
    from PySide.QtCore import *


LOGO_IMAGE = r"C:/Users/takanori/Desktop/widget_gallery/image/logo.png"



class MyDialog(QDialog):


    def __init__(self, parent = None, f = 0):
        super(MyDialog, self).__init__(parent, f)
        #-----------------------------------------------------------------------
        # Layout
        #-----------------------------------------------------------------------
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        #-----------------------------------------------------------------------
        # Image
        #-----------------------------------------------------------------------
        # imageWidget = QLabel()
        # # imageWidget.setPixmap(QPixmap(LOGO_IMAGE))
        # mainLayout.addWidget(imageWidget)
        #-----------------------------------------------------------------------
        # Description
        #-----------------------------------------------------------------------
        description = QLabel("This is coustom dialog.")
        mainLayout.addWidget(description)
        #-----------------------------------------------------------------------
        # Text input
        #-----------------------------------------------------------------------
        self._inputWidget = QLineEdit()
        mainLayout.addWidget(self._inputWidget)
        #-----------------------------------------------------------------------
        # Buttons
        #-----------------------------------------------------------------------
        buttonArea = QHBoxLayout()
        mainLayout.addLayout(buttonArea)
        buttonArea.addStretch()
        okBtn = QPushButton("OK")
        buttonArea.addWidget(okBtn)
        okBtn.clicked.connect(self.accept)
        cancelBtn = QPushButton("Cancel")
        buttonArea.addWidget(cancelBtn)
        cancelBtn.clicked.connect(self.reject)


    def getInputText(self):
        return self._inputWidget.text()


class TestUI(QMainWindow):


    def __init__(self, parent = None):
        super(TestUI, self).__init__(parent)
        self.setObjectName("qarc_theme_test")
        self.setWindowTitle("Qarc Theme Test")
        self._initUI()
        self.errorDialog = QErrorMessage(self) # QErrorMessageインスタンスの保持


    def _initUI(self):
        wrapper = QWidget()
        self.setCentralWidget(wrapper)

        mainLayout = QVBoxLayout()
        wrapper.setLayout(mainLayout)

        #-----------------------------------------------------------------------
        # First row
        #-----------------------------------------------------------------------
        firstHolizontalArea = QHBoxLayout()
        firstHolizontalArea.setSpacing(20)
        mainLayout.addLayout(firstHolizontalArea)

        labelArea = QVBoxLayout()
        firstHolizontalArea.addLayout(labelArea)

        labelWidget = QLabel("Text is shown like this.")
        labelArea.addWidget(labelWidget)

        # imageWidget = QLabel()
        # imageWidget.setPixmap(QPixmap(LOGO_IMAGE))
        # labelArea.addWidget(imageWidget)
        # labelArea.addStretch()

        textArea = QTextEdit()
        textArea.setPlainText("Text are\ncan be set\nmultiple lines and HTML.")
        firstHolizontalArea.addWidget(textArea)

        mainLayout.addWidget(self._makeHorizontalLine())

        #-----------------------------------------------------------------------
        # Second row
        #-----------------------------------------------------------------------
        secondHolizontalArea = QHBoxLayout()
        secondHolizontalArea.setSpacing(20)
        mainLayout.addLayout(secondHolizontalArea)

        lineEdit = QLineEdit()
        lineEdit.setMaximumWidth(200)
        lineEdit.setText("This widget is useful for inputting text")
        secondHolizontalArea.addWidget(lineEdit)

        comboBox = QComboBox()
        comboBox.addItems(["This", "is", "combobox", "it's", "useful"])
        comboBox.setEditable(True)
        comboBox.setInsertPolicy(QComboBox.NoInsert)
        comboBox.completer().setCompletionMode(QCompleter.PopupCompletion)
        secondHolizontalArea.addWidget(comboBox)

        spinBox = QSpinBox()
        spinBox.setMinimum(0)
        spinBox.setMaximum(10)
        spinBox.setSuffix("min")
        secondHolizontalArea.addWidget(spinBox)

        mainLayout.addWidget(self._makeHorizontalLine())

        #-----------------------------------------------------------------------
        # Third row
        #-----------------------------------------------------------------------
        thirdHorizontalArea = QHBoxLayout()
        thirdHorizontalArea.setSpacing(20)
        mainLayout.addLayout(thirdHorizontalArea)

        checkBox = QCheckBox("Check box")
        thirdHorizontalArea.addWidget(checkBox)
        checkBox.setChecked(True)

        radioArea = QVBoxLayout()
        thirdHorizontalArea.addLayout(radioArea)

        radioGroup = QButtonGroup(self)
        radioBtn1 = QRadioButton("Option 1")
        radioArea.addWidget(radioBtn1)
        radioGroup.addButton(radioBtn1)
        radioBtn2 = QRadioButton("Option 2")
        radioArea.addWidget(radioBtn2)
        radioGroup.addButton(radioBtn2)
        radioBtn3 = QRadioButton("Option 3")
        radioArea.addWidget(radioBtn3)
        radioGroup.addButton(radioBtn3)
        radioBtn1.setChecked(True)

        mainLayout.addWidget(self._makeHorizontalLine())

        #-----------------------------------------------------------------------
        # Fourth row
        #-----------------------------------------------------------------------
        fourthHorizontalArea = QHBoxLayout()
        fourthHorizontalArea.setSpacing(20)
        mainLayout.addLayout(fourthHorizontalArea)

        calender = QCalendarWidget()
        fourthHorizontalArea.addWidget(calender)
        calender.setMaximumWidth(300)

        # lcdNumber = QLCDNumber()
        # fourthHorizontalArea.addWidget(lcdNumber)
        # lcdNumber.display(1234)

        sliderArea = QVBoxLayout()
        fourthHorizontalArea.addLayout(sliderArea)

        sliderDisplay = QLabel("0")
        sliderArea.addWidget(sliderDisplay)
        slider = QSlider(Qt.Horizontal)
        sliderArea.addWidget(slider)
        slider.setRange(0, 100)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickInterval(10)
        slider.valueChanged.connect(lambda val: sliderDisplay.setText(str(val)))
        slider.setValue(0)

        # dialDisplay = QLabel("0")
        # sliderArea.addWidget(dialDisplay)
        # dial = QDial()
        # sliderArea.addWidget(dial)
        # dial.setRange(0, 100)
        # dial.setSingleStep(5)
        # dial.setPageStep(10)
        # dial.setNotchesVisible(True)
        # dial.setWrapping(True)
        # dial.setNotchTarget(5)
        # dial.valueChanged.connect(lambda val: dialDisplay.setText(str(val)))
        # dial.setValue(0)

        mainLayout.addWidget(self._makeHorizontalLine())

        #-----------------------------------------------------------------------
        # fifth row
        #-----------------------------------------------------------------------
        fifthHorizontalArea = QHBoxLayout()
        fifthHorizontalArea.setSpacing(20)
        mainLayout.addLayout(fifthHorizontalArea)

        fifthHorizontalArea.addWidget(self._makeListWidget())
        fifthHorizontalArea.addWidget(self._makeTableWidget())
        fifthHorizontalArea.addWidget(self._makeTreeWidget())

        mainLayout.addWidget(self._makeHorizontalLine())

        #-----------------------------------------------------------------------
        # sixth row
        #-----------------------------------------------------------------------
        sixthHorizontalArea = QHBoxLayout()
        sixthHorizontalArea.setSpacing(20)
        mainLayout.addLayout(sixthHorizontalArea)

        msgBoxBtn = QPushButton("Message Dialog")
        sixthHorizontalArea.addWidget(msgBoxBtn)
        msgBoxBtn.clicked.connect(partial(QMessageBox().information, self, "Message", "This is normal information message."))
        msgBoxBtn.setEnabled(False)

        colorDialogBtn = QPushButton("Color Dialog")
        sixthHorizontalArea.addWidget(colorDialogBtn)
        colorDialogBtn.clicked.connect(self._showColorDialog)

        progressDialogBtn = QPushButton("Progress Dialog")
        sixthHorizontalArea.addWidget(progressDialogBtn)
        progressDialogBtn.clicked.connect(self._showProgressDialog)

        fileDialogBtn = QPushButton("File Dialog")
        sixthHorizontalArea.addWidget(fileDialogBtn)
        fileDialogBtn.clicked.connect(partial(QFileDialog.getOpenFileName, self, "File Select", options = QFileDialog.DontUseNativeDialog))

        #-----------------------------------------------------------------------
        # seventh row
        #-----------------------------------------------------------------------
        seventhHorizontalArea = QHBoxLayout()
        seventhHorizontalArea.setSpacing(20)
        mainLayout.addLayout(seventhHorizontalArea)

        errorMsgBtn = QPushButton("Error Dialog")
        seventhHorizontalArea.addWidget(errorMsgBtn)
        errorMsgBtn.clicked.connect(self._showErrorDialog)

        inputDialogTextBtn = QPushButton("Input (text)")
        seventhHorizontalArea.addWidget(inputDialogTextBtn)
        inputDialogTextBtn.clicked.connect(self._showInputTextDialog)

        inputDialogComboBtn = QPushButton("Input (combo)")
        seventhHorizontalArea.addWidget(inputDialogComboBtn)
        inputDialogComboBtn.clicked.connect(self._showInputComboDialog)

        dialogBtn = QPushButton("Custom Dialog")
        seventhHorizontalArea.addWidget(dialogBtn)
        dialogBtn.clicked.connect(self._showCustomDialog)

        #-----------------------------------------------------------------------
        # dock widget
        #-----------------------------------------------------------------------
        dockWidget = QDockWidget("Dock Window", self)
        dockWrapper = QWidget()
        dockWidget.setWidget(dockWrapper)
        dockWidget.setAllowedAreas(Qt.RightDockWidgetArea | Qt.BottomDockWidgetArea)
        dockLayout = QVBoxLayout()
        dockWrapper.setLayout(dockLayout)
        dockDescription = QLabel("This is dock widget contents.")
        dockLayout.addWidget(dockDescription)
        dockButton = QPushButton("OK")
        dockLayout.addWidget(dockButton)
        self.addDockWidget(Qt.BottomDockWidgetArea, dockWidget)


    def _makeHorizontalLine(self):
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Sunken)
        return hline


    def _makeListWidget(self):
        """
        Method to Create QListWidget.
        """
        listWidget = QListWidget()
        listWidget.setMaximumWidth(100)
        listWidget.addItems(["this", "is", "list", "widget"])
        return listWidget


    def _makeTableWidget(self):
        """
        Method to create QTableWidget.
        """
        tableWidget = QTableWidget()
        headerLabels = ["Name", "Age", "Sex"]
        tableWidget.setColumnCount(len(headerLabels))
        tableWidget.setHorizontalHeaderLabels(headerLabels)
        tableWidget.verticalHeader().setVisible(False)

        try:
            tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        except:
            tableWidget.horizontalHeader().setResizeMode(QHeaderView.Interactive)

        tableWidget.setAlternatingRowColors(True)
        tableWidget.horizontalHeader().setStretchLastSection(True)
        dataList = [
            ["Taro",    "25", "Male"],
            ["Hanako",  "30", "Female"],
            ["Ichiro",  "50", "Male"],
            ["Jiro",    "40", "Male"]
        ]
        tableWidget.setRowCount(len(dataList))

        for row, colData in enumerate(dataList):

            for col, value in enumerate(colData):
                item = QTableWidgetItem(value)
                tableWidget.setItem(row, col, item)

        return tableWidget


    def _makeTreeWidget(self):
        """
        Method to create QTreeWidget.
        """
        treeWidget = QTreeWidget()
        headerLabels = ["Name", "Age"]
        treeWidget.setColumnCount(len(headerLabels))
        treeWidget.setHeaderLabels(headerLabels)
        treeWidget.setAlternatingRowColors(True)
        treeData = {
            "Male":[
                {"name":"Taro",     "age":"25"},
                {"name":"Ichiro",   "age":"50"},
                {"name":"Jiro",     "age":"40"}
            ],
            "Female":[
                {"name":"Hanako",   "age":"30"}
            ]
        }

        for sex, profiles in treeData.iteritems():
            topItem = QTreeWidgetItem([sex])
            treeWidget.addTopLevelItem(topItem)

            for profile in profiles:
                childItem = QTreeWidgetItem(topItem, [profile.get("name"), profile.get("age")])

        treeWidget.expandAll()
        return treeWidget


    def _showColorDialog(self):
        """
        Method to create QColorDialog.
        """
        colorDialog = QColorDialog(self)
        response = colorDialog.exec_()

        if response != QDialog.Accepted:
            return

        chosen = colorDialog.currentColor()
        print("Selected color >> (%d, %d, %d)" % (chosen.red(), chosen.green(), chosen.blue()))


    def _showProgressDialog(self):
        """
        Method to create QProgressDialog.
        """
        max = 100
        progressDialog = QProgressDialog("Progress...", "Cancel", 0, max, self)
        progressDialog.setWindowTitle("Progress Dialog")

        for count in range(max+1):
            qApp.processEvents()

            if progressDialog.wasCanceled():
                break

            progressDialog.setValue(count)
            progressDialog.setLabelText("Progress... %d %%" % count)
            time.sleep(0.1)


    def _showErrorDialog(self):
        """
        Method to create QErrorMessage.
        """
        self.errorDialog.showMessage("This is error message.")


    def _showInputTextDialog(self):
        """
        Method to create a displaying slot for QInputDialog(Input strings).
        """
        response = QInputDialog.getText(self,
                                    "Input Text",
                                    "Input text here.")
        print(response)


    def _showInputComboDialog(self):
        """
        Method to create a displaying slot for QInputDialog(Select item)
        """
        response = QInputDialog.getItem(self,
                                    "Select Item",
                                    "Select item from the combo box.",
                                    ["item1", "item2", "item3", "item4"],
                                    editable=False)
        print(response)


    def _showCustomDialog(self):
        """
        Method to create a displaying slot for MyDialog.
        """
        dialog = MyDialog()
        response = dialog.exec_()

        if response == QDialog.Accepted:
            print(dialog.getInputText())


def start():
    ui = TestUI()
    with open("qarc-dark.css", "r") as f:
        print(f)
        ui.setStyleSheet("".join(f.readlines()))
    ui.show()
    return ui


if __name__ == '__main__':

    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    ui = start()
    app.exec_()