# Python program for press event using KV design language
# For KV we use button.kv

from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_btn(self):
        print("Hello! You pressed the button.")

if __name__ == '__main__':
    app = ButtonApp()
    app.run()