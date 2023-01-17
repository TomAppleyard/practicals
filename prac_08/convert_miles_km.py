from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_FACTOR = 1.60934


class ConvertMilesApp(App):
    """An app to convert miles to km"""
    def build(self):
        """Build Kivy app"""
        Window.size = (1000, 600)
        self.title = 'Convert Miles to km'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        """Increases or decreases input miles by the value inputted in the kivy file"""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_conversion()

    def handle_conversion(self):
        """Converts number based on input miles"""
        value = self.get_valid_miles()
        result = value * MILES_FACTOR
        self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):
        """Ensures number is a float before being converted or incremented"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


ConvertMilesApp().run()
