# -*- coding: utf-8 -*-

"""
Module implementing browser.
"""
import sys
from PyQt5.QtCore import pyqtSlot,  QUrl
from PyQt5.QtWidgets import QDialog,  QApplication

from Ui_browser import Ui_Dialog


class browser(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(browser, self).__init__(parent)
        self.setupUi(self)
        
        url = 'http://www.baidu.com'
        self.url.setText(url)
        self.webView.setUrl(QUrl(url))
        self.back.setEnabled(False)
        self.next.setEnabled(False)
    
    def __setHistButtonState(self,  page,  back,  next):
        history = page.history()
        
        if back is not None:
            if history.canGoBack():
                back.setEnabled(True)
            else:
                back.setEnabled(False)
                
        if next is not None:
            if history.canGoForward():
                next.setEnabled(True)
            else:
                next.setEnabled(False)
                
    @pyqtSlot(int)
    def on_webView_loadProgress(self, load):
        if load == 100:
            self.stop.setEnabled(False)
        else:
            self.stop.setEnabled(True)
    
    @pyqtSlot(str)
    def on_webView_titleChanged(self, title):
        self.setWindowTitle(title)
    
    @pyqtSlot(QUrl)
    def on_webView_linkClicked(self, url):
        page = self.webView.page()
        self.__setHistButtonState(page,  self.back,  self.next)
        self.url.setText(url.toString())
    
    @pyqtSlot(QUrl)
    def on_webView_urlChanged(self, url):
        page = self.webView.page()
        self.__setHistButtonState(page,  self.back,  self.next)
        self.url.setText(url.toString())
    
    @pyqtSlot()
    def on_back_clicked(self):
        page = self.webView.page()
        self.__setHistButtonState(page,  self.back,  None)
        history = page.history()
        history.back()
        
    @pyqtSlot()
    def on_next_clicked(self):
        page = self.webView.page()
        history = page.history()
        history.forward()
        self.__setHistButtonState(page,  None,  self.next)
    
    @pyqtSlot()
    def on_stop_clicked(self):
        self.webView.stop()
    
    @pyqtSlot()
    def on_reload_clicked(self):
        self.webView.setUrl(QUrl(self.url.text()))
    
    @pyqtSlot()
    def on_url_returnPressed(self):
        page = self.webView.page()
        history = page.history()
        if history.canGoBack():
            self.back.setEnabled(True)
        else:
            self.back.setEnabled(False)
            
        if history.canGoForward():
            self.next.setEnabled(True)
        else:
            self.next.setEnabled(False)
            
        url = self.url.text()
        self.webView.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = browser()
    browser.show()
    sys.exit(app.exec_())
