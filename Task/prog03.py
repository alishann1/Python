class DimmerSwitch:
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def toggle(self):
        self.is_on = not self.is_on
        if self.is_on:
            self.brightness = 0
        else:
            self.brightness = 10

    def change_brightness(self, change):
        if self.is_on:
            self.brightness = max(0, min(10, self.brightness + change))

    def __str__(self):
        return f"Dimmer Switch: {'On' if self.is_on else 'Off'}, Brightness {self.brightness}"
