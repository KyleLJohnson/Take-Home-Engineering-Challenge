"""
File containing the Menu class
"""

class Menu:
    """
    Small class that creates a menu object given a list of options
    """
    def __init__(self, menu_title: str = "MAIN MENU", menu_options: dict = None, menu_width: int = 50):
        """
        Constructs the basic object given a dictionary of menu_options
        :param menu_options:
        """
        if menu_options is None:
            menu_options = []

        self.menu_title = menu_title
        self.menu_width = menu_width
        self.menu_options = menu_options
        self.dispatch_map = {}

    def display_menu(self):
        """
        Prints out all the menu items in the dictionary along with their descriptions
        :return:
        """
        half_length = int((self.menu_width - len(self.menu_title) - 2) / 2)
        print('\n')
        print(f"{'*' * half_length} {self.menu_title} {'*' * half_length}")
        for option_key, option_value in self.menu_options.items():
            print(f"\t{option_key}) {option_value}")
        print(f"{'*' * ((half_length * 2) + 2 + len(self.menu_title))}")
        #print('\n')

    def is_valid_input(self, raw_input: str) -> bool:
        """
        Method validates that raw_input is a valid option in menu_options
        :param raw_input: raw string to compare against all menu_options
        :return:
        """
        result = False
        if raw_input in self.menu_options:
            result = True
        return result

    def add_dispatch_function(self, new_function):
        """
        Neat little method that adds a function reference to the dispatch table as a value for a key
        :param new_function: function reference/address
        :return:
        """
        index = len(self.dispatch_map.keys())
        self.dispatch_map.update({index: new_function})
