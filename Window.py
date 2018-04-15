#Start_Program
__auther__='Mohamed Salama'
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)

window = QWidget()
window = QMainWindow()
window.resize(200,250)
window.move(300,350)
#window.setGeometry(200 , 250 , 300 , 350)

window.setToolTip('the main program')
window.setWindowTitle('Hello PyQt')

window.setWindowIcon(QIcon('python.jpg'))

         #Message_Box
#btn = QPushButton('close' , window)
#btn.resize(500, 50)
#btn.move(80, 900)
#btn.clicked.connect(exit)
#btn.setToolTip('click to close')
#result = QMessageBox.question(window , 'Message' , 'Do You Want To Exit ?' , QMessageBox.Yes|QMessageBox.No)
#if result == QMessageBox.Yes:
#    print('Exit')
#else:
#    window.show()
#    print('open')

         #Line_Edit
#text_box = QLineEdit(window)
#text_box.resize(180,30)
#text_box.move(180,180)
#text_box.setPlaceholderText('Enter Your Name')
#text_box.setText('Python')
#text_box.setEchoMode(QLineEdit.Password)
#text = text_box.text()
#print (text)
#window.show()
#check1 = QCheckBox(window , text='Ios')
#check1.move(70,70)
#check1.setChecked(True)

           #Radio_Buttton
#rd1 = QRadioButton(window , text='Ios')
#rd1.move(80,80)
#rd1.setChecked(True)

#rd2 = QRadioButton(window , text='Android')
#rd2.move(100,100)

#check2 = QCheckBox(window , text='Android')
#check2.move(50,50)
#check2.setChecked(True)
#open_file = QFileDialog.getOpenFileName ( window , 'open file' , 'c : \' ')
#print(open_file)

#with open ( open_file , 'r') as f :
#    print(f.read())

         #Label
#lbl = QLabel(window , text='<b>User Name</b>')
#lbl.move(80,80)

#lbl2 = QLabel(window , text='<i>Password</i>')
#lbl2.move(80,110)

#user = QLineEdit(window)
#user.move(180,80)

#password = QLineEdit(window)
#password.move(180,110)
#password.setEchoMode(QLineEdit.Password)

        #Combo_Box
#cm = QComboBox(window)
#cm.move(80,80)
#cm.resize(60,20)
#cm.resize(60,20)
#cm.addItem('Windows')
#cm.addItem('Linux')
#cm.setCurrentIndex(2)

        #Progress_Bar
#pb = QProgressBar(window)
#pb.move(180,110)
#pb.resize(300,30)
#pb.setValue(90)
#pb.setAlignment(Qt.AlignCenter)

        #Slider
#s = QSlider(Qt.Horizontal , window)
#s.move(80,80)
#s.resize(200,20)
#s.setValue(60)

        #Color Dailog
#def show_color():
#    cd = QColorDialog.getColor()
#btn = QPushButton(window , text = 'colors')
#btn.move(80,80)
#btn.resize(100,60)
#btn.clicked.connect(show_color)

        #Font_Dailog
#def show_font():
#    fd = QFontDialog.getFont()
#btn = QPushButton(window , text = 'fonts')
#btn.move(80,80)
#btn.resize(100,50)
#btn.clicked.connect(show_font)
        #Calendar
#q = QCalendarWidget(window)
#data = q.selectedDate()

#lbl = QLabel(window)
#lbl.move(300,250)
#lbl.setText(data.toString())
        #StatusBar
#window.statusBar().showMessage('Ready')
        #MenuBar
mainmenu = window.menuBar()
file_menu = mainmenu.addMenu('File')
edit_menu = mainmenu.addMenu('Edit')
view_menu = mainmenu.addMenu('View')
navigate_menu = mainmenu.addMenu('Navigate')
code_menu = mainmenu.addMenu('Code')
run_menu = mainmenu.addMenu('Run')
tools_menu = mainmenu.addMenu('Tools')
vcs_menu = mainmenu.addMenu('Vcs')
window_menu = mainmenu.addMenu('Window')
window_menu = mainmenu.addMenu('Help')

exit_button = QAction(QIcon('linux.png'), 'Exit' , window )
exit_button.setShortcut('ctrl + Z')
exit_button.triggered.connect(window.close)

save_button = QAction('save', window)
file_menu.addAction(exit_button)
file_menu.addAction(save_button)


sub_menu = QMenu("save as")
sub_menu.addAction('.Png')
sub_menu.addAction('.Jpg')
sub_menu.addAction('.Jpeg')
sub_menu.addAction('.Gif')
sub_menu.addAction('.Psd')
sub_menu.addAction('.TIFF')
sub_menu.addAction('.BMP')
sub_menu.addAction('.RAW')
sub_menu.addAction('.DNG')
sub_menu.addAction('.Linux OS')
sub_menu.addAction('.Windows OS')
sub_menu.addAction('.Ubuntu OS')
sub_menu.addAction('.Back Box OS')
sub_menu.addAction('.Metasploit Linux OS')
sub_menu.addAction('.Python Gui')
sub_menu.addAction('.PyQt')
sub_menu.addAction('.Pycharm')

file_menu.addMenu(sub_menu)

       #ToolBar======#
#window.toolbar = window.addToolBar('Exit')
#window.toolbar.addAction(exit_button)
       #Table=======#
#table = QTableWidget()
#table_item = QTableWidgetItem()
#table.setWindowTitle('Table Title')

#table.setRowCount(9)
#table.setColumnCount(6)
#def click(Row , Column):
#    print ("Click on" + str(Row) + " " + str(Column))


#table.setItem(0,2, QTableWidgetItem("Pycharm"))
#table.setItem(1,1 , QTableWidgetItem("PyQT5"))
#table.setItem(0,1 , QTableWidgetItem("Python"))

#table.setHorizontalHeaderLabels(("A1 ,B2 ,C3 , D4 ,E5 , F6").split(','))
#table.setVerticalHeaderLabels(("G1 ,H2 ,I3 ,J4 ,K5 ,L6 ,M7 ,N8 ,O9 ").split(','))

#table.horizontalHeader().setToolTip('Column')
#table.horizontalHeaderItem(1).setToolTip('Column 1')

#table.verticalHeader().setToolTip('Row')
#table.verticalHeaderItem(2).setToolTip('Row 1')

#table.cellClicked.connect(click)


        #Final_Program
window.show()
#table.show()
app.exec_()


