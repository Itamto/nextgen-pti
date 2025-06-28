import json

#hàm giúp load dưc liệu lên khi mở chương trình lần đầu
def load_json_data(file_name):
    temp_data = list ()#khai báo 1 dạng list

    with open(f"data/{file_name}","r") as json_in:
        json_data = json.load(json_in)

# sử dụng phương thức kế thừa lại toàn bộ cấu trúc của file data.json
    temp_data.extend(json_data)
    return temp_data

def write_json_data(file_name,json_data):
    with open(f"data/{file_name}","w") as json_out:
        json.dump(json_data,json_out)