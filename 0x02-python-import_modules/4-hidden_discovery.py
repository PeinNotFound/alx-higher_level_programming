#!/usr/bin/python3

import dis
import types
import importlib.util

def list_module_names(module_file):
    spec = importlib.util.spec_from_file_location("hidden_4", module_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = dir(module)
    names.sort()

    for name in names:
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    list_module_names('/home/pexn/Downloads')
