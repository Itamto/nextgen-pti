from dialog import AddDialog,EditDialog
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

class ModelCRUD:
    def add(self):
        currIndex =self.ui.listWidget.currentRow()
        add_dialog = AddDialog()
        if add_dialog.exec():
            inputs = add_dialog.return_input_fields()
            print(inputs)
            self.ui.listWidget.insertItem(currIndex, inputs["name"])
            self.dtb.add_item_from_dict(inputs)
            self.layout.update_layout() #cập nhật Layout

    def edit(self):
        currIndex =self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currIndex)
        item_title = item.text()
        edit_item = self.dtb.get_item_by_title(item_title)
        if item is not None:
            edit_dialog = EditDialog(edit_item)
            if edit_dialog.exec():
                inputs = edit_dialog.return_input_fields()
                item.setText(inputs["name"])
                self.dtb.edit_item_from_dict(item_title, inputs)
                self.layout.update_layout()#cập nhật Layout
                
    
    def remove(self):
        curr_index = self.ui.listWidget.currentRow() # lấy vị trí index hiện tại trong listWidget
        item = self.ui.listWidget.item(curr_index) # chuyển đổi nó thành 1 anime item
        item_title = item.text() # lấy ra text 
        if item is None:
            return
        # tạo hộp thoại để người dùng xác nhận, người dùng bấm yes mới xóa
        question = QMessageBox.question(self, "Xóa sản phẩm",
                                        f"Bạn có chắc chắn muốn xóa {item_title} không?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if question == QMessageBox.StandardButton.Yes:
            item = self.ui.listWidget.takeItem(curr_index) # lấy ra vị trí hiện tại và xóa nó trên UI
            self.dtb.delete_item(item_title)
            self.layout.update_layout()#cập nhật Layout
        
    def search(self):
        self.handleChangeNav(2)
        search_anime_field = self.ui.txtSearch.text().strip() #lấy ra đoạn text từ ô input search
        if search_anime_field: # nếu mà nó không bị rỗng
            matched_items = self.ui.listWidget.findItems(search_anime_field, Qt.MatchFlag.MatchContains) # tìm ra item giống kí tự mà người dùng gõ
            # hiển thị những thằng giống nó lên listWidget
            for i in range(self.ui.listWidget.count()):
                it = self.ui.listWidget.item(i)
                it.setHidden(it not in matched_items)
        else:
            #ngược lại ẩn những thằng không liên quan
            for i in range(self.ui.listWidget.count()):
                it = self.ui.listWidget.item(i)
                it.setHidden(False)