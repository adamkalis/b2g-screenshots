# b2g-l10n-screenshots

## Requirements

* Linux Distribution with bash shell
* Python 2.7, dev python package and [virtuaenv package](https://pypi.python.org/pypi/virtualenv/)
* [Marionette - Python Client](https://developer.mozilla.org/en-US/docs/Marionette/Client)
* B2G device with [engineering build](https://developer.mozilla.org/en-US/docs/Marionette/Builds)
* adb access to this device
* git 
* mercurial

## Risks - Disclaimer
Similar to the risks that described at [mdn for gaia tests](https://developer.mozilla.org/en-US/docs/Gaia_Test_Runner) please proceed on your own risk. I am not responsible for any data loss or kind of damage.

## Instant start - How to generate screenshots for two locales

* Clone the repository: <pre>git clone https://github.com/adamkalis/b2g-screenshots</pre>
* Go into the cloned directory: <pre>cd b2g-screenshots</pre>
* Initialize the platform (you can choose your own [locale(s)](http://hg.mozilla.org/gaia-l10n)): <pre>make init -j4 LOCALES='en-US el'</pre>
* Make sure your device is connected: <pre>adb devices</pre>
* Run the scripts: <pre>make runscripts</pre>
* Get your screenshots at screenshots/en-US and screenshots/el directories

For more details about commands look at [the wiki](https://github.com/adamkalis/b2g-screenshots/wiki)

