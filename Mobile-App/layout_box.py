# Python program to display box layout using different colors

import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
black = [0, 0, 0, 0]

class BoxLayoutH(App):
    def build(self):
        layout = BoxLayout(padding = 5)
        colors = [red, green, blue, black]

        for i in range(5):
            btn = Button(text = "Button #%s" % (i + 1),
                background_color = random.choice(colors))
            layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    app = BoxLayoutH()
    app.run()