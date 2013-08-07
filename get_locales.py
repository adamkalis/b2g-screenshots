import httplib
import re


regex = re.compile("^/gaia-l10n/(.+)/$",re.MULTILINE)


conn = httplib.HTTPSConnection("hg.mozilla.org")
conn.request("GET", "/gaia-l10n/?style=raw")
response = conn.getresponse()

all_locales = ''

if response.status == 200:
  locales = regex.findall(response.read())
for locale in locales:
  all_locales += locale + ' '

print all_locales
