
#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
from PIL import Image
import glob
import os



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
    
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        
      
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self.label.setObjectName("label")
        self.myconvertButton = QtWidgets.QPushButton(self.centralWidget)
        self.myconvertButton.setGeometry(QtCore.QRect(224, 50, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        self.myconvertButton.setFont(font)
        self.myconvertButton.setObjectName("myconvertButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
       
        self.label.setText(_translate("MainWindow", "ENTER A NUMBER"))
        self.myconvertButton.setText(_translate("MainWindow", "CONVERT"))
        self.myconvertButton.clicked.connect(self.convert_answer)
		
		
    def button_answer(self):
        cap = cv2.VideoCapture('C:\\Users\\cem\\Pictures\\Camera Roll\\WIN_20160317_205235.mp4')
        #print ('cv2 version = {}'.format(cv2.__version__))
        while(cap.isOpened()):
              ret, frame = cap.read()
              print(frame)
              if ret is True :
                 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
              else :
                 continue
 
              cv2.imshow('frame',gray)
              if cv2.waitKey(1) & 0xFF == ord('q'):
                 break
         
             
        cap.release()
        cv2.destroyAllWindows() 

		 
    def convert_answer(self):
      
         cap = cv2.VideoCapture('C:\\Users\\cem\\Desktop\\staj2017\\Kaykay.mp4')
 
			   
			   
         framerate = cap.get(cv2.CAP_PROP_FPS)
         print("framerate: ",int(framerate))
         framecount = 0
         textvalue=self.lineEdit.text()
        
         while(cap.isOpened):

                success, frame = cap.read()
                cv2.imshow('window-name',frame)  
                framecount += 1
                if framecount % int(textvalue) == 0:
                   cv2.imwrite("frame%d.jpg" % framecount, frame)

                 #  framecount=0
             #   if framecount == framerate * 10: 
              #     framecount = 0
                 #  cv2.imshow('image',image)
         
                   dir = "C:\\Users\\cem\\Desktop\\staj2017" 
                   ext = ".jpg" 

                   pathname = os.path.join(dir, "*" + ext)


                   imgs = [ Image.open(i) for i in glob.glob(pathname) ]

                   min_img_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
                   img_merge = np.hstack( (np.asarray( i.resize(min_img_shape,Image.ANTIALIAS) ) for i in imgs ) )

                   img_merge = Image.fromarray( img_merge)
                   img_merge.save( 'framefinal.jpg' )
                  
				   
                   im = Image.open('C:\\Users\\cem\\Desktop\\staj2017\\giphy3.gif')
                   try:
                       while True:
                             new_frame = im.convert('RGBA')
                             new_frame.save('framefromgif%02d.png' % im.tell(), 'PNG')
                             im.seek(im.tell()+1)
                   except EOFError:
                          pass
					  
                   dir = "C:\\Users\\cem\\Desktop\\staj2017" 
                   ext_gif = ".png" 

                   pathname = os.path.join(dir, "*" + ext_gif)


                   imgs_gif = [ Image.open(i) for i in glob.glob(pathname) ]

                   min_img_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs_gif])[0][1]
                   img_merge = np.hstack( (np.asarray( i.resize(min_img_shape,Image.ANTIALIAS) ) for i in imgs_gif ) )

                   img_merge = Image.fromarray( img_merge)
                   img_merge.save( 'giffinal.png' )
                  
               
                   #ff=cv2.imread('framefinal.jpg',0)
                  # cv2.imshow('final image',ff)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                   break
			   
         cap.release()
         cv2.destroyAllWindows()

      
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(window)
	window.show()
	sys.exit(app.exec_())
