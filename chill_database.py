
from data_json import load_json_data,write_json_data

#khởi tạo khuôn mãu cho sản phẩm cuối khoá
class User:
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password

class UsernameDatabase:
    def __init__(self):
        self.user_list = list()
        self.user_dict_data = load_json_data("user.json") #danh sach cac user dict
        self.user_email_list = self.get_email_list()

    def get_email_list(self):
        return [user["email"] for user in self.user_dict_data]

    def load_data(self):
        for user_dict in self.user_dict_data:
            user = User( username=user_dict["username"],
                        email =user_dict["email"],
                        password=user_dict["password"])
            
            self.user_list.append(user) # them du lieu vao list

    def add_user_from_dict(self,user_dict):
        user_dict["id"] = len(self.user_list)
        new_user = User( username=user_dict["username"],
                        email =user_dict["email"],
                        password=user_dict["password"])
        self.user_list.append(new_user)
        self.user_dict_data.append(user_dict)
        write_json_data("user.json",self.user_dict_data)

    #def get_item_by_title(self, anime_name)  

class Model:
    def __init__(self,id,name,desc,desc_detail,brand,price,image,released_date=None):
        self.id = id
        self.name = name
        self.desc = desc
        self.desc_detail = desc_detail
        self.brand = brand
        self.price = price
        self.image = image
        self.released_date = released_date
        

        #cập nhật mô hình
    def update(self,new_data):
        for k, v in new_data.items():
            if v:
                setattr(self,k ,v)

#khởi tạo danh sách cho mô hình
class ModelDatabase:
    def __init__(self):
        self.model_list = list()
        self.model_dict_data = load_json_data("data.json") #danh sach
        #cac model dict
        self.model_title_list = self.get_all_model_name() # danh sách các model dict


    def get_all_model_name(self):
        return [model["name"] for model in self.model_dict_data]
    # đọc giữ liệu file Json
    def load_data(self):
        for model_dict in self.model_dict_data:
            model = Model( id = model_dict["id"],
                        name = model_dict["name"],
                        desc = model_dict["desc"],
                        desc_detail = model_dict["desc_detail"],
                        brand = model_dict["brand"],
                        price =model_dict["price"],
                        image =model_dict["image"],
                        released_date = model_dict["released_date"],
                        )
            
            self.model_list.append(model) #thêm dữ liệu vào list

    def add_item_from_dict(self, model_dict):
        model_dict["id"] = len(self.model_title_list)
        new_item = Model( id = model_dict["id"],
                        name = model_dict["name"],
                        desc = model_dict["desc"],
                        desc_detail = model_dict["desc_detail"],
                        brand = model_dict["brand"],
                        price =model_dict["price"],
                        image =model_dict["image"],
                        released_date = model_dict["released_date"],
        )
        self.model_list.append(new_item)
        self.model_dict_data.append(model_dict)
        write_json_data("data.json",self.model_dict_data) # ghi dữ liệu vào

    def get_item_by_title(self, model_name) -> Model:
        for model_item in self.model_list:
            if model_item.name == model_name:
                return model_item
    # từ item tìm được hoặc cập nhật sẽ biến về lại thành dạng dict để có thể lưu xuống file json
    def item_to_data(self):
        json_data = list()
        for model in self.model_list:
            json_data.append(model.__dict__)
        return json_data
    
    # chỉnh sửa model  
    def edit_item_from_dict(self, edit_title, model_dict: Model):
        model_edit = self.get_item_by_title(edit_title)
        model_edit.update(model_dict)
        self.model_dict_data = self.item_to_data()
        write_json_data("data.json",self.model_dict_data)
    
    # xoá model
    def delete_item(self, delete_title):
        anime_delete = self.get_item_by_title(delete_title) # tìm ra thằng anime bằng cách truyền title vào
        self.model_list.remove(anime_delete) # sử dụng hàm mà list hỗ trợ (remove) để xóa
        self.anime_dict_data = self.item_to_data()
        write_json_data("data.json",self.anime_dict_data)

    def printTable(self):
        from prettytable import PrettyTable
        t = PrettyTable(["Mã mô hình", "Tên mô hình","Mô tảtả", "Kích thước","Giá","Hình ảnh","Ngày đăng"])
        for model in self.list_model:
            t.add_row([model.id,model.name,model.desc,model.brand,model.price,model.image,model.released_date])
        print(t)

    def addMode(self,model):
        self.list_model.append(model)
        self.printTable()


    def removeModel(self,id):
        for model in self.list_model:
            if model.id == id:
                self.list_model.remove(model)
                break
        self.printTable()

    def updateModle(self,id,**zaidep):
        for model in self.list_model:
            if model.id == id:
                model.update(zaidep)
                break
        self.printTable() 




class Cart(Model):
    def __init__(self, id, name, desc, desc_detail, brand, price, image, released_date=None):
        super().__init__(id, name, desc, desc_detail, brand, price, image, released_date)
        

        #cập nhật mô hình
    def update(self,new_data):
        for k, v in new_data.items():
            if v:
                setattr(self,k ,v)

class CartDatabase():
    def __init__(self):
        self.model_list = list()
        self.model_dict_data = load_json_data("cart.json") #danh sach
        self.model_title_list = self.get_all_model_name() # danh sách các model dict


    def get_all_model_name(self):
        return [model["name"] for model in self.model_dict_data]
    # đọc giữ liệu file Json
    def load_data(self):
        for model_dict in self.model_dict_data:
            model = Model( id = model_dict["id"],
                        name = model_dict["name"],
                        desc = model_dict["desc"],
                        desc_detail = model_dict["desc_detail"],
                        brand = model_dict["brand"],
                        price =model_dict["price"],
                        image =model_dict["image"],
                        released_date = model_dict["released_date"],
                        )
            
            self.model_list.append(model) #thêm dữ liệu vào list

    def add_item_from_dict(self, model_dict):
        model_dict["id"] = len(self.model_title_list)
        new_item = Model( id = model_dict["id"],
                        name = model_dict["name"],
                        desc = model_dict["desc"],
                        desc_detail = model_dict["desc_detail"],
                        brand = model_dict["brand"],
                        price =model_dict["price"],
                        image =model_dict["image"],
                        released_date = model_dict["released_date"],
        )
        self.model_list.append(new_item)
        self.model_dict_data.append(model_dict)
        write_json_data("cart.json",self.model_dict_data) # ghi dữ liệu vào
