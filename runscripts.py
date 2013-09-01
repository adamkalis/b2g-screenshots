from scripts import *
import sys
import getopt

locale = ''
apps_list = []
properties_files = []
data_ids = []
device_flags = {
  "sim": None,
  "no-sim": None,
  "wifi": None,
  "no-wifi": None,
  "sd-card": None,
  "no-sdcard": None,
  "3g": None,
  "no-3g": None
}

try:
  myopts, args = getopt.getopt(sys.argv[1:],"l:a:p:i:f:")
except getopt.GetoptError as e:
  print (str(e))
  print("Usage: %s -l locale [-a apps_list_sbc] [-p properties_files_sbc] [-i data_ids_sbc] [-f flags_sbc]" % sys.argv[0])
  print("\"sbc\" means \"seperated by comma\"")
  print("example: %s -l el -a ftu,browser -f no-sim,wifi" % sys.argv[0])
  sys.exit(2)

for o, a in myopts:
  if o == '-l':
    locale = a
  elif o == '-a':
    apps_list = a.split(',')
  elif o == '-p':
    properties_files = a
  elif o == '-i':
    data_ids = a.split(',')
  elif o == '-f':
    for flag in a.split(','):
      if flag == 'sim' and not device_flags['no-sim']:
        device_flags['sim'] = True
        device_flags['no-sim'] = False
      elif flag == 'no-sim' and not device_flags['sim']:
        device_flags['sim'] = False
        device_flags['no-sim'] = True
      elif flag == 'wifi' and not device_flags['no-wifi']:
        device_flags['wifi'] = True
        device_flags['no-wifi'] = False
      elif flag == 'no-wifi' and not device_flags['wifi']:
        device_flags['wifi'] = False
        device_flags['no-wifi'] = True
      elif flag == 'sd-card' and not device_flags['no-sd-card']:
        device_flags['sd-card'] = True
        device_flags['no-sd-card'] = False
      elif flag == 'no-sd-card' and not device_flags['sd-card']:
        device_flags['sd-card'] = False
        device_flags['no-sdcard'] = True
      elif flag == '3g' and not device_flags['no-3g']:
        device_flags['3g'] = True
        device_flags['no-3g'] = False
      elif flag == 'no-3g' and not device_flags['3g']:
        device_flags['3g'] = False
        device_flags['no-3g'] = True
      else:
        #TO DO raise error
        print 'flag ' + flag + ' is ignored (reason: "Not valid" or "Opposite flag has been set")!'
    if device_flags['sim'] == None:
      device_flags['sim'] = False
      device_flags['no-sim'] = True
    elif device_flags['wifi'] == None:
      device_flags['wifi'] = False
      device_flags['no-wifi'] = True
    elif device_flags['sd-card'] == None:
      device_flags['sd-card'] = False
      device_flags['no-sdcard'] = True
    elif device_flags['3g'] == None:
      device_flags['3g'] = False
      device_flags['no-3g'] = True

apps_dict = {
  'ftu': apps.communications.ftu.ftu
}


if 'ftu' in apps_list:
  apps_dict['ftu'](locale, device_flags)
