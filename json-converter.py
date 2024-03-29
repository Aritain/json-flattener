#!/usr/bin/python3

import json
import sys
import getopt


HELP='Usage json_converter.py -f <path> -m <pretty(default)/raw>'

class ProcessJson:
    def __init__(self):
        self.max_key_lenght = 0
        self.pretty_dict = []

    def flatten_dict(self, dd, separator='.'):
        out = {}

        def flatten(dd, prevLine=''):
        # If the Nested key-value
        # pair is of dict type
            if type(dd) is dict:
                for elem in dd:
                    flatten(dd[elem], prevLine + elem + separator)

        # If the Nested key-value
        # pair is of list type
            elif type(dd) is list:
                i = 0
                for elem in dd:
                    flatten(elem, prevLine + str(i) + separator)
                    i += 1
            else:
                out[prevLine[:-1]] = dd

        flatten(dd)
        return out

    def max_element_lenght(self):
        for key in self.dd:
            if len(key) > self.max_key_lenght:
                self.max_key_lenght = len(key)

    def format_dict(self):
        self.pretty_dict.append('')
        for key, value in self.dd.items():
            if self.mode == "pretty":
                additional_spaces=''
                if len(key) < self.max_key_lenght:
                    additional_spaces=' '*(self.max_key_lenght-len(key))
                self.pretty_dict.append(f'{key}{additional_spaces} = {value}')
            else:
                self.pretty_dict.append(f'{key} = {value}')
        self.pretty_dict.append('')

    def get_pretty_dict(self, dd, mode):
        self.mode = mode
        self.dd = dd
        self.dd = self.flatten_dict(self.dd)
        self.max_element_lenght()
        self.format_dict()
        return (self.pretty_dict)


def help_n_quit():
    print(HELP)
    sys.exit(1)

def parse_arguments():
    filename = ''
    mode = 'pretty'
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:m:")
    except getopt.GetoptError:
        help_n_quit()

    for opt, arg in opts:
        if opt == '-h':
            help_n_quit()
        elif opt == '-m':
            mode = arg
            if mode not in ("pretty", "raw"):
                help_n_quit()
        elif opt == '-f':
            filename = arg
        else:
            help_n_quit()

    if len(opts) == 0 or filename == '':
        help_n_quit()

    return filename, mode


def main():
    filename, mode = parse_arguments()
    with open(filename) as json_file:
        data = json.load(json_file)

    PJ = ProcessJson()

    for elem in PJ.get_pretty_dict(data, mode):
        print(elem)

main()

