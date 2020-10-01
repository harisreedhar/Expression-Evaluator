import kivy
kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from math import*
Window.clearcolor = (0.95, 0.95, 0.95, 1)
Window.size = (600, 300)
 
class EvalGridLayout(GridLayout):
 
    # Function called when evaluate button is pressed
    def evaluate(self, expression):
        if expression:
            try:
                self.display.text = ""
                self.display.text = str(eval(expression))
            except Exception:
                self.display.text = "Error"

class EvaluatorApp(App):

    def build(self):
        return EvalGridLayout()
 
evalApp = EvaluatorApp()
evalApp.run()