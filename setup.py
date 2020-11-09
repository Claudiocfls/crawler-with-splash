import os
import re
import time

env_var_regex = r'(?<=\{{)(.*?)(?=\}})'
replace_regex = r'\{{.*\}}'

tag = None

# predefined variables
def get_variable_value(variable):
    global tag
    value = os.environ.get(env_to_replace, None)
    if not value:
        return None
    if variable == 'TAG':
        value += '_{}'.format(int(time.time()))
        tag = value
    return value

print("[info] Starting templating...")

try:
    import generic_crawler.settings
    print("[warn] A previous settings file was found. It will be removed.")
    os.system("rm generic_crawler/settings.py")
except:
    print("[info] None settings file was found.")

template_file = open('template_settings.py', 'r')
template_file_lines = template_file.readlines()

templated_file = open('generic_crawler/settings.py', 'a+')

for line in template_file_lines:
    new_line = line
    if line[0] != '#': # ignore comments with #
        groups = re.findall(env_var_regex, line)
        if groups:
            for env_to_replace in groups:
                value = get_variable_value(env_to_replace)
                if not value:
                    raise Exception('Environment variable not found: "{}"'.format(env_to_replace))
                replacer = re.compile("{}".format("{{"+env_to_replace+"}}"))
                print("{}: {}".format(env_to_replace, value))
                new_line = replacer.sub(value, new_line)
    templated_file.write('{}'.format(new_line))

template_file.close()
templated_file.close()

# create initial files
log_file = '{}/{}'.format(os.environ.get('TARGET_DIR'), tag)
try:
    os.makedirs(log_file)
except:
    pass

with open('{}/logs.txt'.format(log_file), 'w') as file:
    file.write('First log...\n')

print("[info] Templating finished.")