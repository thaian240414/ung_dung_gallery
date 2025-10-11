from guizero import App, Box, Text

app = App("Thời khóa biểu lớp 6.6", width=800, height=400, bg="white")

box = Box(app, layout="grid")

Text(box, text="Tiết", grid=[0,0])
Text(box, text="Thứ 2", grid=[1,0])
Text(box, text="Thứ 3", grid=[2,0])
Text(box, text="Thứ 4", grid=[3,0])
Text(box, text="Thứ 5", grid=[4,0])
Text(box, text="Thứ 6", grid=[5,0])

Text(box, text="1", grid=[0,1])
Text(box, text="Toán", grid=[1,1])
Text(box, text="Tin học", grid=[2,1])
Text(box, text="Ngữ văn", grid=[3,1])
Text(box, text="KHTN (Lý)", grid=[4,1])
Text(box, text="Ngữ văn", grid=[5,1])

Text(box, text="2", grid=[0,2])
Text(box, text="KHTN (Hóa)", grid=[1,2])
Text(box, text="KHTN (Sinh)", grid=[2,2])
Text(box, text="Ngữ văn", grid=[3,2])
Text(box, text="Toán", grid=[4,2])
Text(box, text="Tiếng Anh", grid=[5,2])

Text(box, text="3", grid=[0,3])
Text(box, text="Ngữ văn", grid=[1,3])
Text(box, text="GDĐP", grid=[2,3])
Text(box, text="GDCD", grid=[3,3])
Text(box, text="Toán", grid=[4,3])
Text(box, text="LS-ĐL (Sử)", grid=[5,3])

Text(box, text="4", grid=[0,4])
Text(box, text="LS-ĐL (Địa)", grid=[1,4])
Text(box, text="Toán", grid=[2,4])
Text(box, text="KHTN (Sinh)", grid=[3,4])
Text(box, text="Công nghệ", grid=[4,4])
Text(box, text="HĐTN-HN3", grid=[5,4])

Text(box, text="5", grid=[0,5])
Text(box, text="SHDC", grid=[1,5])
Text(box, text="Tiếng Anh", grid=[2,5])
Text(box, text="LS-ĐL (Sử)", grid=[3,5])
Text(box, text="Tiếng Anh", grid=[4,5])
Text(box, text="", grid=[5,5])

app.display()