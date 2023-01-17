from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

NEW_COLOUR = (0, 1, 0, 1)  # RGBA for green
ALTERNATIVE_COLOUR = (1, 0, 10, 1)  # RGBA for blue


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # dictionary of names: labels
        self.name_to_label = {"Bob Brown": "male", "Cat Cyan": "female", "Oren Ochre": "female", "hello": "there"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_label:
            # create a button for each data entry, specifying the text
            temp_button = Button(text=name)
            # set the button's background colour
            temp_button.background_color = ALTERNATIVE_COLOUR
            # add the button to the "entries_box" layout widget
            self.root.ids.main.add_widget(temp_button)


DynamicLabelsApp().run()
