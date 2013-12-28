Spotify Current Playing
=======================

Usage:
 * `/SPOTIFY` - Displays the current playing song info
 * `/GETSPOTTEMPL` - Shows the current template for `/SPOTIFY`
 * `/SETSPOTTEMPL` - Set the template for `/SPOTIFY`
 
`/SETSPOTTEMPL`
---------------

Controllers:
 * `%(randcolor)s` - Random color
 * `%(randcolor2)s` - `%(randcolor)s` will give the same color code
 * `%(randcolor2)s` - Same as above
 * `%(normal)s` - Removes all the applied IRC controls
 * `%(track)s` - The current playing track
 * `%(artist)s` - And the artist
 * You can use IRC control codes too
 
 Example: is playing %(randcolor)s%(track)s%(normal)s by %(randcolor2)s%(artist)s%(normal)s in 03Spotify
 (note that there is a invisable character before 03Spotify)
