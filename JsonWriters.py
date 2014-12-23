from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
import os


class BaseSectionWriter(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def write_section(self, section):
        pass

    @abstractmethod
    def close(self):
        pass


class ArrayWriter(BaseSectionWriter):

    def __init__(self, filename):
        super(BaseSectionWriter, self).__init__()
        self.repeatingSection = False

        if os.path.isfile(filename):
            os.remove(filename)

        self.file = open(filename, 'w')
        self.write('[')

    def close(self):
        self.write(']')
        self.file.close()

    def write_section(self, section):
        if self.repeatingSection:
            self.write(',')
        else:
            self.repeatingSection = True

        self.write('{{\n\t"SectionName":"{}",\n\t"data":['.format(section.name.replace('"', '\\"')))
        repeatingproperties = False
        for k, v in section.properties.items():
            if repeatingproperties:
                print(',')
            else:
                repeatingproperties = True

            self.write('{{\n\t\t"name":"{}",\n\t\t"value":"{}"\n\t}}'.format(k.strip().replace('"', '\\"'), v.strip().replace('"', '\\"')))

        self.write(']\n}')

    def write(self, string):
        self.file.write(string)
        print(string)


@contextmanager
def create_writer(writertype, filename):

    if writertype == 0:
        writer = ArrayWriter(filename)
    else:
        writer = ObjectWriter(filename)

    try:
        yield writer
    finally:
        writer.close()



class ObjectWriter(BaseSectionWriter):

    def __init__(self, filename):
        super(BaseSectionWriter, self).__init__()

    def close(self):
        print('closed')

    def write_section(self, section):
        print(section)