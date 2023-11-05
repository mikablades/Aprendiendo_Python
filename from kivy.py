from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MiWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MiWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.label = Label(text='Introduce algo:')
        self.add_widget(self.label)
        
        self.text_input = TextInput(multiline=False)
        self.add_widget(self.text_input)
        
        self.button = Button(text='Presiona aquí')
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)
        
    def on_button_press(self, instance):
        self.label.text = self.text_input.text

class MiAplicacion(App):
    def build(self):
        return MiWidget()

if __name__ == '__main__':
    MiAplicacion().run()
