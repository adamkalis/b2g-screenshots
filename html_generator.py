from scripts.toolkit import get_db
import os

#HTML
file = open('html_results/index.html', 'w')
file.write('<!doctype html>\n')
file.write('<html>\n')
file.write('  <head>\n')
file.write('    <title>Locales vs Apps</title>\n')
file.write('    <link rel="stylesheet" type="text/css" href="index.css" />\n')
file.write('  </head>\n')
file.write('  <body>\n')
file.write('')
file.write('    <table>\n')
file.write('      <tbody>\n')
file.write('        <tr>\n')
file.write('          <th></th>\n')
file.write('')

apps = {}

for locale in os.listdir('screenshots'):
  file.write("          <th class='locales'>" + locale + "</th>\n")
  db = get_db(locale)
  for i in db:
    for j in db[i]:
      if j['screenshots']:
        for k in j['screenshots']:
          if apps.has_key(k['path']):
            if [locale, True] in apps[k['path']] or [locale, False] in apps[k['path']]:
              for app in apps[k['path']]:
                if app[0] == locale and not app[1]:
                  app[1] = k['changed']
            else:
              apps[k['path']].append([locale, k['changed']])
          else:
            apps[k['path']] = [[locale, k['changed']]]

file.write('        </tr>\n')
file.write('        <tr>\n')

for app in apps:
  file.write("          <th class='apps'>" + app + "</th>\n")
  for locale in apps[app]:
    if locale[1]:
      file.write("          <td class='changed'>CHANGED</td>\n")
    else:
      file.write("          <td class='ok'>OK</td>\n")

file.write('        </tr>\n')
file.write('      </tbody>\n')
file.write('    </table>\n')
file.write('  </body>\n')
file.write('</html>')
file.close()

#CSS
file = open('html_results/index.css', 'w')

file.write('table th{\n')
file.write('    background-color: #FFFF99;\n')
file.write('    font-size: large;\n')
file.write('    border: 1px solid black;\n')
file.write('}\n')
file.write('table td{\n')
file.write('    border: 1px solid black;\n')
file.write('}\n')
file.write('table {\n')
file.write('    width: 100%;\n')
file.write('    text-align: center;\n')
file.write('    border: 2px solid black;\n')
file.write('    border-collapse: collapse;\n')
file.write('}\n')
file.write('table .changed {\n')
file.write('    background-color: #FF0000;\n')
file.write('    font-weight: bold;\n')
file.write('    border: 2px solid black;\n')
file.write('}\n')
file.write('table .ok {\n')
file.write('    background-color: #00FF00;\n')
file.write('    font-weight: bold;\n')
file.write('}\n')

file.close()
