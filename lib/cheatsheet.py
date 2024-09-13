import logging
import os

from datetime import datetime

from talon import Module, actions, registry




global lines_written
global headerlines
headerlines=0
lines_written = 0




# repeat the above but in html format
def user_list_to_html_table(file, list_name,sort_by='key',left_pad_value=0):

    global lines_written


    command_list_from_registry = registry.lists[list_name][0].items()

    if left_pad_value>0:
        #left pad the value with spaces

        command_list_from_registry = [(key, value.rjust(left_pad_value)) for key, value in command_list_from_registry]


    #sort the commands by the key
    if sort_by=='key' or sort_by=='value':
        command_list = sort_command_list(command_list_from_registry,sort_by)
    else:
        #build the command list using the ordered indexes
        command_list = []
        for key in sort_by.split(','):
            for item_key, item_value in command_list_from_registry:
                if item_key == key:
                    command_list.append((item_key, item_value))



    write_page_break_if_needed(file, len(command_list))

    commandGroup = list_name.replace('user.', '').upper()
    # Append 'S' to Command Group if it doesn't already end with 'S'.
    if commandGroup[-1] != "S":
        commandGroup = commandGroup + "S"
    file.write(f"<h1>{commandGroup}</h1>\n\n")
    # convert this to a two column table
    file.write("<table>\n")
    file.write("<tr><th>Input</th><th>Result</th></tr>\n")
    rowCount = 0
    rows_written=0
    for key, value in command_list:
        rowCount += 1
        rows_written += 1
        lines_written += 1
        if ((rowCount > 4 and key[:2] != previousRule[:2]) and not rows_written==len(command_list)):
            file.write("<tr class=blank><td>&nbsp;</td><td></td></tr>\n")
            rowCount = 0
        previousRule = key
        file.write(f"<tr class=context><td>{key}</td><td>{value}</td></tr>\n")
    file.write("</table>\n\n")

    file.write("\n\n")

def user_list_to_html_table_formatters_nonprogramatically(file, list_name,sort_by='key'):
    global lines_written

    # from talon import actions
    # from core.text import formatters
    #from core.text import formatters  #depends  on source code from https://github.com/talonhub/community


    command_list = registry.lists[list_name][0].items()

    #sort the commands by the key
    command_list = sort_command_list(command_list,sort_by)


    # override the command list with a non programmatically generated list as I can't get this working with formatters.Actions.formatted_text(value+" Example", value)
    command_list = [
        ('all cap', 'EXAMPLE TEXT'),
        ('all down', 'example text'),
        ('camel', 'exampleText'),
        ('dotted', 'example.text'),
        ('dub string', '"example text"'),
        ('dunder', '__example__text'),
        ('hammer', 'ExampleText'),
        ('kebab', 'example-text'),
        ('packed', 'example::text'),
        ('padded', '[space]example text[space]'),
        ('slasher', '/example/text'),
        ('smash', 'exampletext'),
        ('snake', 'example_text'),
        ('string', '\'example text\''),
        ('sentence', 'Example text'),
        ('title', 'Example Text')
    ]




    write_page_break_if_needed(file, len(command_list))

    commandGroup = list_name.replace('user.', '').upper()
    # Append 'S' to Command Group if it doesn't already end with 'S'.
    if commandGroup[-1] != "S":
        commandGroup = commandGroup + "S"
    file.write(f"<h1>{commandGroup}</h1>\n\n")
    # convert this to a two column table
    file.write("<table>\n")
    file.write("<tr><th>Input</th><th>Result</th></tr>\n")
    rowCount = 0
    rows_written=0
    for key, value in command_list:
        rowCount += 1
        rows_written += 1
        lines_written += 1
        if ((rowCount > 4 and key[:2] != previousRule[:2]) and not rows_written==len(command_list)):
            file.write("<tr class=blank><td>&nbsp;</td><td></td></tr>\n")
            rowCount = 0
        previousRule = key

        #STUCK Here as a can't import formatters  as a module
        # value=formatters.Actions.formatted_text(value+" Example", value)
        #will Need to For 'padded' adding &nbsp;  around the value


        file.write(f"<tr class=context><td>{key}</td><td>{value}</td></tr>\n")
    file.write("</table>\n\n")

    file.write("\n\n")

def user_list_to_html_table_alphabet(file, list_name,sort_by='value'):
    global lines_written

    command_list = registry.lists[list_name][0].items()

    #sort the commands by the key
    command_list = sort_command_list(command_list,sort_by)



    write_page_break_if_needed(file, len(command_list))

    commandGroup = list_name.replace('user.', '').upper()
    # Append 'S' to Command Group if it doesn't already end with 'S'.
    if commandGroup[-1] != "S":
        commandGroup = commandGroup + "S"
    file.write(f"<h1>{commandGroup}</h1>\n\n")
    # convert this to a two column table
    file.write("<table>\n")
    file.write("<tr><th>Letter</th><th>Word</th></tr>\n")
    rowCount = 0
    rows_written=0
    for key, value in command_list:
        rowCount += 1
        rows_written += 1
        lines_written += 1
        if ((rowCount > 4 and value[:2] != previousRule[:2]) and not rows_written==len(command_list)):
            file.write("<tr class=blank><td>&nbsp;</td><td></td></tr>\n")
            rowCount = 0
        previousRule = value
        file.write(f"<tr class=context><td>{value}</td><td>{key}</td></tr>\n")
    file.write("</table>\n\n")

    file.write("\n\n")






def sort_command_list(command_list, sort_by='key'):
    """Sorts the command list by key or value"""
    if sort_by == 'key':
        return sorted(command_list)
    elif sort_by == 'value':
        return sorted(command_list, key=lambda x: x[1])
    else:
        raise ValueError("sort_by parameter must be either 'key' or 'value'")

def write_context_commands(key, output_file, commands):
    global lines_written
    global headerlines


    if "private" in key: # don't print out private commands
        return


    # write out each command and it's implementation
    write_page_break_if_needed(output_file, len(commands))
    pretty_print_context_name(output_file, key)
    headerlines += 1

    output_file.write("<table class='contexts'>\n")
    output_file.write("<tr><th>Input</th><th>Result</th></tr>\n")
    output_file.write("")
    #sort the commands by the rule
    commands = dict(sorted(commands.items()))
    #sorted by item
    # commands = {k: v for k, v in sorted(commands.items(), key=lambda item: item[1].target.code)}

    previousRule= ""
    rowCount = 0
    rows_written=0
    for key in commands:
        rowCount += 1
        rows_written += 1
        try:
            rule = escapeHtml(commands[key].rule.rule)
            implementation = escapeHtml(commands[key].target.code).replace("\n", "<br />")
        except Exception:
            continue





        #emove any text following a hash # symbol if the length > 20 chqars
        if len(implementation) > 20:
           implementation = implementation.split('#')[0]


        if ((rowCount > 4 and rule[:rowCount] != previousRule[:rowCount]) and not rows_written==len(commands)):
            output_file.write("<tr class=blank><td>&nbsp;</td><td></td></tr>\n")
            rowCount = 0
        previousRule = rule
        output_file.write(
            f"<tr class=context><td>{rule}</td><td>{implementation}</td></tr>\n")


        lines_written += 1

    output_file.write("</table>\n\n")

def escapeHtml(htmltobe):
    return htmltobe.replace("<", "&lt;").replace(">", "&gt;")


def pretty_print_context_name(file, name):
    ## The logic here is intended to only print from talon files that have actual voice commands.
    splits = name.split(".")
    index = -1



    os = ""

    if "mac" in name:
        os = "mac"
    if "win" in name:
        os = "win"
    if "linux" in name:
        os = "linux"

    if "talon" in splits[index]:
        index = -2
        short_name = splits[index].replace("_", " ")
    else:
        short_name = splits[index].replace("_", " ")

    if "mac" == short_name or "win" == short_name or "linux" == short_name:
        index = index - 1
        short_name = splits[index].replace("_", " ")

    global lines_written

    file.write("<h2>" + short_name.upper() + "</h2>")


def write_page_break_if_needed(file, size_of_next_list):
    global lines_written
    global headerlines
    if lines_written+size_of_next_list + headerlines*3 > 36:
        file.write('<p style="page-break-after: always;"/>')
        lines_written = 0
        headerlines = 0


mod = Module()


def write_html_header(file):
    file.write("""<!DOCTYPE html>
        <html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
        <head>
          <meta charset="utf-8" />
          <meta name="generator" content="pandoc" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
          <title>cheatsheet</title>
          <style>
            code{white-space: pre-wrap;}
            span.smallcaps{font-variant: small-caps;}
            span.underline{text-decoration: underline;}
            div.column{display: inline-block; vertical-align: top; width: 50%;}
            div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
            ul.task-list{list-style: none;}
          </style>
          <link rel="stylesheet" href="cheatsheet.css" />
        </head>
        <body>""")


@mod.action_class
class user_actions:
    def cheatsheet():
        """Print out a sheet of talon commands"""
        # open file
        logging.info(
            f"generating cheat sheet in {os.path.dirname(os.path.realpath(__file__))}"
        )
        this_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(this_dir, 'cheat_sheet.html')
        file = open(file_path, "w")
        write_html_header(file)
        file.write(f"<h1 align=center>Talon Cheat Sheet</h1>\n\n")
        file.write(f"<p align=center>Generated on: {datetime.now()}</p>\n\n")




        write_alphabet(file)
        write_formatters(file)
        write_punctuation(file)
        write_symbol(file)

        write_special(file)
        write_modifiers(file)

        write_arrow(file)
        write_function(file)
        write_numbers(file)



        file.write('<p style="page-break-after: always;"/>')
        lines_written = 0
        # print out all the commands in all of the contexts

        list_of_contexts = dict(registry.contexts.items())
        sorted_keys = sorted(list_of_contexts)

        for key in sorted_keys:
            value = list_of_contexts[key]
            commands = value.commands  # Get all the commands from a context
            if len(commands) > 0:

                write_context_commands(key, file, commands)

        file.write(f"<h1 align=center>End of Talon Cheat Sheet</h1>\n\n")
        file.write("</body></html>")
        file.close()



def write_alphabet(file):
    user_list_to_html_table_alphabet(file, 'user.letter', sort_by='value')


def write_numbers(file):
    user_list_to_html_table(file, 'user.number_key', sort_by='value')


def write_modifiers(file):
    user_list_to_html_table(file, 'user.modifier_key')


def write_special(file):
    user_list_to_html_table(file, 'user.special_key')


def write_symbol(file):
    user_list_to_html_table(file, 'user.symbol_key')


def write_arrow(file):
    user_list_to_html_table(file, 'user.arrow_key', sort_by='up,down,left,right')


def write_punctuation(file):
    user_list_to_html_table(file, 'user.punctuation')


def write_function(file):
    user_list_to_html_table(file, 'user.function_key', sort_by='value',left_pad_value=3)


def write_formatters(file):
    user_list_to_html_table_formatters_nonprogramatically(file, 'user.formatters')
