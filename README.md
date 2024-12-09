# ARCHIVE

Are wallpaper sites even worth it? the bandwidth consumed must be bonkers.

# Ripper

Extract wallpapers links from all aphacoder sites

List
- https://avatars.alphacoders.com/
- https://wall.alphacoders.com/
- https://mobile.alphacoders.com/
- https://art.alphacoders.com/
- https://pics.alphacoders.com/
- https://photos.alphacoders.com/
- https://gifs.alphacoders.com/
- https://covers.alphacoders.com/

There's an API [here](https://wall.alphacoders.com/api.php)

I'm not using the api to scrape but simple html `bs4` scraping.

Auth: Not implemented, Not needed (as every link is absolute and public)

Supports:
- Collections
- Categories
- Sub Categories
- Newest posts
- Authors
- Highest Rated
- Most Viewed
- Most Commented
- Popular
- Tags
- User profile
- By Favourites
- Search Results
- Individual Posts

If a page is specified in the url only that single page is parsed whereas if not specified it will query incrementing `page` till it sees that the server url is different from the requested url.

Check the examples `singlepage.py` for downloading images from a single page.
Check the examples `test.py` for recursive image extraction.
`print(pgs)` instead of `len(pgs)`
