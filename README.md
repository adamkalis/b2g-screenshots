# b2g-l10n-screenshots

## Requirements

* Linux Distribution with bash shell
* Python 2.7
* [Marionette - Python Client](https://developer.mozilla.org/en-US/docs/Marionette/Client)
* B2G device

## Main Commands

#### *make init [LOCALES=' [locale] [other_locale] ']*

The command "make init" initializes the project in three steps using "make clone-gaia" and "make hg-init":

1. Clones [gaia repository](https://github.com/mozilla-b2g/gaia) and checkout the [v1-train branch](https://github.com/mozilla-b2g/gaia/tree/v1-train)
2. Initialize (downloading) the given locales in argument "LOCALES". If no locales are provided, it will download all the available from [gaia-l10n mercurial repository](http://hg.mozilla.org/gaia-l10n)
3. Creates for every downloaded locale a database json file "db.json", in which stores by id
  * the localized string
  * the .properties file that stores this string
  * the screenshot list that stores screenshots where the string shows up (initialy will be empty)

##### Examples:

<pre>
make init LOCALES='en-US cs ro'
</pre>
This will create a v1-train-branch "gaia" directory, "en-US", "cs" and "ro" directories inside "locales" directory and their db.json files

<pre>
+gaia
-locales
  +en-US
  -cs
    db.json
    +apps
    +shared
    +showcase_apps
    +test_apps
    +test_external_apps
  +ro
</pre>

* * *
<pre>
make init LOCALES='en-GB'
</pre>
This will create a v1-train-branch "gaia" directory, "en-GB" directory inside "locales" directory and its db.json file

<pre>
+gaia
-locales
  +en-US
  -cs
    db.json
    +apps
    +shared
    +showcase_apps
    +test_apps
    +test_external_apps
  +ro
</pre>

* * *
<pre>
make init
</pre>
This will create a v1-train-branch "gaia" directory, all available locales inside "locales" directory and their db.json files

<pre>
+gaia
-locales
  +ar
  -as
    db.json
    +apps
    +shared
    +showcase_apps
    +test_apps
    +test_external_apps
  +ast
    .
    .
    .
  +vi
  +zh-CN
  +zh-TW
</pre>

#### *make update [LOCALES=' [locale] [other_locale] ']*

The command "make update" updates the project in three steps using "make update-gaia" and "make update-hg":

1. Pull the latest changes of [v1-train branch](https://github.com/mozilla-b2g/gaia/tree/v1-train) from [gaia repository](https://github.com/mozilla-b2g/gaia)
2. Updates the given locales in argument "LOCALES". If no locales are provided, it will update all the locales inside locales directory
3. Creates for every updated locale a database json file "db.json", in which stores by id
  * the localized string
  * the .properties file that stores this string
  * the screenshot list that stores screenshots where the string shows up (initialy will be empty)

##### Examples:

<pre>
make update LOCALES='el ca pl'
</pre>
This will update v1-train-branch "gaia" repository with the latest changes and "el", "ca" and "pl" locales inside "locales" directory and will create their db.json files

* * *
<pre>
make update LOCALES='ko'
</pre>
This will update v1-train-branch "gaia" repository with the latest changes and "ko" locale inside "locales" directory and will create its db.json file

* * *
<pre>
make update
</pre>
This will update v1-train-branch "gaia" repository with the latest changes and all locales inside "locales" directory and create their db.json files

#### *make add-locales LOCALES=' locale [other_locale] '*

The command "make add-locales" adds new locales to the current ones in two steps:

1. Initialize (downloads) the given locales in argument "LOCALES". If no locales are provided does nothing.
2. Creates for every added locale a database json file "db.json", in which stores by id
  * the localized string
  * the .properties file that stores this string
  * the screenshot list that stores screenshots where the string shows up (initialy will be empty)

##### Example:

<pre>
make add-locales LOCALES='hi-IN sq'
</pre>
This will create "hi-IN" and "sq" directories inside "locales" directory and their db.json files

* * *
<pre>
make add-locales LOCALES='pt-BR'
</pre>
This will create "pt-BR" directory inside "locales" directory and its db.json file

#### *make remove-locales LOCALES=' locale [other_locale] '*

The command "make remove-locales" removes locales from the current ones in one step:

1. Removes the given locales in argument "LOCALES". If no locales are provided does nothing.

##### Examples:

<pre>
make remove-locales LOCALES='es cy'
</pre>
This will remove "es"and "cy" directories inside "locales" directory and their db.json files

* * *
<pre>
make add-locales LOCALES='zh-CN'
</pre>
This will remove "zh-CN" directory inside "locales" directory and its db.json file

#### *make find-dupl-locales [LOCALES=' [locale] [other_locale] ']*


##### Examples:
