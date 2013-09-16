import sys
import os
import json
import base64
from PIL import Image
from PIL import ImageChops

def get_db(locale):
  json_file = open('locales/' + locale + '/db.json')
  db = json.load(json_file)
  json_file.close()
  return db

def set_db(locale, db):
  json_file = open('locales/' + locale + '/db.json', 'w')
  json.dump(db, json_file, indent = 2)
  json_file.close()

def check_duplicate (db, data_id, data_l10n, app, app_categ, screenshot_entry):
  found = False
  for entry in db[data_id]:
    if entry['l10n'] == data_l10n:
      if app in entry['position']:
        for screenshot in entry['screenshots']:
          if screenshot['id'] == screenshot_entry['id']:
            found = True
            screenshot['changed'] = screenshot_entry['changed']
            old_gaia_hash = screenshot['gaia']
            new_gaia_hash = screenshot_entry['gaia']
            old_hg_hash = screenshot['hg']
            new_hg_hash = screenshot_entry['hg']
            screenshot['old_gaia'] = old_gaia_hash
            screenshot['old_hg'] = old_hg_hash
            if old_gaia_hash != new_gaia_hash:
              screenshot['gaia'] = new_gaia_hash
            if old_hg_hash != new_hg_hash:
              screenshot['hg'] = new_hg_hash
            break
        if not found:
          entry['screenshots'] = [screenshot_entry] + entry['screenshots']
          found = True
          break
        else:
          break
  if not found:
    for entry in db[data_id]:
      if entry['l10n'] == data_l10n:
        if app_categ in entry['position']:
          for screenshot in entry['screenshots']:
            if screenshot['id'] == screenshot_entry['id']:
              found = True
              screenshot['changed'] = screenshot_entry['changed']
              old_gaia_hash = screenshot['gaia']
              new_gaia_hash = screenshot_entry['gaia']
              old_hg_hash = screenshot['hg']
              new_hg_hash = screenshot_entry['hg']
              screenshot['old_gaia'] = old_gaia_hash
              screenshot['old_hg'] = old_hg_hash
              if old_gaia_hash != new_gaia_hash:
                screenshot['gaia'] = new_gaia_hash
              if old_hg_hash != new_hg_hash:
                screenshot['hg'] = new_hg_hash
              break
          if not found:
            entry['screenshots'] = [screenshot_entry] + entry['screenshots']
            found = True
            break
          else:
            break
  if not found:
    print '\n***not added to db: ' + data_id + ' ***'

def add_screenshot_to_id(db, data_id, data_l10n, app, app_categ, screenshot_entry):
  print data_id, data_l10n.encode('utf-8'), screenshot_entry
  found = False
  if len(db[data_id]) == 1:
    for screenshot in db[data_id][0]['screenshots']:
      if screenshot['id'] == screenshot_entry['id']:
        found=True
        screenshot['changed'] = screenshot_entry['changed']
        old_gaia_hash = screenshot['gaia']
        new_gaia_hash = screenshot_entry['gaia']
        old_hg_hash = screenshot['hg']
        new_hg_hash = screenshot_entry['hg']
        screenshot['old_gaia'] = old_gaia_hash
        screenshot['old_hg'] = old_hg_hash
        if old_gaia_hash != new_gaia_hash:
          screenshot['gaia'] = new_gaia_hash
        if old_hg_hash != new_hg_hash:
          screenshot['hg'] = new_hg_hash
        break
    if not found:
      db[data_id][0]['screenshots'] = [screenshot_entry] + db[data_id][0]['screenshots']
  else:
    check_duplicate(db, data_id, data_l10n, app, app_categ, screenshot_entry)

def log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, section=''):
  l10n_elems = client.find_elements('css selector', section + ' [data-l10n-id]')

  for i in l10n_elems:
    if i.is_displayed():
      data_id = i.get_attribute('data-l10n-id')
      data_l10n = i.text

      if db.has_key(data_id):
        add_screenshot_to_id(db, data_id, data_l10n, app, app_categ, screenshot_entry)
      else:
        if i.get_attribute('placeholder') and db.has_key(data_id + '.placeholder'):
          add_screenshot_to_id(db, data_id + '.placeholder', data_l10n, app, app_categ, screenshot_entry)
        else:
          #TO DO raise proper error
          print 'String with id "' + data_id + '" does not exist into db.json'

def create_screenshot_dir(locale, path):
  directory = 'screenshots/' + locale + '/' + path + '/'
  if not os.path.exists(directory):
    os.makedirs(directory)

def take_screenshot(locale, path, client, file_name):
  screenshot_name = 'screenshots/' + locale + '/' + path + '/' + file_name
  if os.path.exists(screenshot_name):
    os.rename(screenshot_name, screenshot_name + '.old.jpeg')
  file = open(screenshot_name, 'w')
  screenshot = client.screenshot()[22:]
  file.write(base64.decodestring(screenshot))
  file.close()
  if os.path.exists(screenshot_name + '.old.jpeg'):
    return screenshot_changed(screenshot_name)
  return False

def check_flags(test_flags, device_flags):
  for flag in test_flags:
    if test_flags[flag]:
      if not device_flags[flag]:
        return False
  return True

def screenshot_changed(screenshot_name):
  new = Image.open(screenshot_name)
  old = Image.open(screenshot_name + '.old.jpeg')
  diff = ImageChops.difference(new, old)
  if diff.getbbox():
    diff.save(screenshot_name + '.diff.jpeg', 'JPEG')
    print "-----Screenshot " + screenshot_name + ' changed-----'
    return True
  else:
    return False

def change_screen_timeout(client):
    client.execute_script("""
      let setlock = window.wrappedJSObject.SettingsListener.getSettingsLock();
      let obj = {'screen.timeout': 0};
      setlock.set(obj);
    """)  
