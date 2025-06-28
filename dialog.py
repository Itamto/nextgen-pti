from PyQt6.QtWidgets import QDialog,QFileDialog
from PyQt6 import uic
from PyQt6.QtCore import QDate , QDir
from chill_database import Model 
from PyQt6.QtGui import QPixmap

import os
class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("gui/add_dialog.ui",self)# load UIleen
        self.ui.btnImage.clicked.connect(lambda: self._browse_files())
        self.dir = QDir(os.getcwd())
    #thêm hình ảnh
    def _browse_files(self):
        fname = QFileDialog.getOpenFileName(self,"Open file","./ui/images")
        self.ui.btnImage.setText(fname[0])
        return fname
    #chạy câu lệnh khi người dùng ấn nút ok
    def return_input_fields(self):
        image_path_input = self.ui.btnImage.text()
        return {
            "name": self.ui.Name.text(),
            "desc": self.ui.Desc.text(),
            "desc_detail": self.ui.DescDetail.toHtml(),
            "brand": self.ui.Brand.text(),
            "price": self.ui.Price.text(),
            "image": self.dir.relativeFilePath(image_path_input),
            "released_date": self.ui.deReleaseData.date().toString("dd/MM/yy"),
        }
    
class EditDialog(QDialog):
    def __init__(self,edit_model:Model):
        super().__init__()
        self.ui = uic.loadUi("gui/edit_dialog.ui",self)# load UIleen
        self.ui.Name.setText(edit_model.name)
        self.ui.Desc.setText(edit_model.desc)
        self.ui.Brand.setText(edit_model.brand)  
        self.ui.Price.setText(edit_model.price)
        self.ui.DescDetail.setHtml(edit_model.desc_detail)
        self.ui.deReleaseData.setDate(QDate.fromString(edit_model.released_date,"dd/MM/yy"))
        self.ui.btnImage.setText(edit_model.image)
        self.ui.btnImage.clicked.connect(lambda: self._browse_files())
        self.dir = QDir(os.getcwd())
    #thêm hình ảnh
    def _browse_files(self):
        fname = QFileDialog.getOpenFileName(self,"Open file","./ui/images")
        self.ui.btnImage.setText(fname[0])
        return fname
    #chạy câu lệnh khi người dùng ấn nút ok
    def return_input_fields(self):
        image_path_input = self.ui.btnImage.text()
        
        return {
            "name": self.ui.Name.text(),
            "desc": self.ui.Desc.text(),
            "desc_detail": self.ui.DescDetail.toHtml(),
            "brand": self.ui.Brand.text(),
            "price": self.ui.Price.text(),
            "image": self.dir.relativeFilePath(image_path_input),
            "released_date": self.ui.deReleaseData.date().toString("dd/MM/yy")
        }
        
class ShowDetailDialog(QDialog):
    def __init__(self, model:Model):
        super().__init__()
        self.ui = uic.loadUi("gui/show_detail_dialog.ui",self)
        self.model = model
        self.display_description()
        
    def display_description(self):
        img_pixmap = QPixmap(self.model.image)
        self.ui.lb_name.setText(self.model.name)
        self.ui.lb_price.setText(f"{int(self.model.price):,}đ")
        self.ui.lb_image.setPixmap(img_pixmap)
        self.ui.lb_brand.setText("Thương hiệu: "+self.model.brand)
        self.ui.textBrowser.setHtml(self.model.desc_detail)