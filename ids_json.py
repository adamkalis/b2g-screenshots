import os
import json
import re
import sys

# Check if there is "#" character at the start of each line and
# if there is not, then reads "string1 = string2" pattern and
# returns a list with tuples (string1, string2) of each line
regex = re.compile("^(?!#)(.+?)\s*=\s*(.+?)$",re.MULTILINE)
strings = {}

if len(sys.argv) > 1:
  locale = sys.argv[1]
else:
  locale = ''

for root,dirs,files in os.walk('locales/' + locale):
  for file_name in files:
    if file_name.endswith('.properties'):
      file_stream = open(os.path.join(root,file_name),'r')
      l10n_strings = regex.findall(file_stream.read())
      file_stream.close()
      for string in l10n_strings:
        if strings.has_key(string[0]):
          strings[string[0]] = [{'id': string[0], 'l10n': string[1], 'position': os.path.join(root,file_name), 'screenshots': []}] + strings[string[0]]
        else:
          strings[string[0]] = [{'id': string[0], 'l10n': string[1], 'position': os.path.join(root,file_name), 'screenshots': []}]

json_file = open('locales/' + locale + '/db.json','w')
json.dump(strings, json_file, indent = 2)
json_file.close()
