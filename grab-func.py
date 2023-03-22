##
# This code reads source document and creates a dummy file for ac object.
# Chat GPT generated this code by my lead :) Please judge only it (or he 😆)
# Not bad at the end though

import re
import importlib.util
import sys
import os


def import_from_path(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


# Get the path of the `ac-stubs` directory
ac_stubs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ac-stubs")

# Import the `ac` module from the `__init__.py` file within the `ac-stubs` directory
ac = import_from_path("ac", os.path.join(ac_stubs_dir, "__init__.py"))


def extract_functions(text):
    # Find all function definitions starting with "ac."
    pattern = r'^\s*-\s?ac\.(.*?)\((.*?)\)'
    matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
    # Create a dictionary to store the function names and their arguments
    ac_functions = {}
    for function_match in matches:
        function_name = function_match[0]

        # fix incorrect name of function in the document
        if 'addInputText' == function_name:
            function_name = 'addTextInput'

        function_args = function_match[1]
        # Extract the arguments and their default values
        args_dict = extract_function_args(function_args)
        # Add the function to the ac_functions dictionary
        ac_functions[function_name] = args_dict
    return ac_functions


def extract_function_args(function_args):
    # Remove any spaces in the arguments string and the triangle brackets
    function_args = function_args \
        .replace(' ', '') \
        .replace('<', '') \
        .replace('>', '')

    # Fix type in a variable name
    function_args = function_args \
        .replace('CONTROLO_IDENTIFIER', 'CONTROL_IDENTIFIER')

    # Split the arguments string by commas
    args_list = function_args.split(',')
    # Create a dictionary to store the function arguments and their default values
    args_dict = {}
    # Loop through each argument and set its default value to None if it is optional
    for arg in args_list:
        # check for optional comment in the argument
        optional = False
        if '/*OPTIONAL*/' in arg:
            # Remove the optional comment and add the default value None
            arg = arg.replace('/*OPTIONAL*/', '')
            optional = True
        # Split the argument by colon to get its name and type
        arg_name_type = arg.split(':')
        arg_name = arg_name_type[0]
        # check if argument name is in camelCase
        if re.search('[a-z]+[A-Z]+', arg_name):
            # convert camelCase to underscore_case
            arg_name = re.sub('(.)([a-z])([A-Z]+)', r'\1\2_\3', arg_name)
        arg_name = arg_name.lower()
        # if optional, set default value to None
        if optional:
            args_dict[arg_name] = None
        else:
            args_dict[arg_name] = arg_name_type[1] if len(arg_name_type) > 1 else None
    return args_dict


def create_stub_functions(ac_functions):
    function_str = ''
    for function_name, function_args in ac_functions.items():

        if hasattr(ac, function_name):
            continue

        # Convert function args dictionary into a list of argument strings
        args_list = []
        for arg_name, default_value in function_args.items():
            if default_value is None:
                arg_str = arg_name
            else:
                arg_str = f"{arg_name}={default_value}"
            args_list.append(arg_str)
        args_str = ', '.join(args_list)
        # Generate the function string and add it to the ac object
        function_str += f'\n\ndef {function_name}({args_str}): ...\n'
    return function_str


def write_functions(content: str):
    _file = 'ac-stubs/__init__.py'

    # Check if the file exists
    if os.path.exists(_file):
        file_mode = 'a'  # Append mode if the file exists
    else:
        file_mode = 'w'  # Write mode if the file doesn't exist

    # Write or append the content from ac_functions_str if it's not empty
    if content:
        with open(_file, file_mode) as _file:
            _file.write(content)
    else:
        print("No content to write or append.")


if __name__ == '__main__':
    # Open the PDF file and extract the text
    with open('ACPythonDoc.txt', 'r') as file:
        input_text = file.read()

    # Extract the AC functions and their arguments from the text
    ac_functions = extract_functions(input_text)

    # Create dummy functions for the AC module
    write_functions(
        create_stub_functions(ac_functions)
    )
