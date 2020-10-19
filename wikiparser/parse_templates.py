import wikitextparser as wtp


def clean_template_string(string):
    string = string.replace('\n', '')
    return ' '.join([token for token in string.split() if token != ''])


def parse_template(template):
    is_nested = template.nesting_level != 1
    if not is_nested:
        template_dict = {
            'name': clean_template_string(template.name)
        }
        for arg in template.arguments:
            arg_key = clean_template_string(arg.name)
            arg_value = clean_template_string(wtp.parse(arg.value).plain_text())
            template_dict[arg_key] = arg_value
        return template_dict





# def parse_args(args):
#     arg_list = [str(arg).replace('|', '').split('=') for arg in args]
#     arg_list = [(arg[0], wtp.parse(arg[1]).plain_text().replace('\n', '')) for arg in arg_list if len(arg) > 1]
#     arg_list = [arg for arg in arg_list if len(arg[1]) > 0]
#     parsed_args = [{
#         'key': remove_multiple_spaces(arg[0]),
#         'value': remove_multiple_spaces(arg[1])
#     } for arg in arg_list]
#     return parsed_args
#
#
# def templates_to_args(templates):
#     args = [parse_template(template) for template in templates]
#     args = [arg for arg in args if arg]
#     return args