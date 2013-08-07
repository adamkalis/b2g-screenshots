#!/bin/bash

case "$1" in
  init)
    shift
    if [ $# != 0 ]
    then
      for locale in $@
      do
       (hg clone http://hg.mozilla.org/gaia-l10n/$locale locales/$locale/; python ids_json.py $locale;) &
      done
      wait
    else
      for locale in $(python get_locales.py)
      do
       (hg clone http://hg.mozilla.org/gaia-l10n/$locale locales/$locale/; python ids_json.py $locale;) &
      done
      wait
    fi
    ;;

  add)
    shift
    #Check if locale already exists
    for locale in $@
    do
      if [ ! -d locales/$locale ]
      then
        locales=$locale' '$locales
      else
        echo "Locale $locale already exists"
      fi
    done
    #Adding locales
    for locale in $locales
    do
     (hg clone http://hg.mozilla.org/gaia-l10n/$locale locales/$locale/; python ids_json.py $locale;) &
    done
    wait
    ;;

  remove)
    shift
    #Check if locale does not exist
    for locale in $@
    do
      if [ -d locales/$locale ]
      then
        locales=$locale' '$locales
      else
        echo "Locale $locale does not exist"
      fi
    done
    #Adding locales
    for locale in $locales
    do
     (rm -rf locales/$locale/) &
    done
    wait
    ;;

  update)
    shift
    if [ $# != 0 ]
    then
      for locale in $@
      do
        if [ -d locales/$locale ]
        then
          locales=$locale' '$locales
        else
          echo "Locale $locale does not exist"
        fi
      done
      for locale in $locales
      do
       (hg pull -u -R locales/$locale; python ids_json.py $locale;) &
      done
      wait
    else
      for locale in $(ls locales)
      do
        (hg pull -u -R locales/$locale; python ids_json.py $locale;) &
      done
      wait
    fi
    ;;

  dupl)
    shift
    if [ $# != 0 ]
    then
      for locale in $@
      do
        if [ -d locales/$locale ]
        then
          locales=$locale' '$locales
        else
          echo "Locale $locale does not exist"
        fi
      done
      for locale in $locales
      do
        python find_duplicates.py $locale
      done
    else
      for locale in $(ls locales)
      do
        python find_duplicates.py $locale
      done
    fi
    ;;
esac
