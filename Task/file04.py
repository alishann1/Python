class DimmerSwitch:
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print("Switch is on?", self.switchIsOn)
        print("Brightness is", self.brightness)


mySwitch = DimmerSwitch()


mySwitch.turnOn()
mySwitch.raiseLevel()
mySwitch.raiseLevel()
mySwitch.lowerLevel()
mySwitch.show()
