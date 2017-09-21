# Sample Hello World hdtv plugin

This sample plugin demonstrates, how user plugins are created and used in the nuclear spectrum analysis tool hdtv.

## Installation

User plugins are located in the `plugins` folder of the hdtv config directory, e. g. `~/.config/hdtv/plugins`.
If you don’t have any plugins yet, you will first have to create this folder.
Afterwards, clone this repository to the `helloworld` subdirectory of the plugins folder, e. g. `~/.config/hdtv/plugins/helloworld`.

Finally, you have to activate the plugin. Create the file `startup.py` in the hdtv config directory.
This file is automatically read and executed, when hdtv starts.
Add the following line to import the plugin:

```python
import plugins.helloworld
```

## Usage

Currently, the plugin outputs `Hello World!`, when hdtv is started. Additionally, a new command `helloworld` is added to the hdtv shell, that also prints `Hello World!`:

```
HDTV - Nuclear Spectrum Analysis Tool
Hello World!
hdtv> helloworld
Hello World!
hdtv>
```

