# Python program for touch event

from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        btn = Button(text = "Press it",
                size_hint = (0.2, 0.2),
                pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        btn.bind(on_press = self.on_press_btn)
        return btn
    
    def on_press_btn(self, instance):
        print("Hello! You pressed the button.")

if __name__ == '__main__':
    app = MainApp()
    app.run()