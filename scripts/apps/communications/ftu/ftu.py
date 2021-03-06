import sys
import json
from marionette import Marionette
import base64
import time
from scripts.toolkit import create_screenshot_dir, take_screenshot
from scripts.toolkit import get_db, set_db, log_displayed_l10n_strings
from scripts.toolkit import check_flags, change_screen_timeout, set_time
from scripts.config import *


def ftu(locale, device_flags, hashes):

  db = get_db(locale)

  app = 'ftu'
  app_categ = 'communications'
  app_type = 'apps'
  gaia_hash = hashes[0]
  hg_hash = hashes[1]
  screenshot_path = app_type + '/' + app_categ + '/' + app

  create_screenshot_dir(locale, screenshot_path)

  client = Marionette('localhost', 2828)
  client.start_session()

  change_screen_timeout(client) 

  ftu_iframe = client.find_element('css selector',"iframe[src='app://communications.gaiamobile.org/ftu/index.html']")

  if client.switch_to_frame(ftu_iframe):

    time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#languages 
    file_name = 'languages'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#activation-screen')


      # switch to app://communications.gaiamobile.org/ftu/index.html#data_3g (unlock-sim-screen screen)
      next = client.find_element('css selector', '#forward')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim pin screen - unlock-sim-screen - 1st attempt)
    file_name = 'data_3g-unlock_sim_screen-pin_screen'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # invalid pin -> error about pin characters
      # stay at app://communications.gaiamobile.org/ftu/index.html#data_3g (unlock-sim-screen screen)
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim pin screen - unlock-sim-screen - pin error)
    file_name = 'data_3g-unlock_sim_screen-pin_screen-invalid_pin'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # insert wrong pin (attempt 1 of 3)
      pin_input = client.find_element('css selector', '#pin-input')
      pin_input.send_keys(wrong_sim_pin)

      # stay at app://communications.gaiamobile.org/ftu/index.html#data_3g (unlock-sim-screen screen)
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)
    
    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim pin screen - unlock-sim-screen - 2nd attempt)
    file_name = 'data_3g-unlock_sim_screen-pin_screen-wrong_pin-1st_time'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # insert wrong pin (attempt 2 of 3)
      pin_input = client.find_element('css selector', '#pin-input')
      pin_input.send_keys(wrong_sim_pin)

      # stay at app://communications.gaiamobile.org/ftu/index.html#data_3g (unlock-sim-screen screen)
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim pin screen - unlock-sim-screen - 3rd attempt)
    file_name = 'data_3g-unlock_sim_screen-pin_screen-wrong_pin-2nd_time'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # insert wrong pin (atempt 3 of 3) - continues to puk screen
      pin_input = client.find_element('css selector', '#pin-input')
      pin_input.send_keys(wrong_sim_pin)

      # switch to app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen)
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)

      # tap the header in order to hide keyboard and get full screenshot of the puk screen
      header = client.find_element('css selector', '#unlock-sim-header')
      header.tap()

    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen - 1st attempt)
    file_name = 'data_3g-unlock_sim_screen-puk_screen'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # invalid puk -> error about puk characters
      # stay at app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen)
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen - puk error)
    file_name = 'data_3g-unlock_sim_screen-puk_screen-invalid_puk'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # insert wrong puk - invalid new pin -> error about pin characters
      puk_input = client.find_element('css selector', '#puk-input')
      puk_input.send_keys(wrong_sim_puk)

      # stay at app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen)
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen - pin error)
    file_name = 'data_3g-unlock_sim_screen-puk_screen-invalid_new_pin'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # insert new pin without confirmed it -> error about pin confirmation (wrong puk is preserved at its input)
      newpin_input = client.find_element('css selector', '#newpin-input')
      newpin_input.send_keys(sim_pin)

      # stay at app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen)
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen - pin error)
    file_name = 'data_3g-unlock_sim_screen-puk_screen-invalid_new_pin_confirmation'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # insert confirmation of the new pin (wrong puk and new pin are preserved at their inputs)
      newpin_input = client.find_element('css selector', '#confirm-newpin-input')
      newpin_input.send_keys(sim_pin)

      # wrong puk (attempt 1 of 9)
      # stay at app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen)
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen - puk error)
    file_name = 'data_3g-unlock_sim_screen-puk_screen-wrong_puk-1st_time'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # insert wrong puk (attempt 2 of 9) (new pin and its confirmation are preserved at their inputs)
      puk_input = client.find_element('css selector', '#puk-input')
      puk_input.send_keys(wrong_sim_puk)

      # stay at app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen)
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#data_3g (sim puk screen - unlock-sim-screen - 2nd attempt)
    file_name = 'data_3g-unlock_sim_screen-puk_screen-wrong_puk-2nd_time'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#unlock-sim-screen')


      # insert right puk (attempt 2 of 9) (new pin and its confirmation are preserved at their inputs)
      puk_input = client.find_element('css selector', '#puk-input')
      puk_input.send_keys(sim_puk)

      # switch to app://communications.gaiamobile.org/ftu/index.html#data_3g
      next = client.find_element('css selector', '#unlock-sim-button')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#data_3g
    file_name = 'data_3g'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {
      "sim": True,
      "no-sim": False}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#activation-screen')


      # switch to app://communications.gaiamobile.org/ftu/index.html#wifi
      next = client.find_element('css selector', '#forward')
      next.tap()
      time.sleep(long_time)

      # enable overlay "scanningNetworks" spinner screen (loading-overlay)
      client.execute_script("window.wrappedJSObject.utils.overlay.show('scanningNetworks', 'spinner');")
      time.sleep(middle_time)
    
    # overlay "scanningNetworks" spinner screen
    file_name = 'wifi-loading_overlay-scanning_networks'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#loading-overlay')


      # disable overlay "scanningNetworks" spinner screen
      client.execute_script("window.wrappedJSObject.utils.overlay.hide('scanningNetworks', 'spinner');")
      time.sleep(middle_time)

    # app://communications.gaiamobile.org/ftu/index.html#wifi
    file_name = 'wifi'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#wifi')


      # switch to app://communications.gaiamobile.org/ftu/index.html#date_and_time
      next = client.find_element('css selector', '#forward')
      next.tap()
      time.sleep(short_time)

    # Set time in order to be the same at every screenshot
    set_time(client)

    # app://communications.gaiamobile.org/ftu/index.html#date_and_time
    file_name = 'date_and_time'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#date_and_time')


      # switch to app://communications.gaiamobile.org/ftu/index.html#geolocation
      next = client.find_element('css selector', '#forward')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#geolocation
    file_name = 'geolocation'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#geolocation')


      # switch to app://communications.gaiamobile.org/ftu/index.html#import_contacts
      next = client.find_element('css selector', '#forward')
      next.tap()
      time.sleep(middle_time)

    # app://communications.gaiamobile.org/ftu/index.html#import_contacts
    file_name = 'import_contacts'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry, '#import_contacts')


      # switch to app://communications.gaiamobile.org/ftu/index.html#welcome_browser
      next = client.find_element('css selector', '#forward')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#welcome_browser
    file_name = 'welcome_browser'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry)


      # switch to app://communications.gaiamobile.org/ftu/index.html#browser_privacy
      next = client.find_element('css selector', '#forward')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#browser_privacy
    file_name = 'browser_privacy'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry)


      # switch to app://communications.gaiamobile.org/ftu/index.html#step1 (first tutorial screen)
      next = client.find_element('css selector', '#forward')
      next.tap()
      time.sleep(long_time)

    # app://communications.gaiamobile.org/ftu/index.html#step1 (first tutorial screen)
    file_name = 'step1-first_tutorial_screen'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry)


      # switch to app://communications.gaiamobile.org/ftu/index.html#step1
      next = client.find_element('css selector', '#lets-go-button')
      next.tap()
      time.sleep(long_time)

    # app://communications.gaiamobile.org/ftu/index.html#step1
    file_name = 'step1'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry)


      # switch to app://communications.gaiamobile.org/ftu/index.html#step2
      next = client.find_element('css selector', '#forwardTutorial')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#step2
    file_name = 'step2'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry)


      # switch to app://communications.gaiamobile.org/ftu/index.html#step3
      next = client.find_element('css selector', '#forwardTutorial')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#step3
    file_name = 'step3'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry)


      # switch to app://communications.gaiamobile.org/ftu/index.html#step4
      next = client.find_element('css selector', '#forwardTutorial')
      next.tap()
      time.sleep(short_time)

    # app://communications.gaiamobile.org/ftu/index.html#step4
    file_name = 'step4'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry)


      # switch to app://communications.gaiamobile.org/ftu/index.html#step4 (last tutorial screen)
      next = client.find_element('css selector', '#forwardTutorial')
      next.tap()
      time.sleep(long_time)

    # app://communications.gaiamobile.org/ftu/index.html#step4 (last tutorial screen)
    file_name = 'step4-last_tutorial_screen'
    screenshot_entry = {
      "id" : file_name,
      "script" : app,
      "gaia" : gaia_hash,
      "hg" : hg_hash,
      "changed" : False,
      "path" : screenshot_path}
    test_flags = {}
    if check_flags(test_flags, device_flags):
      screenshot_entry.update(test_flags)
      if take_screenshot(locale, screenshot_path, client, file_name):
        screenshot_entry['changed'] = True
      log_displayed_l10n_strings(client, db, app, app_categ, screenshot_entry)


      # Close ftu frame
      next = client.find_element('css selector', '#tutorialFinished')
      next.tap()
      time.sleep(short_time)

    set_db(locale, db)

  else:
  #TO DO raise proper error
    print "switch to ftu frame failed"
