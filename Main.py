import argparse
import INISection
import sys
import JsonWriters

parser = argparse.ArgumentParser(description='Converts an ini file into a json object.')
parser.add_argument('input', help='The .ini file to transform into a json object e.g. ./input.ini')
parser.add_argument('-p', '--parseType', help='1 parses to an object, 0 parses to an array.', type=int, choices=[0, 1],
                    default=0)
args = parser.parse_args()

with open(args.input) as file:
    out_name = args.input + ".json"

    with JsonWriters.create_writer(args.parseType, out_name) as writer:

        #define a variable to hold the current section
        section = None
        for line in file:
            line = line.strip()
            if line.__len__() == 0:
                continue

            if line.startswith('['):
                #new section
                #send the old section off to be printed
                if section is not None:
                    writer.write_section(section)

                section = INISection.Section(line.strip('[]'))
            elif line.startswith(';') or line.startswith('//') or line.startswith('#'):
                continue
            else:
                #this is a property HOPEFULLY
                if section is None:
                    print('Invalid ini file, properties declared before section header.')
                    sys.exit()
                split_val = line.split('=')
                section.add_property(split_val[0], split_val[1])