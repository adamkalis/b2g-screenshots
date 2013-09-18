#!/bin/bash

case "$1" in
  init | add)
    shift
    if [ $# != 0 ]
    then
      #Check if locale already exists
      for locale in $@
      do
        if [ ! -d locales/$locale ]
        then
          AVAIL_LOCALES=$locale' '$AVAIL_LOCALES
        else
          echo "Locale $locale already exists"
        fi
      done
      #Initialize locales
      for locale in $AVAIL_LOCALES
      do
       (hg clone http://hg.mozilla.org/gaia-l10n/$locale locales/$locale/;
        python ids_json.py $locale;
        mkdir -p results/screenshots/$locale) &
      done
      wait
    else
      #Check if locale already exists
      for locale in $(python get_locales.py)
      do
        if [ ! -d locales/$locale ]
        then
          AVAIL_LOCALES=$locale' '$AVAIL_LOCALES
        else
          echo "Locale $locale already exists"
        fi
      done
      #Initialize locales
      for locale in $AVAIL_LOCALES
      do
       (hg clone http://hg.mozilla.org/gaia-l10n/$locale locales/$locale/;
        python ids_json.py $locale;
        mkdir -p results/screenshots/$locale) &
      done
      wait
    fi
    ;;

  remove)
    shift
    #Check if locale does not exist
    for locale in $@
    do
      if [ -d locales/$locale ]
      then
        AVAIL_LOCALES=$locale' '$AVAIL_LOCALES
      else
        echo "Locale $locale does not exist"
      fi
    done
    #Removing locales
    for locale in $AVAIL_LOCALES
    do
     (rm -rf locales/$locale/;
      rm -rf results/screenshots/$locale/) &
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
          AVAIL_LOCALES=$locale' '$AVAIL_LOCALES
        else
          echo "Locale $locale does not exist"
        fi
      done
      for locale in $AVAIL_LOCALES
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
          AVAIL_LOCALES=$locale' '$AVAIL_LOCALES
        else
          echo "Locale $locale does not exist"
        fi
      done
      for locale in $AVAIL_LOCALES
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
