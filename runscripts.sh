#!/bin/bash

if [ ! -z "$APPS" ]
then
  for app in $APPS
  do
    if [ -z "$APPS_LIST" ]
    then
      APPS_LIST=$app
    else
      APPS_LIST=$app,$APPS_LIST
    fi
  done
  ARGS="-a $APPS_LIST"
fi

if [ ! -z "$L10N_IDS" ]
then
  for id in $L10N_IDS
  do
    if [ -z "$IDS_LIST" ]
    then
      IDS_LIST=$id
    else
      IDS_LIST=$id,$IDS_LIST
    fi
  done
  ARGS="$ARGS -i $IDS_LIST"
fi

if [ ! -z "$L10N_FILES" ]
then
  for file in $L10N_FILES
  do
    if [ -z "$FILES_LIST" ]
    then
      FILES_LIST=$file
    else
      FILES_LIST=$file,$FILES_LIST
    fi
  done
  ARGS="$ARGS -p $FILES_LIST"
fi

if [ ! -z "$FLAGS" ]
then
  for flag in $FLAGS
  do
    if [ -z "$FLAGS_LIST" ]
    then
      FLAGS_LIST=$flag
    else
      FLAGS_LIST=$flag,$FLAGS_LIST
    fi
  done
  ARGS="$ARGS -f $FLAGS_LIST"
fi

GAIA_HASH=$(git --git-dir=gaia/.git log --pretty=format:"%h" -1)

if [ ! -z "$LOCALES" ]
then
  for locale in $LOCALES
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
    adb wait-for-device
    (cd gaia; make clean && make production GAIA_DEFAULT_LOCALE=$locale LOCALES_FILE=locales/languages_all.json LOCALE_BASEDIR=../locales/ REMOTE_DEBUGGER=1)
    adb wait-for-device
    adb forward tcp:2828 tcp:2828
    echo connected to adb - wait for device to fully load GAIA
    HG_HASH=$(hg -R locales/$locale id -i)
    HASHES="$GAIA_HASH,$HG_HASH"
    sleep 40s
    env/bin/python runscripts.py -l $locale $ARGS -h $HASHES
  done
else
  for locale in $(ls locales)
  do
    adb wait-for-device
    (cd gaia ; make clean && make production GAIA_DEFAULT_LOCALE=$locale LOCALES_FILE=locales/languages_all.json LOCALE_BASEDIR=../locales/ REMOTE_DEBUGGER=1)
    HG_HASH=$(hg -R locales/$locale id -i)
    HASHES="$GAIA_HASH,$HG_HASH"
    adb wait-for-device
    adb forward tcp:2828 tcp:2828
    echo connected to adb - wait for device to fully load GAIA
    sleep 40s
    env/bin/python runscripts.py -l $locale $ARGS -h $HASHES
  done
fi
