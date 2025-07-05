from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QHBoxLayout,QMessageBox
from PyQt6 import uic
import sys

from chill_database import ModelDatabase,Model,UsernameDatabase
from utils import ModelCRUD
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
class PageHome(QMainWindow):
    def __init__(self):
        super().__init__()
        global widget
        self.ui = uic.loadUi("gui/main.ui", self)
        widget = self.ui
        self.handleChangeNav(0) # mặc định là home
        self.ui.btnNavHome.clicked.connect(lambda: self.handleChangeNav(0))
        self.ui.btnNavLeaderboard.clicked.connect(lambda: self.handleChangeNav(1))
        self.ui.btnNavAdd.clicked.connect(lambda: self.handleChangeNav(2))
        self.ui.btnNavSetting.clicked.connect(lambda: self.handleChangeNav(3))
        self.ui.btnNavInfo.clicked.connect(lambda: self.handleChangeNav(4))
        self.ui.btnNavShop.clicked.connect(lambda: self.handleChangeNav(5))
    
        global database
        self.dtb = ModelDatabase()
        database =self.dtb
        self.setup_CRUD()
        self.setup_ShowModel()

            
    def setup_CRUD(self):
        database.load_data()
        self.listWidget.addItems(database.model_title_list)
        widget.btn_add.clicked.connect(lambda: ModelCRUD.add(self))
        widget.btn_edit.clicked.connect(lambda: ModelCRUD.edit(self))
        widget.btn_remove.clicked.connect(lambda: ModelCRUD.remove(self))
        widget.txtSearch.textChanged.connect(lambda: ModelCRUD.search(self))

    def handleChangeNav(self,index):
        self.ui.stackedWidget.setCurrentIndex(index)

    def setup_ShowModel(self): 
# tạo ra một layout để chứa các item, sau đó hiển thị nó lên UI 
        global h_layout 
        self.horizontal_layout= QHBoxLayout(self.ui.scrollAreaWidgetContents) 
        h_layout = self.horizontal_layout 
        h_layout.setAlignment(Qt.AlignmentFlag.AlignLeft) 
        self.layout = ModelHorizontalLayout() 
        self.layout.display_layout()

class ModelHorizontalLayout():
    def display_layout(self):
        for model in database.model_list:
            model_item_widget = ModelItemWidget(model)
            h_layout.addWidget(model_item_widget)
        widget.scrollAreaWidgetContents.setLayout(h_layout)

    def clear_layout(self):
        while h_layout.count():
            child = h_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def update_layout(self, item_list=None):
        self.clear_layout()

        if item_list is None:
            item_list = database.model_list
            #Update layout from custom item list
            for model in item_list:
                model_item_widget = ModelItemWidget(model)
                h_layout.addWidget(model_item_widget)

from dialog import ShowDetailDialog
class ModelItemWidget(QWidget):
    def __init__(self, model:Model):
        QWidget.__init__(self)
        self.ui = uic.loadUi("gui/model_column.ui", self)

        self.model = model
        self.display_description()
        self.ui.image.mousePressEvent = lambda e: self.handleShowDetail(e)
    #bấm vào sẽ hiện phần chi tiết
    def handleShowDetail(self,e):
        self.show_detail_dialog = ShowDetailDialog(self.model)
        self.show_detail_dialog.exec()
        
    def display_description(self):
        img_pixmap = QPixmap(self.model.image)
        self.ui.title.setText(self.model.name)
        self.ui.desc.setText(self.model.desc)#hiện thị derecspin
        self.ui.image.setPixmap(img_pixmap)#hiện thị hình ảnh
class MessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thông báo")
        self.setIcon(QMessageBox.Icon.Warning)
        self.setStyleSheet("background-coler: #F8F2EC; coler: #356a9c")

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("gui/login.ui",self)
        self.msg = MessageBox()
        self.ui.btnLogin.clicked.connect(self.handLeLogin)
        self.ui.btnregister.clicked.connect(self.handleRegister)
    def handleRegister(self):
        registerPage.show()
        self.close
    def handLeLogin(self):
        self.user = UsernameDatabase()
        self.user.load_data()

        email = self.ui.txtEmail.text()
        password = self.ui.txtPassword.text()

        if not password:
            self.msg.setText("Vui lòng không bỏ trống password")
            self.msg.exec()
            self.ui.txtPassword.setFocus()
            return
        
        if not email:
            self.msg.setText("Vui lòng không bỏ trống email")
            self.msg.exec()
            self.ui.txtEmail.setFocus()
            return
# kiểm tra email và password
        if email in self.user.user_email_list:
            index = self.user.user_email_list.index(email)
            if password == self.user.user_list[index].password:
                #Nếu đăng nhập thành công , chuyển sang giao diện chính (Main)
                self.msg.setText("Đăng nhập thành công")
                self.msg.exec()
                self.close()
                myWindow.show()
            else:
                #nếu mật khẩu ko đúng , hiện thị báo lỗi
                self.msg.setText("Mật khẩu không đúng")
                self.msg.exec()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("gui/register.ui",self)

        self.msg = MessageBox()
        self.user = UsernameDatabase()
        self.user.load_data()
        self.ui.btnRegister.clicked.connect(self.handleRegister)
        self.ui.btnlogin.clicked.connect(self.handLeLogin)

    def handLeLogin(self):
        LoginPage.show()
        self.close

    def handleRegister(self):
        username = self.ui.txtUser.text()
        email = self.ui.txtEmail.text()
        password = self.ui.txtPassword.text()
        re_password = self.ui.txtRePassword.text()
        
        if not username:
            self.msg.setText("Vui lòng không bỏ trống username")
            self.msg.exec()
            self.ui.txtUser.setFocus()
            return
        
        if not email:
            self.msg.setText("Vui lòng không bỏ trống email")
            self.msg.exec()
            self.ui.txtEmail.setFocus()
            return
        
        if not password:
            self.msg.setText("Vui lòng không bỏ trống password")
            self.msg.exec()
            self.ui.txtPassword.setFocus()
            return
        
        if not re_password:
            self.msg.setText("Vui lòng không bỏ trống re_password")
            self.msg.exec()
            self.ui.txtRePassword.setFocus()
            return
        
        if email in self.user.get_email_list():
            self.msg.setText("Vui lòng đổi email khác vì email này đã được sử dụng")
            self.msg.exec()
            return
        
        if password != re_password:
            self.msg.setText("Mật Khẩu không khớp")
            self.msg.exec()
            return
        
        print(username,email,re_password,password)
        self.user.add_user_from_dict({
            "username": username,
            "email": email,
            "password": password
        })
        self.msg.setText(f"đang ký thành công với email là : {email}")
        self.msg.exec()
        LoginPage.show()
        registerPage.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = PageHome()

    LoginPage = Login()
    registerPage = Register()
    registerPage.show()
    
    sys.exit(app.exec())