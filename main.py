import atexit
from tkinter import *
import serial

class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("brightness manager")
        self.root.minsize(603, 650)
        self.ser = serial.Serial("/dev/ttyACM0", 115200)
        atexit.register(self.ser.close)

    def execute(self):
        image = PhotoImage(file="static/hibiki_icon.png")
        canvas = Canvas(bg="black", width=603, height=600)
        canvas.place(x=0, y=0)
        canvas.create_image(0, 0, image=image, anchor=NW)

        while True:
            line = self.ser.readline().decode()
            if "dark" in line:
                self.root.mainloop()
                return

    def close_window(self):
        self.root.destroy()

def main():
    while True:
        window = Window()
        window.execute()

if __name__ == "__main__":
    main()
