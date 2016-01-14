# autotorrent
Python script for torrenting Spotify playlists

Credits for the API go to karan with the Unofficial Python API for TPB (https://github.com/karan/TPB)

The API is packaged with this script and is updated for Python 3.5.

Everything else is my messy code. Please don't look at it, it's pretty bad, but it works (kinda)

The default version is for Windows, but the 'unix' folder contains a new main.py and tpb.py that will work on Mac and possibly Linux. Haven't tested it on Linux yet. The Unix version has fancy color codes and a workaround because something is not working with TPB and Python's urllib. 

The only dependency is LXML for Python 3.5, you can install by pip on Unix or grab the wheel for Windows here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml





== USAGE ==

Run main.py from the terminal or whatever

Main menu will show up (if it didn't then it's broke)

Enter '1' or '2' for a manual search or to import and torrent a playlist, respectively. 

Playlists should be saved in the same directory as main.py as "playlist.csv", the exporter can be found here: http://joellehman.com/playlist/

In manual mode, enter a search term and the torrents will display. Enter any number to choose a torrent and add it to the list of magnet links.

You can enter 'q' to save and quit or 'r' to redo a search without adding anything to the list.

After you're done, the script will output a list of magnet links that you can paste into your web browser or torrent client


In import mode, the script reads from playlist.csv and searches for each album automatically. You're still given control over it, however.

If the program searches and doesn't find anything, you can try searching by artist with 'a' (the script defaults to album)
Or input 'm' for manual mode or 's' to skip or 'q' to quit.

That's about it, have fun




== KNOWN BUGS == 

Sometimes on Windows, a search will return a result with a character that causes an error in encoding. I don't quite know how to fix this, it's only happened once to me so I don't forsee it being a huge problem.
