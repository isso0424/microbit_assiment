import atexit
from tkinter import *
from PIL import Image
import serial

class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("brightness manager")
        image_cache = Image.open("static/picture.png")
        self.width, self.height = image_cache.size
        self.root.minsize(self.width, self.height)
        self.ser = serial.Serial("/dev/ttyACM0", 115200)
        atexit.register(self.ser.close)

    def execute(self):
        image = PhotoImage(file="static/picture.png")
        canvas = Canvas(bg="black", width=self.width, height=self.height)
        canvas.place(x=0, y=0)
        canvas.create_image(0, 0, image=image, anchor=NW)

        while True:
            line = self.ser.readline().decode()
            if "dark" in line:
                self.root.mainloop()

def main():
    while True:
        window = Window()
        window.execute()

if __name__ == "__main__":
    main()
