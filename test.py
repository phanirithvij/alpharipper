# category
from ripper import get_pages, singular_post

PLURALS = {
    "wall": "wallpapers",
    "mobile": "mobile wallpapers",
    "art": "artworks",
    "pics": "pics",
    "avatars": "avatars",
    "gifs": "gifs",
    "covers": "covers"
}


get_pages("https://mobile.alphacoders.com/by-category/3")
get_pages("https://wall.alphacoders.com/by_category.php?id=3")
get_pages("https://art.alphacoders.com/by_category/3")
get_pages("https://pics.alphacoders.com/by_category/3")
get_pages("https://avatars.alphacoders.com/by_category/3")
get_pages("https://gifs.alphacoders.com/by_category/3")
get_pages("https://covers.alphacoders.com/by_category/3")

# collections
get_pages("https://wall.alphacoders.com/by_collection.php?id=654")
get_pages("https://mobile.alphacoders.com/by-collection/654")
get_pages("https://art.alphacoders.com/arts/by_collection/654")
get_pages("https://pics.alphacoders.com/pictures/by_collection/654")
get_pages("https://avatars.alphacoders.com/avatars/by_collection/654")
get_pages("https://gifs.alphacoders.com/gifs/by_collection/654")
get_pages("https://covers.alphacoders.com/cover/by-collection/654")

# sub category
get_pages("https://mobile.alphacoders.com/by-sub-category/173190")
get_pages(
    "https://wall.alphacoders.com/by_sub_category.php?id=173190&name=One+Piece+Wallpapers")
get_pages("https://art.alphacoders.com/by_sub_category/173190")
get_pages("https://pics.alphacoders.com/by_sub_category/173190")
get_pages("https://avatars.alphacoders.com/by_sub_category/173190")
get_pages("https://gifs.alphacoders.com/by_sub_category/173190")
get_pages("https://covers.alphacoders.com/by_sub_category/173190")

# newest
get_pages("https://wall.alphacoders.com/newest_wallpapers.php")
get_pages("https://mobile.alphacoders.com/newest")
get_pages("https://gifs.alphacoders.com/gifs/newest")
get_pages("https://avatars.alphacoders.com/avatars/newest")
get_pages("https://art.alphacoders.com/arts/newest")
get_pages("https://pics.alphacoders.com/pictures/newest")
get_pages("https://covers.alphacoders.com/cover/newest/")
get_pages("https://covers.alphacoders.com/cover/newest/3/linkedin-background")

# authors
get_pages("https://wall.alphacoders.com/unregistered.php?id=38683")
get_pages("https://mobile.alphacoders.com/authors/view/24266")
get_pages("https://art.alphacoders.com/authors/view/48965")
get_pages("https://pics.alphacoders.com/authors/view/32388")
get_pages("https://avatars.alphacoders.com/authors/view/24266")
get_pages("https://gifs.alphacoders.com/authors")
# covers have no authors

# highest rated
get_pages("https://avatars.alphacoders.com/avatars/highest_rated")
get_pages("https://gifs.alphacoders.com/gifs/highest_rated")
get_pages("https://covers.alphacoders.com/cover/highest-rated")
get_pages("https://pics.alphacoders.com/pictures/highest_rated")
get_pages("https://art.alphacoders.com/arts/highest_rated")
get_pages("https://wall.alphacoders.com/highest_rated.php")
# no mobile top :(
# sub filters
get_pages("https://covers.alphacoders.com/cover/highest-rated/1/facebook-cover")

# wall specials
get_pages("https://wall.alphacoders.com/featured.php")
get_pages("https://wall.alphacoders.com/by_creator.php")
get_pages("https://wall.alphacoders.com/by_license.php?filter=4")
get_pages("https://wall.alphacoders.com/by_color.php?hex_color=498676")
get_pages("https://wall.alphacoders.com/by_resolution.php?w=7680&h=4320")

# most viewed
get_pages("https://wall.alphacoders.com/by_views.php")
get_pages("https://art.alphacoders.com/arts/by_views")
get_pages("https://pics.alphacoders.com/pictures/by_views")
get_pages("https://avatars.alphacoders.com/avatars/by_views")
get_pages("https://gifs.alphacoders.com/gifs/by_views")
get_pages("https://covers.alphacoders.com/cover/by-views")
get_pages("https://covers.alphacoders.com/cover/by-views/1/facebook-cover")
# no mobile most viewed :(

# most comments
get_pages("https://wall.alphacoders.com/by_comments.php")
get_pages("https://art.alphacoders.com/arts/by_comments")
get_pages("https://pics.alphacoders.com/pictures/by_comments")
get_pages("https://avatars.alphacoders.com/avatars/by_comments")
get_pages("https://gifs.alphacoders.com/gifs/by_comments")
# no mobilr, covers

# popular
get_pages("https://avatars.alphacoders.com/avatars/popular")
get_pages("https://pics.alphacoders.com/pictures/popular")
get_pages("https://wall.alphacoders.com/popular.php")
get_pages("https://art.alphacoders.com/arts/popular")
get_pages("https://gifs.alphacoders.com/gifs/popular")
get_pages("https://covers.alphacoders.com/cover/popular")
# no mobile :( popular

# tags
get_pages("https://wall.alphacoders.com/tags.php?tid=135")
get_pages("https://mobile.alphacoders.com/by-tag/135")
get_pages("https://art.alphacoders.com/by_tag/135")
get_pages("https://pics.alphacoders.com/by_tag/135")
get_pages("https://avatars.alphacoders.com/avatars/by_tag/135")
get_pages("https://gifs.alphacoders.com/gifs/by_tag/135")
get_pages("https://covers.alphacoders.com/by-tag/135")

# user profile
get_pages("https://wall.alphacoders.com/profile.php?id=47849")
get_pages("https://pics.alphacoders.com/users/profile/167118")
get_pages("https://art.alphacoders.com/users/profile/47849")
get_pages("https://gifs.alphacoders.com/users/profile/18905")
get_pages("https://mobile.alphacoders.com/users/profile/18905")
get_pages("https://avatars.alphacoders.com/users/profile/18905")

# by_favourites
get_pages("https://pics.alphacoders.com/pictures/by_favorites")
get_pages("https://art.alphacoders.com/arts/by_favorites")
get_pages("https://avatars.alphacoders.com/avatars/by_favorites")
get_pages("https://gifs.alphacoders.com/gifs/by_favorites")
get_pages("https://covers.alphacoders.com/cover/by-favorites")
get_pages("https://wall.alphacoders.com/by_favorites.php")
# no mobile :( favorites

# search
# mobile has no global search bar
get_pages(
    "https://mobile.alphacoders.com/by-device/541/iPhone-11-Pro-Max-Wallpapers?search=onepiece")
get_pages("https://wall.alphacoders.com/search.php?search=one+piece")
get_pages("https://pics.alphacoders.com/search?t=one+piece")
get_pages("https://gifs.alphacoders.com/gifs/search?t=gintama")
get_pages("https://art.alphacoders.com/search?t=gintama")
get_pages("https://covers.alphacoders.com/searches/view?search=gintama")
get_pages("https://avatars.alphacoders.com/searches/view?search=gintama")

# direct posts
singular_post("https://wall.alphacoders.com/big.php?i=841283")
singular_post(
    "https://mobile.alphacoders.com/wallpapers/view/809896/Anime-Noragami-Wallpapers")
singular_post("https://art.alphacoders.com/arts/view/135777")
singular_post("https://pics.alphacoders.com/pictures/view/238772")
singular_post("https://avatars.alphacoders.com/avatars/view/71560")
singular_post("https://gifs.alphacoders.com/gifs/view/1936")
singular_post("https://covers.alphacoders.com/cover/view/162090")

# micellaneous
# mobile by device
get_pages(
    "https://mobile.alphacoders.com/by-device/541/iPhone-11-Pro-Max-Wallpapers")
# mobile by resolution
get_pages("https://mobile.alphacoders.com/by-resolution/18/1440x1280-Wallpapers")
# covers by type
get_pages("https://covers.alphacoders.com/by-type/3/linkedin-background")
# avatars by resolution
get_pages("https://avatars.alphacoders.com/by_resolution/256")
