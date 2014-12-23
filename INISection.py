class Section:
    """Class that represents on an INI section and it's properties"""

    def __init__(self, section_name):
        assert isinstance(section_name, str)
        self.name = section_name
        self.properties = dict()

    def add_property(self, name, value):
        """
        Adds a property to the section
        :param name: The property name
        :param value: The property value
        """
        if name and isinstance(name, str):
            self.properties[name] = value

    def __str__(self):
        s = '[' + self.name + ']'
        for k, v in self.properties.items():
            s += '\n' + k + '=' + v
        return s

    def __repr__(self):
        s = '[' + self.name + ']'
        for k, v in self.properties.items():
            s += '\n' + k + '=' + v
        return s