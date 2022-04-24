

def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == "left" or keycode[1] == "numpad4":
        self.current_speed_x = self.SPEED_X
    elif keycode[1] == "right" or keycode[1] == "numpad6":
        self.current_speed_x = - self.SPEED_X

    if keycode[1] == "up" or keycode[1] == "numpad8":
        self.SPEED_Y += .1

    return True


def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0
    self.SPEED_Y = .2
    return True


def on_touch_down(self, touch):
    if touch.x < self.width / 2:
        self.current_speed_x = self.SPEED_X

    else:
        self.current_speed_x = - self.SPEED_X


def on_touch_up(self, touch):
    self.current_speed_x = 0