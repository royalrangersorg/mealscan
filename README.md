# Meal Scanning Software

The meal scanning software is intended to be used to scan tags that have barcodes to determine if someone has been through a line.

It consists of a python gui program and a small (optional) server component for remote detection


### Server component 

A sample php file has been included in /server that shows the type of response required for checking remote server for supporting multiple locations


### Settings File

The json settings file contains local settings

```
{"localonly":1,"host":"http://royalrangers.foo/check.php","location":"GREEN"}
```

* localonly (bool) - whether we should connect to a remote server 
* host (string) - the host we should connect to send data for checking
* location (string) - the location of this scanning station

### Local Saving

The software saves a file "mealscan.txt" with a plain text result of scans

The format saves is as follows

```
DATE      |MEAL |CODE|TIME
2016-04-26|DINNR|6|17:13:18
```

### Building Desktop Software

Enter into the src directory

```
$ python setup.py py2exe
```

### Dependencies

The gui software depends on the following python packages

* wx widgets
* pyglet
* request
* py2exe for compiling to windows
