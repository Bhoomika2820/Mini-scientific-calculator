import kivy
import math

kivy.require("1.11.1")

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from fractions import Fraction


class CalcGridLayout(GridLayout):
    Window.size = (320, 500)

    def fraction(self, j):
        if "=" in j:
            s = j.split("\n=")
            j = (str(eval(s[1])))
            if "." in j:
                self.display.text = s[0] + "\n=" + str(Fraction(float(j)).limit_denominator(1000))
            elif "/" in j:
                self.display.text = j + "\n=" + str(eval(j))

        else:
            self.display.text = j + "\n=" + str(eval(j))

    def sign(self, input):
        if input:
            c = []
            if "=" in input:
                c = input.split("\n=")
            else:
                c.append(0)
                c.append(input)
            try:
                if c[1][0] == "-":
                    self.display.text = c[1][1:]
                else:
                    self.display.text = "-" + c[1]
            except Exception:
                pass

    def calculate(self, calculation):
        g = calculation
        if calculation:
            try:
                if "%" in calculation:
                    c = calculation.split("%")
                    calculation = "/100".join(c)
                if "\u03C0" in calculation:
                    c = calculation.split("\u03C0")
                    calculation = "(22/7)".join(c)
                if "^" in calculation:
                    c = calculation.split("^")
                    calculation = "**".join(c)
                if "\u00B2" in calculation:
                    c = calculation.split("\u00B2")
                    calculation = "**2".join(c)
                if "=" in calculation:
                    s = calculation.split("\n=")
                    self.display.text = (str(eval(s[1])))
                if "=" not in calculation:
                    self.display.text = g + "\n=" + str(eval(calculation))

            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()


CalcApp = CalculatorApp()
CalcApp.run()
