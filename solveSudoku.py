from sudoku.Sudoku import Sudoku
from pprint import pprint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.boxlayout import BoxLayout

class MySudokuWidget(Widget):
    def on_touch_down(self,touch):
        with self.canvas:
                Color(2,2,2)
                d = 40.
                Ellipse(pos=(touch.x - d / 2, touch.y - d /2), size=(d,d))
                touch.ud['line'] = Line(points =(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        print(touch.ud)

class MarvelApp(BoxLayout):
    def build(self):



class SolveSudokuApp(App):
    pass
"""
class SolveSudoku(App):
    def build(self):
        s = Sudoku()
        s.printCanvas()
        s.startSolve()
        s.printCanvas()
        return MySudokuWidget()
"""
if __name__ == "__main__":
    #SolveSudoku().run()
    Marvel().build()
