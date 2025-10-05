from guizero import App, Text, Box, Picture

app = App(title="Ứng dụng",width=1100, height=1100, bg="#fffeed")

text = Text(app, text="Giới thiệu", size=20, color="#00d4b7")

box = Box(app, layout="grid", border=True)

picture1 = Picture(box, image="cho.png", grid = [0,0],width=200, height=200)

picture2 = Picture(box, image="cho1.png", grid = [1,0],width=200, height=200)

picture3 = Picture(box, image="cho2.png", grid = [2,0],width=200, height=200)

picture4 = Picture(box, image="cho3.png", grid = [0,1],width=200, height=200)

picture5 = Picture(box, image="cho.png", grid = [1,1],width=200, height=200)

picture6 = Picture(box, image="cho1.png", grid = [2,1],width=200, height=200)

picture7 = Picture(box, image="cho2.png", grid = [0,2],width=200, height=200)

picture8 = Picture(box, image="cho3.png", grid = [1,2],width=200, height=200)

picture9 = Picture(box, image="cho.png", grid = [2,2],width=200, height=200)

app.display()

