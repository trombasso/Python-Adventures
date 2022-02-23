import tkinter as tk
import math


class Circle:
    def __init__(self, x, y, radius):  # x og y er sirkelens senterposisjon
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__radius

    def isInside(self, x, y):
        if x > (self.__x + self.__radius) and y > (self.__y + self.__radius):
            return True
        else:
            return False


class CreateGUI:
    def __init__(self):
        # Lag vindu:
        window = tk.Tk()
        window.title("Two Circles")

        # Oppretter et Canvas:
        self.canvas = tk.Canvas(window, width=250, height=150)
        self.canvas.pack()
        # Oppretter første sirkelobjekt, samt visuell representasjon av denne:
        self.circle1 = Circle(20, 20, 20)
        self.circle1Canvas = self.canvas.create_oval(
            self.circle1.getX(),
            self.circle1.getY(),
            self.circle1.getX() + 2 * self.circle1.getRadius(),
            self.circle1.getY() + 2 * self.circle1.getRadius(),
            fill="red",
            tags="circle1",
        )
        # Oppretter andre sirkelobjekt, samt visuell representasjon av denne:
        self.circle2 = Circle(120, 50, 20)
        self.circle2Canvas = self.canvas.create_oval(
            self.circle2.getX(),
            self.circle2.getY(),
            self.circle2.getX() + 2 * self.circle2.getRadius(),
            self.circle2.getY() + 2 * self.circle2.getRadius(),
            fill="blue",
            tags="circle2",
        )
        # Linje som skal koble sirklene sammen:
        self.canvas.create_line(40, 40, 140, 70, tags="line")
        # Tekst som skal angi avstand i antall piksler:
        distance = self.calculateDistanceBetweenCircles()
        self.canvas.create_text(60, 60, text=distance, tags="text")

        self.canvas.bind("<B1-Motion>", self.mouseMoved)

        window.mainloop()  # Kjører eventløkke

    def calculateDistanceBetweenCircles(self):
        distance = math.sqrt((self.circle1.getX() - self.circle2.getX()) ** 2 + (self.circle1.getY() - self.circle2.getY()) ** 2)
        return round(distance, 2)

    def createDistanceLine(self):
        # Sletter først gammel linje:
        self.canvas.delete("line", "text")
        # Lager ny linje:
        self.canvas.create_line(self.circle1.getX(), self.circle1.getY(), self.circle2.getX(), self.circle2.getY(), tag="line")
        # Ny tekst:
        self.canvas.create_text(
            self.circle2.getX() - self.circle1.getX(),
            self.circle2.getY() - self.circle1.getY(),
            text=self.calculateDistanceBetweenCircles(),
            tags="text",
        )

    def createNewCircle(self, x, y, tag):
        # Sletter først gamle sirkler:
        self.canvas.delete(tag)
        # Lager ny sirkel:
        if tag == "circle1":
            self.circle1 = Circle(x, y, 20)
            self.circle1Canvas = self.canvas.create_oval(
                self.circle1.getX() - self.circle1.getRadius(),
                self.circle1.getY() - self.circle1.getRadius(),
                self.circle1.getX() + self.circle1.getRadius(),
                self.circle1.getY() + self.circle1.getRadius(),
                fill="red",
                tag="circle1",
            )
        elif tag == "circle2":
            self.circle2 = Circle(x, y, 20)
            self.circle2Canvas = self.canvas.create_oval(
                self.circle2.getX() - self.circle2.getRadius(),
                self.circle2.getY() - self.circle2.getRadius(),
                self.circle2.getX() + self.circle2.getRadius(),
                self.circle2.getY() + self.circle2.getRadius(),
                fill="blue",
                tag="circle2",
            )

    def mouseMoved(self, event):
        # Finner ut som musa er over en av sirklene:
        if self.circle1.isInside(event.x, event.y):
            # print("JA MUSA ER INNAFOR SIRKELEN")
            self.createNewCircle(event.x, event.y, "circle1")
        elif self.circle2.isInside(event.x, event.y):
            # print("JA MUSA ER INNAFOR SIRKELEN")
            self.createNewCircle(event.x, event.y, "circle2")
        self.createDistanceLine()


CreateGUI()  # Lag GUI
