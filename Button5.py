from kivy.app import App 
from kivy.uix.button import Button

class MyApp(App):
    def button_pressed(self, instance):
        print("Button Pressed!")


    def build(self):
        button = Button(text='Click Me!', size_hint=(0.5, 0.5),
                        pos_hint={'Center_x': 0.5, 'center_y': 0.5})
                                  

        return button
    
if __name__ == '__main__':
    MyApp().run()
