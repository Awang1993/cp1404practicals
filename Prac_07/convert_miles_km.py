"""
CP1404 Practicals
Kivy GUI for Miles to Kilometres Converter
"""

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

__author__ = 'Adrian Wang'

MILES_TO_KILOMETRES = 1.60934


class ConvertMilesKm(App):
    """Miles to Kilometres converter App"""
    output_label = StringProperty()

    def build(self):
        """Build the Kivy app from kv file"""
        Window.size = (700, 300)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_miles_to_kilometres(self):
        """handle conversion and displays to output label"""
        value = self.validate_input()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def handle_change_input(self, increment):
        """Increases or decreases input number value"""
        result = self.validate_input() + increment
        self.root.ids.input_number.text = str(result)

    def validate_input(self):
        """Validates input and handles errors without crashing"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesKm().run()