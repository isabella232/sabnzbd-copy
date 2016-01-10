# sabnzbd-copy #

This is a python script for post processing in sabnzbd

The largest file will be copied depending on the configuration.

You can configure where movies and tv shows will be copied

# Installtion

Checkout the project.

In the directory do
```bash
python3 setup.py install
```

# Configuration

Configuration is done in $HOME/.sabnzbd-copy 

Example:
```json
{
	"basePath" : "/media/videos",
	"categories" : {
		"tvshows" : {		
			"patterns" : {
				"TVShow" : ["^tvshow"],
				"Old Tv Show": ["^old.tv.show"]
			},
			"subFolder" : "Serien",
			"miscFolder" : "temp"
		},
		"movies" : {
			"subFolder" : "Filme"
		}
	}
}
```

`basePath` defines the base path for all other paths defined in the configuration

`categories` defines the supported categories. 

A category has

* `subFolder` in which all files for this pattern have to moved
* `patterns` for more specific matches on subfolder
* `miscFolder` for all files that could not be matched (if not defined, the `subFolder` will be used)

A pattern consists of a folder and a list of regexes that are interpreted case insensitive. If a regex mathches on the largest file, the file will be moved in this folder which is a subfolder of the category `subFolder`.

# Prerequisites

* python3
* setuptools
