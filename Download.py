    #This paragraph in any PyQt Projest.
__auther__='Mohamed Hamada Salama'
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import os
from os import path
import sys
import pafy
import humanize

import urllib.request


Form_Class,_=loadUiType(path.join(path.dirname(__file__),"Download.ui"))


class MainApp(QMainWindow , Form_Class ):
    def __init__(self , parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Ui()
        self.Handel_Buttons()


         ## Code to a program##
    def Handel_Ui(self):
        self.setWindowTitle('PyDownloader')
        self.setFixedSize(651,281)


    def Handel_Buttons(self):

        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.Handel_Browse)
        self.pushButton_7.clicked.connect(self.Get_Youtube_Video)
        self.pushButton_4.clicked.connect(self.Download_Youtube_Video)
        self.pushButton_3.clicked.connect(self.Save_Browse)
        self.pushButton_5.clicked.connect(self.Save_Browse)
        self.pushButton_6.clicked.connect(self.Playlist_Download)


    def Handel_Browse(self):
        save_place = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files (*.*)")
        text = str(save_place)
        name = (text[2:].split(',')[0].replace("'"  , ''))
        self.lineEdit_2.setText(name)



    def Handel_Progress(self , blocknum , blocksize , totalsize):
       read = blocknum * blocksize
       if totalsize > 0:
           percent = read * 100 / totalsize
           self.progressBar.setValue(percent)
           QApplication.processEvents()   #Not Responding

    def Download(self):

        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        try:
            urllib.request.urlretrieve(url , save_location , self.Handel_Progress)
        except Exception:
            QMessageBox.warning(self, "Download Error", "The Download Failed")
            return

        QMessageBox.information(self, "Download Completed", "The Download Finished")
        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

    def Save_Browse(self):
        save = QFileDialog.getExistingDirectory(self , "Select Download Directory")
        self.lineEdit_4.setText(save)
        self.lineEdit_6.setText(save)



    def Get_Youtube_Video(self):
       video_link = self.lineEdit_3.text()
       v = pafy.new(video_link)
       #print(v.title)
       #print(v.duration)
       #print(v.rating)
       #print(v.author)
       #print(v.length)
       #print(v.keywords)
       #print(v.thumb)
       #print(v.videoid)
       #print(v.viewcount)
       #print(st)
       st = v.videostreams
       for s in st :
           size = humanize.naturalsize(s.get_filesize())
           data = '{} {} {} {}' .format(s.mediatype , s.extension , s.quality , size)
           self.comboBox.addItem(data)

    def Download_Youtube_Video(self):

         video_link = self.lineEdit_3.text()
         save_location = self.lineEdit_4.text()

         v = pafy.new(video_link)
         st = v.videostreams
         quality = self.comboBox.currentIndex()

         down = st[quality].download(filepath=save_location)

         QMessageBox.information(self, "Download Completed", "The Video Download Finished")

    def Playlist_Download(self):
        playlist_url = self.lineEdit_5.text()
        save_location = self.lineEdit_6.text()
        playlist = pafy.get_playlist(playlist_url)
        videos = playlist['items']

        os.chdir(save_location)
    
        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))
        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))

        for video in videos :
            p = video['pafy']
            best = p.getbest(preftype='mp4')
            best.download()

     #####Complete Code To Any Program Ui in PyQt ####
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()   #infinite loop

if __name__=='__main__':
    main()

