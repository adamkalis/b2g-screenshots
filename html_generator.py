from scripts.toolkit import get_db
import os

#HTML
htmlfile = open('results/index.html', 'w')
htmlfile.write('<!doctype html>\n')
htmlfile.write('<html>\n')
htmlfile.write('  <head>\n')
htmlfile.write('    <title>Locales vs Apps</title>\n')
htmlfile.write('    <link rel="stylesheet" type="text/css" href="style.css" />\n')
htmlfile.write('  </head>\n')
htmlfile.write('  <body>\n')
htmlfile.write('')
htmlfile.write('    <table>\n')
htmlfile.write('      <tbody>\n')
htmlfile.write('        <tr>\n')
htmlfile.write('          <th></th>\n')
htmlfile.write('')

apps = {}

for locale in os.listdir('results/screenshots'):
  htmlfile.write("          <th class='locales'>" + locale + "</th>\n")
  db = get_db(locale)
  for i in db:
    for j in db[i]:
      if j['screenshots']:
        for k in j['screenshots']:
          if apps.has_key(k['path']):
            if apps[k['path']].has_key(locale):
              if not apps[k['path']][locale]['changed']:
                apps[k['path']][locale]['changed'] = k['changed']
              apps[k['path']][locale]['ids'].append((k['id'], k['changed']))
            else:
              apps[k['path']].update({locale: {'changed': k['changed'], 'ids': [(k['id'], k['changed'])]}})
          else:
            apps.update({k['path']: {locale: {'changed': k['changed'], 'ids': [(k['id'], k['changed'])]}}})

htmlfile.write('        </tr>\n')

for app in apps:
  htmlfile.write('        <tr>\n')
  htmlfile.write("          <th class='apps'>" + app + "</th>\n")
  for locale in os.listdir('results/screenshots'):
    if apps[app][locale]['changed']:
      htmlfile.write("          <td class='changed'><a href=" + app.replace("/","_") + "_" + locale + ".html>CHANGED</a></td>\n")
    else:
      htmlfile.write("          <td class='ok'><a href=" + app.replace("/","_") + "_" + locale + ".html>OK</a></td>\n")

    htmlappfile = open("results/" + app.replace('/','_') + '_' + locale + '.html', 'w')
    htmlappfile.write('<!doctype html>\n')
    htmlappfile.write('<html>\n')
    htmlappfile.write('  <head>\n')
    htmlappfile.write('    <title>Screenshots for ' + app + ' in ' + locale + '</title>\n')
    htmlappfile.write('    <link rel="stylesheet" type="text/css" href="style.css" />\n')
    htmlappfile.write('  </head>\n')
    htmlappfile.write('  <body>\n')
    htmlappfile.write('')
    htmlappfile.write('    <table>\n')
    htmlappfile.write('      <tbody>\n')
    htmlappfile.write('        <tr>\n')
    htmlappfile.write('          <th>l10n ID</th>\n')
    htmlappfile.write('          <th>New</th>\n')
    htmlappfile.write('          <th>Old</th>\n')
    htmlappfile.write('          <th>Diff</th>\n')
    htmlappfile.write('        </tr>\n')
    for screenshot in apps[app][locale]['ids']:
      if screenshot[1]:
        htmlappfile.write("        <tr class='changed'>\n")
      else:
        htmlappfile.write("        <tr class='ok'>\n")
      htmlappfile.write("          <td class='id'>" + screenshot[0] + "</td>\n")
      htmlappfile.write("          <td class='new'>\n")
      htmlappfile.write("            <a href='screenshots/" + locale + "/" + app + "/" + screenshot[0] + ".jpeg'>\n")
      htmlappfile.write("              <img src='screenshots/" + locale + "/" + app + "/" + screenshot[0] + ".jpeg'/>\n")
      htmlappfile.write("            </a>\n")
      htmlappfile.write("          </td>\n")
      htmlappfile.write("          <td class='old'>\n")
      htmlappfile.write("            <a href='screenshots/" + locale + "/" + app + "/" + screenshot[0] + ".old.jpeg'>\n")
      htmlappfile.write("              <img src='screenshots/" + locale + "/" + app + "/" + screenshot[0] + ".old.jpeg'/>\n")
      htmlappfile.write("            </a>\n")
      htmlappfile.write("          </td>\n")
      htmlappfile.write("          <td class='diff'>\n")
      if screenshot[1]:
        htmlappfile.write("            <a href='screenshots/" + locale + "/" + app + "/" + screenshot[0] + ".diff.jpeg'>\n")
        htmlappfile.write("              <img src='screenshots/" + locale + "/" + app + "/" + screenshot[0] + ".diff.jpeg'/>\n")
        htmlappfile.write("            </a>\n")
      htmlappfile.write("          </td>\n")
      htmlappfile.write("        </tr>\n")
    htmlappfile.write('      </tbody>\n')
    htmlappfile.write('    </table>\n')
    htmlappfile.write('  </body>\n')
    htmlappfile.write('</html>')
    htmlappfile.close()
  htmlfile.write('        </tr>\n')

htmlfile.write('      </tbody>\n')
htmlfile.write('    </table>\n')
htmlfile.write('  </body>\n')
htmlfile.write('</html>')
htmlfile.close()

#CSS
cssfile = open('results/style.css', 'w')

cssfile.write('table th{\n')
cssfile.write('    background-color: #FFFF99;\n')
cssfile.write('    font-size: large;\n')
cssfile.write('    border: 1px solid black;\n')
cssfile.write('}\n')
cssfile.write('table td{\n')
cssfile.write('    border: 1px solid black;\n')
cssfile.write('}\n')
cssfile.write('table {\n')
cssfile.write('    width: 100%;\n')
cssfile.write('    text-align: center;\n')
cssfile.write('    border: 2px solid black;\n')
cssfile.write('    border-collapse: collapse;\n')
cssfile.write('}\n')
cssfile.write('table .changed {\n')
cssfile.write('    background-color: #FF0000;\n')
cssfile.write('    font-weight: bold;\n')
cssfile.write('    border: 2px solid black;\n')
cssfile.write('}\n')
cssfile.write('table .ok {\n')
cssfile.write('    background-color: #00FF00;\n')
cssfile.write('    font-weight: bold;\n')
cssfile.write('}\n')
cssfile.write('table .id {\n')
cssfile.write('    font-weight: bold;\n')
cssfile.write('}\n')
cssfile.write('img{\n')
cssfile.write('    width: 40%;\n')
cssfile.write('}\n')

cssfile.close()
