CLI PE reader
=============

Just simple [PE](https://ru.wikipedia.org/wiki/Portable_Executable) fomrat file reader which print all PE data.

Not too much data is printed right now though. Working on it.

Usage
------

python3 pereader.py <filepath/file.exe>

Docs
----

* [Awesome PE explained image](https://i.imgur.com/tnUca.jpg)

Fetched (printed) data
-----------

* PE header address
* Machine Type
* Number of sections
* Characteristics
* Compiled for (32/64 bits)
* Entry Point

In Progress
-----------

* Get more data from Optional Header
* Print sections
